import discord
from discord.ext import commands
from discord import app_commands
import json
import random
import time
import asyncio
import datetime
from typing import Literal
import datetime
from datetime import timedelta

class economy(commands.Cog):
    def __init__(self, client):
        self.client = client 



    @commands.hybrid_command(name="leaderboard", description="View the top ten richest players!", aliases = ["lb", "top"])
    async def leaderboard(self, ctx: commands.Context) -> None:
      with open("json/bank.json", "r") as f:
        bank = json.load(f)
      net_worths = {user_id: info['wallet'] + info['bank'] for user_id, info in bank.items()}
      top_10_net_worths = dict(sorted(net_worths.items(), key=lambda item: item[1], reverse=True)[:10])
      leaderboard_info = []
      for i, (user_id, amount) in enumerate(top_10_net_worths.items()):
          user = await self.client.fetch_user(user_id)
          leaderboard_info.append("\n\u200b" + f'{i+1}. {user.name}:' + ' ${:,}'.format(int(amount)))
      leaderboard_string = '\n'.join(leaderboard_info)
      leaderboard = discord.Embed(
        title = "Economy Leaderboard",
        description = "*Top 10 Richest Players*",
        color = discord.Color.green()
      )
      leaderboard.add_field(
        name = "Leaderboard",
        value = leaderboard_string,
        inline = False
      )
      leaderboard.set_thumbnail(url = "https://cdn-icons-png.flaticon.com/512/3716/3716691.png")
      leaderboard.set_footer(text = f"Requested by {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
      await ctx.send(embed = leaderboard)




    @commands.hybrid_command(name="open_account", description="Open an account for economy purposes.")
    async def open_account(self, ctx: commands.Context) -> None:
      with open("json/bank.json", "r") as f:
        bank = json.load(f)
      with open("json/inventory.json", "r") as f:
        inventory = json.load(f)
      if f"{ctx.author.id}" not in bank:
        bank[ctx.author.id] = {}
        bank[ctx.author.id]["wallet"] = 0
        bank[ctx.author.id]["bank"] = 0
        await ctx.send("Account created!")
      if f"{ctx.author.id}" not in inventory:
        inventory[ctx.author.id] = {}
        inventory[ctx.author.id]["small_apartment"] = 0
        inventory[ctx.author.id]["news_station"] = 0
        inventory[ctx.author.id]["empty_storefront"] = 0
        inventory[ctx.author.id]["business_down_payment"] = 0
        inventory[ctx.author.id]["law_tuition"] = 0
        await ctx.send("Inventory Initialized!")
      else:
        await ctx.send("You already have an account!")
      with open("json/bank.json", "w") as f:
        bank = json.dump(bank, f)
      with open(f"json/inventory.json", "w") as f:
        inventory = json.dump(inventory, f)

    @commands.hybrid_command(name = "close_account", description = "Close your account.")
    async def close_account(self, ctx: commands.Context) -> None:
      with open(f"json/bank.json", "r") as f:
        bank = json.load(f)
      with open(f"json/inventory.json", "r") as f:
        inventory = json.load(f)
      check = discord.Embed(
      title = "**WAIT!**",
      description = "Are you SURE you want to close your account? You will lose ALL of your money and your inventory.",
      color = discord.Color.red()
      )
      check.set_footer(text = "Type 'yes' to confirm or 'no' to cancel.")
      await ctx.reply(embed = check)
      msg = await self.client.wait_for("message" , check = lambda message: message.author == ctx.author)
      try:
        if msg.content == "yes":
          bank.pop(str(ctx.author.id))
          inventory.pop(str(ctx.author.id))
          with open(f"json/bank.json", "w") as f:
            bank = json.dump(bank, f)
          with open(f"json/inventory.json", "w") as f:
            inventory = json.dump(inventory, f)
          await ctx.send("Account closed!")
        elif msg.content == "no":
          await ctx.send("Cancelled! Your account is still open.")
        else:
          await ctx.send("Cancelled! Your account is still open.")
      except KeyError:
        await ctx.send("You don't seem to have an account yet! Open one by using `.open_account`.")
        await ctx.send("You don't seem to have an account yet!")

    @commands.hybrid_command(name="balance", description = "View the balance of a player!", aliases = ["bal"])
    @app_commands.describe(
      user = "The user you want to view the balance of.",
    )
    async def balance(self, ctx: commands.Context, user : discord.Member = None) -> None:
      with open(f"json/bank.json", "r") as f:
        bank = json.load(f)
      if user == None:
        user = ctx.author
      if not f"{user.id}" in bank:
        await ctx.send("This user does not have an account! Open one by using the command `.open_account`.")
        await ctx.send("This user does not have an account!")
      else:
        net_worth = bank[str(user.id)]["wallet"] + bank[str(user.id)]["bank"]
        balance = discord.Embed(
          title = "Balance",
          description = f"*{user.name}'s Balance*",
          color = discord.Color.blurple()
        )
        balance.add_field(
          name = "Wallet",
          value = "${:,}".format(int(bank[str(user.id)]["wallet"])),
          inline = True
        )
        balance.add_field(
          name = "Bank",
          value = "${:,}".format(int(bank[str(user.id)]["bank"])),
          inline = True
        )
        balance.add_field(
          name = "Net Worth",
          value = "${:,}".format(int(net_worth)),
          inline = False
        )
        balance.set_thumbnail(url = "https://i.imgur.com/xcRGqcB.png")
        balance.set_footer(text = f"Requested by {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
        await ctx.reply(embed = balance)

    @commands.hybrid_command(name="add_money", description = "Add money to a player!")  
    @app_commands.describe(
      user = "The user you want to add money to",
      amount = "The amount of money you want to add",
    )
    async def add_money(self, ctx: commands.Context, user : discord.Member = None, amount = None) -> None:
      with open(f"json/bank.json", "r") as f:
        bank = json.load(f)
      if amount == None:
        await ctx.send("Please specify an amount!")
      else:
        if user == None:
          user = ctx.author
        if not f"{user.id}" in bank:
          await ctx.send("This user does not have an account! Perhaps suggest they open an account using `.open_account`?")
        else:        
          if user == None:
            user = ctx.author
          bank[str(user.id)]["wallet"] += int(amount)
          await ctx.send("Added ${:,}".format(int(amount)) + f" to {user.mention}'s wallet!")
          with open(f"json/bank.json", "w") as f:
            bank = json.dump(bank, f)

    @add_money.error
    async def add_money_error(self, ctx, error):
      if isinstance(error, commands.MissingRole):
        await ctx.send("You do not have the required role to use this command!")

    @commands.hybrid_command(name="money_party", description = "Gives money to all users in the economy system!")
    @commands.has_role(1060315345266683955)
    async def money_party(self, ctx: commands.Context, amount = None) -> None:
      with open("json/bank.json", "r") as f:
        bank = json.load(f)
      if amount == None:
        await ctx.send("Please specify an amount!")
      else:
        for user in bank:
          bank[str(user)]["wallet"] += int(amount)
          await ctx.send("Added ${:,}".format(int(amount)) + f" to all users!")
          with open(f"json/bank.json", "w") as f:
            bank = json.dump(bank, f)

    @commands.hybrid_command(name="remove_money", description = "Remove money from a player!")  
    @app_commands.describe(
      user = "The user you want to remove money from",
      amount = "The amount of money you want to remove",
    )
    @commands.has_role(1060315345266683955)
    async def remove_money(self, ctx: commands.Context, user : discord.Member = None, amount = None) -> None:
      with open(f"json/bank.json", "r") as f:
        bank = json.load(f)
      if amount == None:
        await ctx.send("Please specify an amount!")
      else:
        if user == None:
          user = ctx.author
        if not f"{user.id}" in bank:
          await ctx.send("This user does not have an account! Perhaps suggest they open an account using `.open_account`?")
        else:        
          if user == None:
            user = ctx.author
          bank[str(user.id)]["wallet"] -= int(amount)
          await ctx.send("Removed ${:,}".format(int(amount)) + f" from {user.mention}'s wallet!")
          with open(f"json/bank.json", "w") as f:
            bank = json.dump(bank, f)

    @remove_money.error
    async def remove_money_error(self, ctx, error):
      if isinstance(error, commands.MissingRole):
        await ctx.send("You do not have the required role to use this command!")

    @commands.hybrid_command(name="deposit", description = "Deposit money into your bank!", aliases = ["dep", "d"])
    @app_commands.describe(
      amount = "The amount of money you want to deposit",
    )
    async def deposit(self, ctx: commands.Context, amount = None) -> None:
      if amount == None:
        await ctx.send("Please specify an amount!")
      else:
        with open(f"json/bank.json", "r") as f:
          bank = json.load(f)
        if not f"{ctx.author.id}" in bank:
          await ctx.send("You do not have an account! Make one by typing `.open_account`!")
          await ctx.send("You do not have an account!")
        elif amount != "all" and bank[str(ctx.author.id)]["wallet"] < int(amount):
          await ctx.send("You do not have that much money in your wallet!")
        else:
          if amount == "all":
            all = bank[str(ctx.author.id)]["wallet"]
            bank[str(ctx.author.id)]["wallet"] -= all
            bank[str(ctx.author.id)]["bank"] += all
            deposit = discord.Embed(
              title = "Deposit",
              description = "Deposited ${:,}".format(int(all)) + f" to your bank!",
              color = discord.Color.green()
            )
            deposit.set_footer(text = f"Requested by {ctx.author.name}")
            await ctx.reply(embed = deposit)
          else:
            bank[str(ctx.author.id)]["wallet"] -= int(amount)
            bank[str(ctx.author.id)]["bank"] += int(amount)
            deposit = discord.Embed(
              title = "Deposit",
              description = "Deposited ${:,}".format(int(amount)) + f" to your bank!",
              color = discord.Color.green()
            )
            deposit.set_footer(text = f"Requested by {ctx.author.name}")
            await ctx.reply(embed = deposit)
          with open(f"json/bank.json", "w") as f:
            bank = json.dump(bank, f)

    @commands.hybrid_command(name = "withdraw", description = "Withdraw money from your bank!", aliases = ["with", "w"])
    async def withdraw(self, ctx: commands.Context, amount = None) -> None:
      if amount == None:
        await ctx.send("Please specify an amount!")
      else:
        with open(f"json/bank.json", "r") as f:
          bank = json.load(f)
        if not f"{ctx.author.id}" in bank:
          await ctx.send("You do not have an account! Create one by doing `.open_account`.")
          await ctx.send("You do not have an account!")
        elif amount != "all" and bank[str(ctx.author.id)]["bank"] < int(amount):
          await ctx.send("You do not have that much money in your bank!")
        else:
          if amount == "all":
            all = bank[str(ctx.author.id)]["bank"]
            bank[str(ctx.author.id)]["bank"] -= all
            bank[str(ctx.author.id)]["wallet"] += all
            withdraw = discord.Embed(
              title = "Withdraw",
              description = "Withdrew ${:,}".format(int(all)) + f" from your bank!",
              color = discord.Color.green()
            )
            withdraw.set_footer(text = f"Requested by {ctx.author.name}")
            await ctx.reply(embed = withdraw)
          else:
            bank[str(ctx.author.id)]["bank"] -= int(amount)
            bank[str(ctx.author.id)]["wallet"] += int(amount)
            withdraw = discord.Embed(
              title = "Withdraw",
              description = "Withdrew ${:,}".format(int(amount)) + f" from your bank!",
              color = discord.Color.green()
            )
            withdraw.set_footer(text = f"Requested by {ctx.author.name}")
            await ctx.reply(embed = withdraw)
          with open(f"json/bank.json", "w") as f:
            bank = json.dump(bank, f)

    @commands.hybrid_command(name="work", description="Work for money!")
    @commands.cooldown(1, 5400, commands.BucketType.user)
    async def work(self, ctx: commands.Context) -> None:
      with open(f"json/bank.json", "r") as f:
        bank = json.load(f)
      amount = random.randint(100, 500)
      if not f"{ctx.author.id}" in bank:
        await ctx.send("You do not have an account! Open one with `.open_account`.")
        await ctx.send("You do not have an account!")
      else:
        bank[str(ctx.author.id)]["wallet"] += amount
        work = discord.Embed(
          title = "Work",
          description = f"You worked odd jobs and earned ${amount}!",
          color = discord.Color.green()
        )
        work.set_footer(text = f"{ctx.author.name}")
        await ctx.reply(embed = work)
        with open(f"json/bank.json", "w") as f:
          bank = json.dump(bank, f)

    @work.error
    async def work_error(self, ctx, error):
      remaining_time = str(datetime.timedelta(seconds=int(error.retry_after)))
      if isinstance(error, commands.CommandOnCooldown):
        error = discord.Embed(
          title = "Cooldown",
          description = f"You are on cooldown! Try again in {remaining_time}",
          color = discord.Color.red()
        )
        error.set_footer(text = f"{ctx.author.name}")
        await ctx.reply(embed = error)

    @commands.command(name="rob", description="Rob a user!")
    @app_commands.describe(
      member = "The user you want to rob."
    )
    @commands.cooldown(1, 10800, commands.BucketType.user)
    async def rob(self, ctx: commands.Context, member: discord.Member = None) -> None:
      rob_fail = ["Caught!", "Caught Red-Handed", "You Were Caught!"]
      with open(f"json/bank.json", "r") as f:
        bank = json.load(f)
      if member == None:
        error = discord.Embed(
          title = "Error",
          description = "You cannot rob yourself!",
          color = discord.Color.red()
        )
        await ctx.reply(embed = error)
      if not f"{ctx.author.id}" in bank:
        await ctx.send("You do not have an account! Open one with `.open_account`.")
        await ctx.send("You do not have an account!")
      elif not f"{member.id}" in bank:
        await ctx.send("That user does not have an account!")
      else:
        roll = random.randint(1, 100)
        if roll < 50:
          max = bank[str(member.id)]["wallet"]
          amount = random.randint(100, int(max))
          bank[str(ctx.author.id)]["wallet"] += amount
          bank[str(member.id)]["wallet"] -= amount
          await ctx.send(f"You robbed ${amount} from {member.name}!")
        else:
          amount = random.randint(300, 1000)
          bank[str(ctx.author.id)]["wallet"] -= amount
          caught = discord.Embed(
            title = random.choice(rob_fail),
            description = f"You were caught attempting to rob {member.name} and paid ${amount} to the police!",
            color = discord.Color.red()
          )
          caught.set_footer(text = f"{ctx.author.name}")
          await ctx.reply(embed = caught)
        with open(f"json/bank.json", "w") as f:
          bank = json.dump(bank, f)

    @rob.error
    async def rob_error(self, ctx, error):
      if isinstance(error, commands.CommandInvokeError):
        error = discord.Embed(
          title = "Error",
          description = "Target is too poor to rob!",
          color = discord.Color.red()
        )
        error.set_footer(text = f"{ctx.author.name}")
        await ctx.reply(embed = error)
      if isinstance(error, commands.CommandOnCooldown):
        minutes, seconds = divmod(error.retry_after, 60)
        hours, minutes = divmod(minutes, 60)
        embed = discord.Embed(
          title = "You're on cooldown!",
          description = f"Please wait {int(hours)} hours, {int(minutes)} minutes, and {int(seconds)} seconds before running this command again.",
          color = discord.Color.red()
        )
        embed.set_footer(text = f"{ctx.author.name}" , icon_url = ctx.author.avatar.url)
        await ctx.reply(embed = embed)

    @commands.hybrid_command(name="slots", description="Play slots!")
    @app_commands.describe(
      amount = "The amount you want to bet."
    )
    async def slots(self, ctx: commands.Context, amount: int = None) -> None:
      with open(f"json/bank.json", "r") as f:
        bank = json.load(f)
      slot_emotes = ["🍍", "💸", "💰", "🧽", "🍬"]
      choice1 = random.choice(slot_emotes)
      choice2 = random.choice(slot_emotes)
      choice3 = random.choice(slot_emotes)
      choice4 = random.choice(slot_emotes)
      choice5 = random.choice(slot_emotes)
      choice6 = random.choice(slot_emotes)
      choice7 = random.choice(slot_emotes)
      choice8 = random.choice(slot_emotes)
      choice9 = random.choice(slot_emotes)
      if amount == None:
        error = discord.Embed(
          title = "Error",
          description = "You need to specify an amount to bet!",
          color = discord.Color.red()
        )
        error.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar.url)
        await ctx.reply(embed = error)
      else:
        if not f"{ctx.author.id}" in bank:
          await ctx.send("You do not have an account! Create one with `.open_account`!")
          await ctx.send("You do not have an account!")
        else:
          if amount > bank[str(ctx.author.id)]["wallet"]:
            error = discord.Embed(
              title = "Error",
              description = "You do not have enough money in your wallet to bet that much!",
              color = discord.Color.red()
            )
            error.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar.url)
            await ctx.reply(embed = error)
          else:
            await ctx.send("Spinning...")
            slots = discord.Embed(
              title = "Slot Machine",
              description = "Spinning...",
              color = discord.Color.blurple()
            )
            slots.add_field(name = "\n\u200b", value = choice1, inline = True)
            slots.add_field(name = "\n\u200b", value = choice2, inline = True)
            slots.add_field(name = "\n\u200b", value = choice3, inline = True)
            slots.add_field(name = "\n\u200b", value = choice4, inline = True)
            slots.add_field(name = "\n\u200b", value = choice5, inline = True)
            slots.add_field(name = "\n\u200b", value = choice6, inline = True)
            slots.add_field(name = "\n\u200b", value = choice7, inline = True)
            slots.add_field(name = "\n\u200b", value = choice8, inline = True)
            slots.add_field(name = "\n\u200b", value = choice9, inline = True)
            slots.set_thumbnail(url = "https://media.istockphoto.com/id/843640814/vector/red-slot-machine-wins-the-jackpot-isolated-on-white-background-casino-big-win-slot-machine.jpg?s=612x612&w=0&k=20&c=9rYfl-R8ATGjXdC1UwcLBzvHZqyYK3OHMcjMBxEv0Bc=")
            slots.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.display_avatar.url)
            msg = await ctx.reply(embed = slots)
            await asyncio.sleep(1.5)
            if choice1 == choice2 == choice3 or choice4 == choice5 == choice6 or choice7 == choice8 == choice9 or choice1 == choice5 == choice9 or choice3 == choice5 == choice7 or choice1 == choice4 == choice7 or choice2 == choice5 == choice8 or choice3 == choice6 == choice9:
              slots2 = discord.Embed(  
                title = "Slot Machine",
                description = "You won ${:,}!".format(int(amount)),
                color = discord.Color.green()
              )
              slots2.add_field(name = "\n\u200b", value = choice1, inline = True)
              slots2.add_field(name = "\n\u200b", value = choice2, inline = True)
              slots2.add_field(name = "\n\u200b", value = choice3, inline = True)
              slots2.add_field(name = "\n\u200b", value = choice4, inline = True)
              slots2.add_field(name = "\n\u200b", value = choice5, inline = True)
              slots2.add_field(name = "\n\u200b", value = choice6, inline = True)
              slots2.add_field(name = "\n\u200b", value = choice7, inline = True)
              slots2.add_field(name = "\n\u200b", value = choice8, inline = True)
              slots2.add_field(name = "\n\u200b", value = choice9, inline = True)
              slots2.set_thumbnail(url = "https://media.istockphoto.com/id/843640814/vector/red-slot-machine-wins-the-jackpot-isolated-on-white-background-casino-big-win-slot-machine.jpg?s=612x612&w=0&k=20&c=9rYfl-R8ATGjXdC1UwcLBzvHZqyYK3OHMcjMBxEv0Bc=")
              slots2.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.display_avatar.url)
              await msg.edit(embed = slots2)
              bank[str(ctx.author.id)]["wallet"] += amount
              with open(f"json/bank.json", "w") as f:
                json.dump(bank, f)
            else:
              slots3 = discord.Embed(
                title = "Slot Machine",
                description = "You lost ${:,}.".format(int(amount)),
                color = discord.Color.red()
              )
              slots3.add_field(name = "\n\u200b", value = choice1, inline = True)
              slots3.add_field(name = "\n\u200b", value = choice2, inline = True)
              slots3.add_field(name = "\n\u200b", value = choice3, inline = True)
              slots3.add_field(name = "\n\u200b", value = choice4, inline = True)
              slots3.add_field(name = "\n\u200b", value = choice5, inline = True)
              slots3.add_field(name = "\n\u200b", value = choice6, inline = True)
              slots3.add_field(name = "\n\u200b", value = choice7, inline = True)
              slots3.add_field(name = "\n\u200b", value = choice8, inline = True)
              slots3.add_field(name = "\n\u200b", value = choice9, inline = True)
              slots3.set_thumbnail(url = "https://media.istockphoto.com/id/843640814/vector/red-slot-machine-wins-the-jackpot-isolated-on-white-background-casino-big-win-slot-machine.jpg?s=612x612&w=0&k=20&c=9rYfl-R8ATGjXdC1UwcLBzvHZqyYK3OHMcjMBxEv0Bc=")
            slots3.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.display_avatar.url)
            await msg.edit(embed = slots3)
            bank[str(ctx.author.id)]["wallet"] -= amount
            with open(f"json/bank.json", "w") as f:
              json.dump(bank, f)

    @commands.hybrid_command(name="roulette", description="Play a game of roulette!")
    @app_commands.describe(
      color="The color of the roulette wheel to bet on",
      amount="The amount of money to bet",
    )
    async def roulette(self, ctx: commands.Context, color: Literal["red","black"], amount = None) -> None:
      winning_color = random.choice(["🟥", "⬛️"])
      winning_color_text = "none"
      if winning_color == "🟥":
        winning_color_text = "red"
      elif winning_color == "⬛️":
        winning_color_text = "black"
      with open(f"json/bank.json", "r") as f:
        bank = json.load(f)
      if color == None:
        error = discord.Embed(
          title = "Error",
          description = "You need to specify a color!",
          color = discord.Color.red()
        )
        error.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.display_avatar.url)
        await ctx.reply(embed = error)
      elif amount == None:
        error = discord.Embed(
          title = "Error",
          description = "You need to specify an amount!",
          color = discord.Color.red()
        )
        error.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.display_avatar.url)
        await ctx.reply(embed = error)
      elif int(amount) > int(bank[str(ctx.author.id)]["wallet"]):
        error = discord.Embed(
          title = "Error",
          description = "You don't have enough money!",
          color = discord.Color.red()
        )
        error.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.display_avatar.url)
        await ctx.reply(embed = error)
      else:
        random_color_1 = random.choice(["🟥", "⬛️"])
        random_color_2 = random.choice(["🟥", "⬛️"])
        random_color_3 = random.choice(["🟥", "⬛️"])
        random_color_4 = random.choice(["🟥", "⬛️"])
        random_color_5 = random.choice(["🟥", "⬛️"])
        roulette = discord.Embed(
          title = "Roulette",
          description = random_color_1 + random_color_2 + random_color_3,
          color = discord.Color.blurple()
        )
        msg = await ctx.reply(embed = roulette)
        await asyncio.sleep(1)
        roulette2 = discord.Embed(
          title = "Roulette",
          description = random_color_2 + random_color_3 + random_color_4,
          color = discord.Color.blurple()
        )

        await msg.edit(embed = roulette2)
        await asyncio.sleep(1)
        roulette3 = discord.Embed(
          title = "Roulette",
          description = random_color_3 + random_color_4 + winning_color,
          color = discord.Color.blurple()
        )
        await msg.edit(embed = roulette3)
        await asyncio.sleep(1)
        roulette4 = discord.Embed(
          title = "Roulette",
          description = random_color_4 + winning_color + random_color_5,
          color = discord.Color.blurple()
        )
        await msg.edit(embed = roulette4)
        await asyncio.sleep(1)
        if winning_color_text == color:
          roulettewin = discord.Embed(
            title = "Roulette",
            description = random_color_4 + winning_color + random_color_5,
            color = discord.Color.green()
          )
          roulettewin.set_footer(text = "You won ${:,}!".format(int(amount)))
          bank[str(ctx.author.id)]["wallet"] += int(amount)
          with open(f"json/bank.json", "w") as f:
            json.dump(bank, f)
          await msg.edit(embed = roulettewin)
        else:
          roulettelose = discord.Embed(
            title = "Roulette",
            description = random_color_4 + winning_color + random_color_5,
            color = discord.Color.red()
          )
          roulettelose.set_footer(text = "You lost ${:,}.".format(int(amount)))
          bank[str(ctx.author.id)]["wallet"] -= int(amount)
          await msg.edit(embed = roulettelose)
          with open(f"json/bank.json", "w") as f:
            json.dump(bank, f)

    @commands.hybrid_command(name="store", description="Buy from the server store!",aliases = ["shop"])
    async def store(self, ctx: commands.Context) -> None:
      with open(f"dictionaries/inventory_display.json", "r") as f:
        display = json.load(f)
      shop = discord.Embed(
        title = "Server Store",
        description = "Welcome to the server store!",
        color = discord.Color.blurple()
        )
      for key, value in display.items():
        shop.add_field(name = key, value = value, inline = False)
      shop.set_thumbnail(url = "https://i.imgur.com/LIKZo8O.png")
      user = ctx.author
      shop.set_footer(text = f"{ctx.author.name}" + " | Page 1/1", icon_url = user.display_avatar.url)
      await ctx.reply(embed = shop)

    @commands.hybrid_command(name="buy", description="Buy from the server store!")
    async def buy(self, ctx: commands.Context, item: Literal["Business Down Payment","Empty Storefront","News Station", "Small Apartment", "Law School Tuition"], amount: int = 1) -> None:
      with open(f"json/bank.json", "r") as f:
        bank = json.load(f)
      with open(f"json/inventory.json", "r") as f:
        inventory = json.load(f)
      with open(f"json/store.json", "r") as f:
        store = json.load(f)

      for key, value in store.items():
        if item.lower() == key:
          if bank[str(ctx.author.id)]["wallet"] < int(value) * amount:
            await ctx.reply(f"You don't have enough money to buy {amount} {item}.")
          else:
            bank[str(ctx.author.id)]["wallet"] -= int(value) * amount
            item_parsed = item.lower().replace(" ", "_")
            inventory[str(ctx.author.id)][f"{item_parsed}"] += amount
            await ctx.reply(f"You bought {amount} {item}(s).")

      with open(f"json/bank.json", "w") as f:
        json.dump(bank, f)
      with open(f"json/inventory.json", "w") as f:
        json.dump(inventory, f)

    @commands.hybrid_command(name = "inventory", description = "Access your inventory!", aliases = ["inv"])
    @app_commands.describe(
      user = "The user you want to view the inventory of."
    )
    async def inventory(self, ctx: commands.Context, user : discord.Member = None) -> None:
      with open(f"json/inventory.json", "r") as f:
        inventory = json.load(f)
      if user == None:
        user = ctx.author
      apt_inv = int(inventory[str(user.id)]["small_apartment"])
      news_inv = int(inventory[str(user.id)]["news_station"])
      emp_inv = int(inventory[str(user.id)]["empty_storefront"])
      bus_inv = int(inventory[str(user.id)]["business_down_payment"])
      tuition_inv = int(inventory[str(user.id)]["law_tuition"])

      inv = discord.Embed(
        title = "Inventory",
        description = f"{user.name}'s inventory",
        color = discord.Color.blue()
      )
      if apt_inv > 0:
        inv.add_field(name = "Small Apartment Lease (x" + str(apt_inv) + ")", value = "Each lease lets you live in an apartment for two irl weeks!", inline = False)    

      if news_inv > 0:
        inv.add_field(name = "News Studio (x" + str(news_inv) + ")", value = "Each lease lets you operate a news station for two irl weeks!", inline = False)   

      if emp_inv > 0:
        inv.add_field(name = "Empty Storefront (x" + str(emp_inv) + ")", value = "Each lease lets you operate an empty storefront for two irl weeks!", inline = False)  

      if bus_inv > 0:
        inv.add_field(name = "Business Down Payment (x" + str(bus_inv) + ")", value = "Down payment that is redeemable for a business, if you have all the other necessities!", inline = False)

      if tuition_inv > 0:
        inv.add_field(name = "Law School Tuition (x" + str(tuition_inv) + ")", value = "Tuition used to attend law school, and eventually get a law degree!", inline = False)

      inv.set_thumbnail(url = "https://i.imgur.com/tAjhb3X.png")
      inv.set_footer(text = f"{user.name} | Page 1/1", icon_url = user.display_avatar.url)      
      await ctx.reply(embed = inv)

    @inventory.error
    async def inventory_error(self, ctx, error):
      if isinstance(error, commands.KeyError):
        await ctx.reply("Specified User hasn't set up their inventory yet! They can do so by using `.open_account`!")

    @commands.hybrid_command(name = "use", description = "Use an item from your inventory!", aliases = ["use_item"])
    @app_commands.describe(
      item = "The item you want to use",
      amount = "The amount of the item you want to use",
    )
    async def use(self, ctx: commands.Context, item: Literal["Business Down Payment","Empty Storefront", "News Station", "Small Apartment", "Law School Tuition"], amount: int = 1) -> None:
      with open(f"json/inventory.json", "r") as f:
        inventory = json.load(f)
      for key, value in inventory.items():
          item_parsed = item.lower().replace(" ", "_")
          if inventory[str(ctx.author.id)][f"{item_parsed}"] < amount:
            await ctx.reply("You don't have enough of this item!")
          else:
            inventory[str(ctx.author.id)][f"{item_parsed}"] -= amount
            await ctx.reply(f"You used {amount} {item}!")
            with open(f"json/inventory.json", "w") as f:
              json.dump(inventory, f)

    @use.error
    async def use_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("You need to specify which item to use!")

    @commands.hybrid_command(name = "pay", description = "Pay someone money!")
    @app_commands.describe(
      user = "The user you want to pay",
      amount = "The amount of money you want to pay"
    )
    async def pay(self, ctx: commands.Context, user : discord.Member, amount: int) -> None:
      if user == ctx.author:
        await ctx.reply("You can't pay yourself!")
      elif user.bot:
        await ctx.reply("You can't pay bots!")
      else:
        with open(f"json/bank.json", "r") as f:
          bank = json.load(f)
        if bank[str(ctx.author.id)]["wallet"] >= amount:
          bank[str(ctx.author.id)]["wallet"] -= int(amount)
          bank[str(user.id)]["wallet"] += int(amount)
          with open(f"json/bank.json", "w") as f:
            json.dump(bank, f)
          await ctx.reply(f"You paid {user.mention} " + "${:,}!".format(int(amount)))
        elif bank[str(ctx.author.id)]["wallet"] < amount:
          await ctx.reply("You don't have enough money in your wallet to pay that user!")

    @commands.hybrid_command(name = "gift", description = "Gift someone an item!")
    @app_commands.describe(
      user = "The user you want to gift the item to",
      item = "The item you want to gift",
      amount = "The amount of the item you want to gift"
    )
    async def gift(self, ctx: commands.Context, user : discord.Member = None, item = None, amount: int = 1) -> None:
      if user == ctx.author:
        await ctx.reply("You can't gift yourself!")
      elif item == None:
        await ctx.reply("You need to specify an item to gift!")
      elif user == None:
        await ctx.reply("You need to specify a user to gift something to!")
      else:
        with open(f"json/inventory.json", "r") as f:
          inventory = json.load(f)
        if inventory[str(ctx.author.id)]["small_apartment"] >= amount:
          inventory[str(ctx.author.id)]["small_apartment"] -= int(amount)
          inventory[str(user.id)]["small_apartment"] += int(amount)
          with open(f"json/inventory.json", "w") as f:
            inventory = json.dump(inventory, f)
          await ctx.reply(f"You gifted {user.mention} {amount} small apartment leases!")
        elif inventory[str(ctx.author.id)]["small_apartment"] < amount:
          await ctx.reply("You don't have enough small apartment leases!")

    @commands.hybrid_command(name = "salary", description = "Get information about your salary!")
    async def salary(self, ctx: commands.Context) -> None:
      Rep = discord.utils.get(ctx.guild.roles, name="Representative")
      Sen = discord.utils.get(ctx.guild.roles, name="Senator")
      Pres = discord.utils.get(ctx.guild.roles, name="President")
      VP = discord.utils.get(ctx.guild.roles, name="Vice President")
      Gov = discord.utils.get(ctx.guild.roles, name="Governor")
      salaryview = discord.Embed(
        title = "Salary View",
        description = f"{ctx.author.name}'s Salary",
        color = discord.Color.green()
      )
      salaryview.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRWbQEuDAu9kTn--3IRg-Urne7t93iPGuP2UedRmMcQKa_l8MOk2toXOP19eu2y_85ysSk&usqp=CAU")
      salaryview.set_footer(text = f"{ctx.author.name}")
      user = ctx.author
      if not Rep in user.roles and not Sen in user.roles and not Pres in user.roles and not VP in user.roles and not Gov in user.roles:
        if not Rep in user.roles and not Sen in user.roles and not Pres in user.roles and not VP in user.roles:
          salaryview.add_field(
            name = "Salary",
            value = "You do not have a job!",
        )
        await ctx.reply(embed = salaryview)
      elif Rep in user.roles:
        salaryview.add_field(
          name = "Salary", 
          value = "$178,000/year",
          inline = False
        )
        await ctx.reply(embed = salaryview)
      elif Sen in user.roles:
        salaryview.add_field(
          name = "Salary",
          value = "$178,000/year",
          inline = False
        )
        await ctx.reply(embed = salaryview)
      elif Gov in user.roles:
        salaryview.add_field(
          name = "Salary",
          value = "$147,000/year",
          inline = False
        )
        await ctx.reply(embed = salaryview)
      elif Pres in user.roles:
        salaryview.add_field(
          name = "Salary",
          value = "$400,000/year",
          inline = False
        )
        await ctx.reply(embed = salaryview)
      elif VP in user.roles:
        salaryview.add_field(
          name = "Salary",
          value = "$230,700/year",
          inline = False
        )
        await ctx.reply(embed = salaryview)

    @commands.hybrid_command(name = "collect", description = "Collect your salary!")
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def collect(self, ctx: commands.Context) -> None:
      with open(f"json/bank.json", "r") as f:
        bank = json.load(f)
      Rep = discord.utils.get(ctx.guild.roles, name="Representative")
      Sen = discord.utils.get(ctx.guild.roles, name="Senator")
      Pres = discord.utils.get(ctx.guild.roles, name="President")
      VP = discord.utils.get(ctx.guild.roles, name="Vice President")
      Gov = discord.utils.get(ctx.guild.roles, name="Governor")
      LtGov = discord.utils.get(ctx.guild.roles, name="Lt. Governor")
      if not Rep in ctx.author.roles and not Sen in ctx.author.roles and not Pres in ctx.author.roles and not VP in ctx.author.roles and not Gov in ctx.author.roles and not LtGov in ctx.author.roles:
        if not Rep in ctx.author.roles and not Sen in ctx.author.roles and not Pres in ctx.author.roles and not VP in ctx.author.roles:
          collectview = discord.Embed(
            title = "Income Could Not Be Collected!",
            description = f"You do not have a job, and your income could therefore not be collected!",
            color = discord.Color.red()
          )
          collectview.set_thumbnail(url = "https://as2.ftcdn.net/v2/jpg/00/02/91/03/1000_F_2910336_yP4opz0fBKz9XpL0WgqMeBL8WJpUIJ.jpg")
          collectview.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
          await ctx.reply(embed = collectview)
      elif LtGov in ctx.author.roles:
        collectview = discord.Embed(
          title = "Income Collected!",
          description = "You have collected $7,142! Good job, Lt. Governor!",
          color = discord.Color.green()
        )
        collectview.set_footer(text = f"{ctx.author.name}")
        bank[str(ctx.author.id)]["wallet"] += 7142
        with open(f"json/bank.json", "w") as f:
          json.dump(bank, f)
        await ctx.reply(embed = collectview)
      elif Rep in ctx.author.roles:
        collectview = discord.Embed(
        title = "Income Collected!",
        description = f"You have collected $12,714! Great job, Representative!",
        color = discord.Color.green()
      )
        collectview.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Seal_of_the_United_States_House_of_Representatives.svg/1030px-Seal_of_the_United_States_House_of_Representatives.svg.png")
        collectview.set_footer(text = f"{ctx.author.name}")
        bank[f"{ctx.author.id}"]["wallet"] += 12714
        with open(f"json/bank.json", "w") as f:
          json.dump(bank, f)
        await ctx.reply(embed = collectview)
      elif Gov in ctx.author.roles:
        collectview = discord.Embed(
        title = "Income Collected!",
        description = f"You have collected $10,500! Great job, Governor!",
        color = discord.Color.green()
        )
        collectview.set_thumbnail(url = "https://www.transportation.gov/sites/dot.gov/files/NGA_Logo_CMYK_0.JPG")
        collectview.set_footer(text = f"{ctx.author.name}")
        bank[f"{ctx.author.id}"]["wallet"] += 10500
        with open(f"json/bank.json", "w") as f:
          json.dump(bank, f)
        await ctx.reply(embed = collectview)
      elif Sen in ctx.author.roles:
        collectview = discord.Embed(
        title = "Income Collected!",
        description = f"You have collected $12,714! Great job, Senator!",
        color = discord.Color.green()
      )
        collectview.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Seal_of_the_United_States_Senate.svg/1200px-Seal_of_the_United_States_Senate.svg.png")
        collectview.set_footer(text = f"{ctx.author.name}")
        bank[f"{ctx.author.id}"]["wallet"] += 12714
        with open(f"json/bank.json", "w") as f:
          json.dump(bank, f)
        await ctx.reply(embed = collectview)
      elif VP in ctx.author.roles:
        collectview = discord.Embed(
        title = "Income Collected!",
        description = f"You have collected $17,478! Great job, Vice President!",
        color = discord.Color.green()
      )
        collectview.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Seal_of_the_Vice_President_of_the_United_States.svg/200px-Seal_of_the_Vice_President_of_the_United_States.svg.png")
        collectview.set_footer(text = f"{ctx.author.name}")
        bank[f"{ctx.author.id}"]["wallet"] += 17478
        with open(f"json/bank.json", "w") as f:
          json.dump(bank, f)
        await ctx.reply(embed = collectview)
      elif Pres in ctx.author.roles:
        collectview = discord.Embed(
        title = "Income Collected!",
        description = f"You have collected $28,571! Great job, President!",
        color = discord.Color.green()
      )
        collectview.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Seal_of_the_President_of_the_United_States.svg/2424px-Seal_of_the_President_of_the_United_States.svg.png")
        collectview.set_footer(text = f"{ctx.author.name}")
        bank[f"{ctx.author.id}"]["wallet"] += 28571
        with open(f"json/bank.json", "w") as f:
          json.dump(bank, f)
        await ctx.reply(embed = collectview)

    @collect.error
    async def collect_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        minutes, seconds = divmod(error.retry_after, 60)
        hours, minutes = divmod(minutes, 60)
        embed = discord.Embed(
          title = "You're on cooldown!",
          description = f"Please wait {int(hours)} hours, {int(minutes)} minutes, and {int(seconds)} seconds before running this command again.",
          color = discord.Color.red()
        )
        embed.set_footer(text = f"{ctx.author.name}" , icon_url = ctx.author.avatar.url)
        await ctx.reply(embed = embed)

    @commands.hybrid_command(name="clean_economy", description="Removes the people who are no longer in the server from the economy module.")
    @commands.has_role("*")
    async def clean_economy(self, ctx: commands.Context) -> None:
      with open("json/bank.json", "r") as f:
        bank = json.load(f)
      await ctx.send("Are you SURE?")
      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
      msg = await self.client.wait_for("message", check=check, timeout=60.0)
      if msg.content.lower() == "yes":
        await ctx.send("Cleaning economy...")
        await asyncio.sleep(2.0)
        users_to_remove = [user_id for user_id, user_data in bank.items() if int(user_id) not in [member.id for member in ctx.guild.members]]
        ###
        for user_id in users_to_remove:
          del bank[user_id]
        ###
        with open("json/bank.json", "w") as f:
          json.dump(bank, f)
        await ctx.send("Done!")
      else:
        await ctx.send("Cancelled!")

    @commands.hybrid_command(name = "update_shop", description = "An administrative command used to update everyone's inventories when the shop is updated!")
    @commands.has_role("*")
    async def update_shop(self, ctx: commands.Context) -> None:
      with open("json/inventory.json", "r") as f:
        inventory = json.load(f)
      for user_id, user_data in inventory.items():
        if user_id in inventory:
          inventory[user_id]["law_tuition"] = 0
          with open("json/inventory.json", "w") as f:
            json.dump(inventory, f)
          await ctx.send("Done!")



async def setup(bot):
    await bot.add_cog(economy(bot))
    print("My economy extension has been loaded")  # Print a message after loading the extension
    return True  # Return a value to indicate that the setup was successful