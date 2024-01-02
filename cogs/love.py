import discord
from discord.ext import commands
import asyncio
import json

class Love(commands.Cog):
    def __init__(self, client):
        self.client = client
      
    rrmatrix = [f"'The body cannot live without the mind.' -Morpheus, The Matrix" , f"'Ever have that feeling where you’re not sure if you’re awake or dreaming?'' -Neo, The Matrix" , f"'I don’t like the idea that I’m not in control of my life.'' -Neo, The Matrix" , f"'Never tell me the odds!' - Han Solo, Star Wars", f"'It's time to spin the chamber, Boris.' -DeAngelo, The Office (US)", f"'Do not throw away your shot...' -Alexander Hamilton, Hamilton" , f"'Guns. Lots of guns.' -Neo, The Matrix"]
  

    @commands.hybrid_command(name = "propose", description = "Propose to someone") 
    async def propose(self, ctx: commands.Context, member : discord.Member) -> None:
      if member.bot:
        await ctx.send("You can't propose to a bot!")
      elif member.id == ctx.author.id:
        await ctx.send("You can't propose to yourself! That's just pathetic.")
      else:
        await ctx.send(f"{ctx.author.mention} has proposed to {member.mention}. Type `yes` or `no` to accept or decline the proposal." + "\n\u200b" + "https://media.tenor.com/p_VjOui06o4AAAAM/sole-proposal.gif")
        def check(message):
          return message.author == member and message.channel == ctx.channel
        msg = await client.wait_for('message', timeout=30.0, check=check)
        if msg.content.lower() == "yes":
          await ctx.send(f"{member.mention} has accepted the proposal from {ctx.author.mention}. They are now engaged!" + "\n\u200b" + "https://media3.giphy.com/media/l1J9yTco40EU5JzTW/giphy.gif?cid=6c09b952l6lp90s60owsv428kkljleksr4puxuylxe6bekwi&ep=v1_internal_gif_by_id&rid=giphy.gif&ct=g")
          user = ctx.author
          with open(".gitignore/engaged.json", "r") as f:
            engaged = json.load(f)
            if not f"{user.id}" in engaged:
              engaged[f"{user.id}"] = {}
              engaged[f"{user.id}"]["partner"] = member.id
            if not f"{member.id}" in engaged:
              engaged[f"{member.id}"] = {}
              engaged[f"{member.id}"]["partner"] = user.id
            with open(".gitignore/engaged.json", "w") as f:
              engaged = json.dump(engaged, f)
        elif msg.content.lower() == "no":
          await ctx.send(f"{member.mention} has declined the proposal from {ctx.author.mention}." + "\n\u200b")
          await member.send(f"{ctx.author.mention} has declined your proposal.")
          await ctx.send(f"{ctx.author.mention} has declined the proposal from {member.mention}." + "\n\u200b" + "https://media1.giphy.com/media/TY3bikeN6R4DS2wpcN/giphy.gif")

    @commands.hybrid_command(name = "date", description = "Ask someone to start dating you", aliases = ["ask_out"])
    async def date(self, ctx: commands.Context, member : discord.Member) -> None:
      if member.bot:
        await ctx.send("You can't ask out a bot!")
      elif member.id == ctx.author.id:
        await ctx.send("You can't ask out yourself! That's just pathetic.")
      else:
        await ctx.send(f"{ctx.author.mention} has asked out {member.mention}. Type `yes` or `no` to accept or decline.")
        def check(message):
          return message.author == member and message.channel == ctx.channel
        msg = await self.client.wait_for('message', timeout=30.0, check=check)
        if msg.content.lower() == "yes":
          await ctx.send(f"{member.mention} has accepted the date from {ctx.author.mention}. They are now dating!") 
          user = ctx.author
          with open(".gitignore/dating.json", "r") as f:
            dating = json.load(f)
            if not f"{user.id}" in dating:
              dating[f"{user.id}"] = {}
              dating[f"{user.id}"]["partner"] = member.id
            if not f"{member.id}" in dating:
              dating[f"{member.id}"] = {}
              dating[f"{member.id}"]["partner"] = user.id
            with open(".gitignore/dating.json", "w") as f:
              dating = json.dump(dating, f)
              await member.send(f"{ctx.author.mention} has accepted your date request.")
        elif msg.content.lower() == "no":
          await ctx.send(f"{member.mention} has declined the date request from {ctx.author.mention}.")
          await member.send(f"{ctx.author.mention} has declined your date request.")
          await ctx.send(f"{ctx.author.mention} has declined the date request from {member.mention}.")

    @date.error
    async def date_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
          title = "Error!",
          description = "You need to mention a member to ask out.",
          color = discord.Color.red()
        )
        embed.set_footer(text = "This message will self-destruct in 5 seconds.")
        await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=2)

    @commands.hybrid_command(name = "marriage_law", description = "Set the law for marriage in a certain state")
    @commands.has_any_role("Administrator","Server Co-Owner", "Server Owner")
    async def marriage_law(self, ctx: commands.Context, state = None, status = None) -> None:
      if state == None:
        embed = discord.Embed(
        title = "Error!",
        description = "You need to specify a state.",
        color = discord.Color.red()
      )
        embed.set_footer(text = "This message will self-destruct in 5 seconds.")
        await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=2)
      elif status == None:
        embed = discord.Embed(
          title = "Error!",
          description = "You need to specify a status.",
          color = discord.Color.red()
        )
        embed.set_footer(text = "This message will self-destruct in 5 seconds.")
        await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=2)
      else:
        with open(".gitignore/marriage.json", "r") as f:
          marriage_laws = json.load(f)
        marriage_laws[state] = {
          "status": status
        }
        with open(".gitignore/marriage.json", "w") as f:
          json.dump(marriage_laws, f, indent=4)
    
        await ctx.send(f"The marriage laws for {state} have been updated.")

    @commands.hybrid_command(name="marry", description = "Marry two users together")
    @commands.has_role("Priest")
    async def marry(self, ctx: commands.Context, member : discord.Member, user : discord.Member) -> None:
      with open(".gitignore/married.json", "r") as f:
        married = json.load(f)
      with open(".gitignore/gender.json", "r") as f:
        gender = json.load(f)
      with open(".gitignore/marriage.json", "r") as f:
        law = json.load(f)
      if member.bot or user.bot:
        await ctx.send("You can't marry a bot!")
      elif member.id == user.id:
        await ctx.send("You can't marry the same person to themselves! That's pathetic and weird.")
      elif f"{member.id}" in married:
        await ctx.send(f"{member.mention} is already married.")
      elif f"{user.id}" in married:
        await ctx.send(f"{user.mention} is already married.")
      elif not f"{member.id}" in gender:
        await ctx.send(f"{member.mention} needs to set their gender to marry!")
      elif not f"{user.id}" in gender:
        await ctx.send(f"{user.mention} needs to set their gender to marry!")
      elif member.id == ctx.author.id:
        await ctx.send("You can't officiate your own wedding, silly!")
      elif user.id == ctx.author.id:
        await ctx.send("You can't officiate your own wedding, silly!")
      elif gender[f"{member.id}"] == gender[f"{user.id}"]:
        if any(role.name == 'Southern Union' or "Sunbelt" or "Bible Belt" for role in member.roles):
          if f"{member.id}" in gender:
            if gender[f"{member.id}"] == gender[f"{user.id}"]:
              if law["South"]["status"] == "1":
                await ctx.send("Sorry, but gay marriage is not legal in your region.")
              elif law["South"]["status"] == "2" or "3":
                await ctx.send(f"{member.mention}, do you take {user.mention} as your lawfully wedded spouse?")
                def check(message):
                  return message.author == member and message.channel == ctx.channel
                msg = await client.wait_for('message', timeout=60.0, check=check)
                if msg.content.lower() == "yes":
                  await ctx.send(f"And {user.mention}, do you take {member.mention} as your lawfully wedded spouse?")
                def check(message):
                  return message.author == user and message.channel == ctx.channel
                msg = await client.wait_for('message', timeout=60.0, check=check)
                if msg.content.lower() == "yes":
                  await ctx.send(f"{member.mention} and {user.mention} have married!")
                  if not f"{user.id}" in married:
                    married[f"{user.id}"] = {}
                    married[f"{user.id}"]["partner"] = member.id
                  if not f"{member.id}" in married:
                    married[f"{member.id}"] = {}
                    married[f"{member.id}"]["partner"] = user.id
                  with open(".gitignore/married.json", "w") as f:
                    married = json.dump(married, f)
                  await ctx.send(f"{member.mention} and {user.mention} have married!")
                elif msg.content.lower() == "no":
                  await ctx.send("You have declined the marriage.")
                elif asyncio.TimeoutError:
                  await ctx.send("Someone didn't show up to the altar! Try again later.")
        elif any(role.name == 'New England' or "Mid-Atlantic" or "Midwest" for role in member.roles):
          if f"{member.id}" in gender:
            if gender[f"{member.id}"] == gender[f"{user.id}"]:
              if law["East"]["status"] == "1":
                await ctx.send("Sorry, but gay marriage is not legal in your region.")
              elif law["East"]["status"] == "2" or "3":
                await ctx.send(f"{member.mention}, do you take {user.mention} as your lawfully wedded spouse?")
                def check(message):
                  return message.author == member and message.channel == ctx.channel
                msg = await client.wait_for('message', timeout=60.0, check=check)
                if msg.content.lower() == "yes":
                  await ctx.send(f"And {user.mention}, do you take {member.mention} as your lawfully wedded spouse?")
                def check(message):
                  return message.author == user and message.channel == ctx.channel
                msg = await client.wait_for('message', timeout=60.0, check=check)
                if msg.content.lower() == "yes":
                  await ctx.send(f"{member.mention} and {user.mention} have married!")
                  if not f"{user.id}" in married:
                    married[f"{user.id}"] = {}
                    married[f"{user.id}"]["partner"] = member.id
                  if not f"{member.id}" in married:
                    married[f"{member.id}"] = {}
                    married[f"{member.id}"]["partner"] = user.id
                  with open(".gitignore/married.json", "w") as f:
                    married = json.dump(married, f)
                  await ctx.send(f"{member.mention} and {user.mention} have married!")
                elif msg.content.lower() == "no":
                  await ctx.send("You have declined the marriage.")
                elif asyncio.TimeoutError:
                  await ctx.send("Someone didn't show up to the altar! Try again later.")
        elif any(role.name == 'Four Corners' or "Great Plains" or "Cascadia" or "West Coast" or "Pacific Territories" for role in member.roles):
          if f"{member.id}" in gender:
            if gender[f"{member.id}"] == gender[f"{user.id}"]:
              if law["West"]["status"] == "1":
                await ctx.send("Sorry, but gay marriage is not legal in your region.")
              elif law["West"]["status"] == "2" or "3":
                await ctx.send(f"{member.mention}, do you take {user.mention} as your lawfully wedded spouse?")
                def check(message):
                  return message.author == member and message.channel == ctx.channel
                msg = await client.wait_for('message', timeout=60.0, check=check)
                if msg.content.lower() == "yes":
                  await ctx.send(f"And {user.mention}, do you take {member.mention} as your lawfully wedded spouse?")
                def check(message):
                  return message.author == user and message.channel == ctx.channel
                msg = await client.wait_for('message', timeout=60.0, check=check)
                if msg.content.lower() == "yes":
                  await ctx.send(f"{member.mention} and {user.mention} have married!")
                  if not f"{user.id}" in married:
                    married[f"{user.id}"] = {}
                    married[f"{user.id}"]["partner"] = member.id
                  if not f"{member.id}" in married:
                    married[f"{member.id}"] = {}
                    married[f"{member.id}"]["partner"] = user.id
                  with open(".gitignore/married.json", "w") as f:
                    married = json.dump(married, f)
                  await ctx.send(f"{member.mention} and {user.mention} have married!")
                elif msg.content.lower() == "no":
                  await ctx.send("You have declined the marriage.")
                elif asyncio.TimeoutError:
                  await ctx.send("Someone didn't show up to the altar! Try again later.")

    @marry.error
    async def marry_error(ctx, error):
      if isinstance(error, commands.MissingRole):
        await ctx.send("You do not have the Priest role.")

    @commands.hybrid_command(name = "gender", description = "Set or view your gender")
    async def gender(self, ctx: commands.Context, *, criterion = None) -> None:
      with open('.gitignore/gender.json', 'r') as f:
        gender = json.load(f)
      if criterion == None:
        if not f'{ctx.author.id}' in gender:
          await ctx.send("You haven't set your gender yet. Set it with `.gender [gender]`.")
        else:
          gender_embed = discord.Embed(
            title = f"{ctx.author.name}'s Gender",
            description = f"{ctx.author.name}'s gender is {gender[f'{ctx.author.id}']['gender']}.",
            color = discord.Color.green()
          )
          await ctx.send(embed = gender_embed)
      elif criterion != None:
        if not f'{ctx.author.id}' in gender:
          if criterion.lower() == "male" or criterion.lower() == "female" or criterion.lower() == "Non-binary":
            gender[f'{ctx.author.id}'] = {}
            gender[f'{ctx.author.id}']['gender'] = str(criterion)
            embed_success = discord.Embed(
              title = "Success!",
              description = f"Your gender has been set to {criterion}.",
              color = discord.Color.green()
            )
            await ctx.reply(embed = embed_success)
          elif criterion.lower() != "male" or criterion.lower() != "female" or criterion.lower() != "Non-binary":
            await ctx.send("Sorry, right now only Male, Female, and Non-Binary are recognized by the bot. Please reach out to an admin to get your preferred gender added!")
        elif f'{ctx.author.id}' in gender:
          await ctx.send("Your gender is already set! To change it, please contact server staff.")
        with open('.gitignore/gender.json', 'w') as f:
          gender = json.dump(gender, f)

    @commands.hybrid_command(name = "partner", description = "View your partnership status")
    async def partner(self, ctx: commands.Context) -> None:
      with open(".gitignore/engaged.json", "r") as f:
        engaged = json.load(f)
      with open(".gitignore/dating.json", "r") as f:
        dating = json.load(f)
      with open(".gitignore/married.json", "r") as f:
        married = json.load(f)
      user = ctx.author
      engaged_text = engaged.get(f"{user.id}", {}).get("partner")  
      dating_text = dating.get(f"{user.id}", {}).get("partner")
      married_text = married.get(f"{user.id}", {}).get("partner")
      embed = discord.Embed(
        title=f"Partnership Status of {user.display_name}",
        description=f"{user.display_name}'s partnership status.",
        color=discord.Color.blue()
      )
      if married_text is not None:
        embed.add_field(
          name="Partnership Status", 
          value=f"{ctx.author.mention} is married to <@" + str(married_text) + ">.",
          inline=False
        )
        await ctx.send(embed = embed)
      elif engaged_text is not None:
        embed.add_field(
          name="Relationship Status",
          value="Engaged to <@" + str(engaged_text) + ">.",
          inline=False
          )
        await ctx.send(embed = embed)
      elif dating_text is not None:
        embed.add_field(
          name="Relationship Status",
          value="Dating <@" + str(dating_text) + ">.",
          inline=False
          )
        await ctx.send(embed = embed)
      elif married_text is None:
        if engaged_text is None:
          if dating_text is None:
            embed.add_field(
              name="Relationship Status",
              value="Not in a relationship!",
              inline=False
            )
            await ctx.send(embed=embed)
  
    @commands.hybrid_command(name = "breakup", description = "Break up with a user", aliases = ["break_up"])
    async def breakup(self, ctx: commands.Context) -> None:
      with open(".gitignore/engaged.json", "r") as f:
        engaged = json.load(f)
      with open(".gitignore/dating.json", "r") as f:
        dating = json.load(f)
      with open(".gitignore/married.json", "r") as f:
        married = json.load(f)
      user = ctx.author
      married_text = married.get(f"{user.id}", {}).get("partner")
      engaged_text = engaged.get(f"{user.id}", {}).get("partner")
      dating_text = dating.get(f"{user.id}", {}).get("partner")
      if engaged_text is not None:
        await ctx.send(f"You have broken up with <@" + str(engaged_text) + ">.")
        del engaged[f"{user.id}"]
        with open(".gitignore/engaged.json", "w") as f:
          engaged = json.dump(engaged, f)
      elif dating_text is not None:
        await ctx.send(f"You have broken up with <@" + str(dating_text) + ">.")
        del dating[f"{user.id}"]
        with open(".gitignore/dating.json", "w") as f:
          dating = json.dump(dating, f)
      elif married_text is not None:
        await ctx.send("You cannot break up with your spouse! Divorce them iinstead with `.divorce`.")

    @commands.hybrid_command(name = "divorce", description = "Divorce your spouse")
    async def divorce(self, ctx: commands.Context) -> None:
      with open(".gitignore/married.json", "r") as f:
        married = json.load(f)
      with open(".gitignore/engaged.json", "r") as f:
        engaged = json.load(f)
      with open(".gitignore/dating.json", "r") as f:
        dating = json.load(f)
      married_text = married.get(f"{ctx.author.id}", {}).get("partner")
      if married_text is not None:
        del married[f"{ctx.author.id}"]
        del engaged[f"{ctx.author.id}"]
        del dating[f"{ctx.author.id}"]
        with open(".gitignore/married.json", "w") as f:
          married = json.dump(married, f)
        with open(".gitignore/engaged.json", "w") as f:
          engaged = json.dump(engaged, f)
        with open(".gitignore/dating.json", "w") as f:
          dating = json.dump(dating, f)
        await ctx.send(f"{ctx.author.mention} has divorced <@" + str(married_text) + ">.")
      elif married_text is None:
        await ctx.send("You are not married.")

async def setup(bot):
  await bot.add_cog(Love(bot))
  print("My Love & Marriage Cog Has Successfully Loaded!")
  return True