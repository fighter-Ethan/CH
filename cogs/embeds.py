import discord
from discord.ext import commands
import asyncio
from typing import Literal

class Embeds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command(name = "help", description = "Shows the help menu for the bot's commands")
    async def help(self, ctx: commands.Context, criteria = None) -> None:
      if criteria == None:
        embed = discord.Embed(
          title = "**Help Menu**", description = "Capitol Hill's Help Interface" , color = discord.Color.red())
        embed.add_field(name = "**amendment [amendment]**" , value = "Recites the selected amendment" + "\n\u200b" , inline = True)
        embed.add_field(name = "**whatis [Court case]**" , value = "Explains a monumental US court case!" + "\n\u200b" , inline = True)
        embed.add_field(name = "*whatis list**" , value = "Displays a list of court cases that Liberty Bot can display" + "\n\u200b" , inline = True)
        embed.add_field(name = "**yapms**" , value = "Sends the link to Yet Another Political Map Simulator" + "\n\u200b")
        embed.add_field(name = "**potus [number]**" , value = "Displays info about the selected president." + "\n\u200b" , inline = True)
        embed.add_field(name = "**help love**", value = "Shows the help menu for the love commands!")
        embed.add_field(name = "**help economy**", value = "Shows the help menu for the economy commands!")
        embed.add_field(name = "**help economy**", value = "Shows the help menu for the economy commands! (Coming soon)")
        embed.set_footer(text = f"Requested by {ctx.author.name}")
        await ctx.reply(embed=embed)
      elif criteria == "love":
        embed = discord.Embed(
          title = "**Love & Marriage Help Menu**", description = "Capitol Hill's Help Interface" , color = discord.Color.red())
        embed.add_field(name = "**date @mention**" , value = "Asks out the mentioned person!", inline = False)
        embed.add_field(name = "**propose @mention**" , value = "Proposes to the mentioned person!" , inline = False)
        embed.add_field(name = "**marry @mention @mention**" , value = "Marries two mentioned people! Must have the Priest role to execute this command." , inline = False)
        embed.add_field(name = "**divorce @mention**" , value = "Divorces the mentioned person." , inline = False)
        embed.add_field(name = "**breakup**" , value = "Breaks you up with your current partner." , inline = False)
        embed.add_field(name = "**partner**", value = "Displays your current partnership status!", inline = False)
        embed.set_footer(text = f"Requested by {ctx.author.name}")
        await ctx.reply(embed=embed)
      elif criteria == "economy":
        embed = discord.Embed(
          title = "**Economy Help Menu**", 
          description = "Economy Help" , 
          color = discord.Color.red()
        )
        embed.add_field(
          name = "open_account",
          value = "Opens your account! Needed to execute any other economy command.",
          inline = False
        )
        embed.add_field(
          name = "close_account",
          value = "Closes your account and deletes all economy data.",
          inline = False
        )
        embed.add_field(
          name = "withdraw [amount]",
          value = "Withdraws the specified amount from your bank account.",
          inline = False
        )
        embed.add_field(
          name = "deposit [amount]",
          value = "Deposits the specified amount into your bank account.",
          inline = False
        )
        embed.add_field(
          name = "work",
          value = "Lets you do odd jobs for money.",
          inline = False
        )
        embed.add_field(
          name = "rob [player]",
          value = "Attempt to rob a player's wallet!",
          inline = False
        )
        embed.add_field(
          name = "leaderboard",
          value = "Shows the top 10 richest players.",
          inline = False
        )
        embed.add_field(
          name = "slots [amount]",
          value = "Bet an amount on slot machines!",
          inline = False
        )
        embed.add_field(
          name = "roulette [red/black] [amount]",
          value = "Bet an amount of money on a color!",
          inline = False
        )
        embed.add_field(
          name = "balance",
          value = "Shows your wallet, bank, and net worth.",
          inline = False
        )
        embed.add_field(
          name = "salary",
          value = "Shows your current salary.",
          inline = False
        )
        embed.add_field(
          name = "collect",
          value = "Collect your salary.",
          inline = False
        )
        embed.add_field(
          name = "shop",
          value = "Open the server shop.",
          inline = False
        )
        embed.add_field(
          name = "inventory",
          value = "Show your owned items.",
          inline = False
        )
        embed.add_field(
          name = "buy",
          value = "Buy items from the store.",
          inline = False
        )
        embed.add_field(
          name = "use",
          value = "Use an item in your inventory.",
          inline = False
        )
        embed.add_field(
          name = "pay [player] [amount]",
          value = "Pay a player an amount of money.",
          inline = False
        )
        await ctx.reply(embed=embed)

    @commands.hybrid_command(name = "rules", description = "Shows the rules for the server")
    @commands.has_role(1060313658053361754)
    async def rules(self, ctx: commands.Context) -> None:
      embed_statement = discord.Embed(title = "Capitol Hill's Mission Statement", description = "Capitol Hill is a community of people who want to explore and engage in the United States political system. You may interact as leaders, business people, the press, and regular citizens. We are united by our respect for each other and the goals of the server.", color = discord.Color.blurple())
      await ctx.send(embed=embed_statement)
      embed_rules = discord.Embed(title = "Capitol Hill Rules" , description = "These are the rules of Capitol Hill. Breaking any of these rules will result in a punishment, as determined by the class of the offense." , color = discord.Color.blue())
      embed_rules.add_field(name = "\n\u200b", value = "**1)** Follow [The Terms of Service for Discord](https://discord.com/terms). [Class Varies]", inline = False)
      embed_rules.add_field(name = "\n\u200b", value = "**2)** No NSFW. [Class II]", inline = False)
      embed_rules.add_field(name = "\n\u200b", value = "**3.** Respect Staff Members. [Class II]", inline = False)
      embed_rules.add_field(name = "\n\u200b", value = "**4.** Do not impersonate Staff Members. [Class III]", inline = False)
      embed_rules.add_field(name = "\n\u200b", value = "**5.** Respect each other! This means that no anti-semitism, racism, homophobia, transphobia, xenophobia, harassment, or other discrimination will be allowed. [Class I]", inline = False)
      embed_rules.add_field(name = "\n\u200b", value = "**6.** No sexualization of minors. [Class I]" , inline = False)
      embed_rules.add_field(name = "\n\u200b", value = "**7.** Do not inflate the economy unnecessarily. [Class II]" , inline = False)
      embed_rules.add_field(name = "\n\u200b", value = "**8.** Do not abuse the use of bots. [Class I]" , inline = False)
      embed_rules.add_field(name = "\n\u200b", value = "**9.** Keep it IRP (In Roleplay). If a member is targeting you IRP without a valid reason, ping an admin or moderator, and have them step in. Do not hurt them OORP (Out of Roleplay). [Class III]" , inline = False)
      embed_rules.add_field(name = "\n\u200b", value = "**10.** Do not intentionally rig elections. [Class III]" , inline = False)
      embed_rules.add_field(name = "\n\u200b", value = "**11.** Do not mass invite people before elections. [Class III]" , inline = False)
      embed_rules.add_field(name = "\n\u200b", value = "**12.** The rules may be updated or edited at any time by staff, with or without notice." , inline = False)
      embed_rules.add_field(name = "\n\u200b", value = "**13.** You may not advertise other servers, in ANY server of the Capitol Hill network, without the explicit permission of Server Staff/Partnership Team leadership. [Class II]" , inline = False)
      await ctx.send(embed=embed_rules)

    @commands.hybrid_command(name = "senate_leadership", description = "Make an embed showing senate leaders! Must be server staff.")
    @commands.has_role(1140349395334873119)
    async def senate_leadership(self, ctx, term = None, vpotus: discord.Member = None, ppt: discord.Member = None, senmajldr: discord.Member = None, senminldr: discord.Member = None):
      embed = discord.Embed(
        title = "Senate Leadership",
        description = "*" + term + "*",
        color = discord.Color.blurple()
      )
      if vpotus != None:
        embed.add_field(
          name = "Vice President",
          value = vpotus.mention,
          inline = False
        )
      if ppt != None:
        embed.add_field(
          name = "President Pro-Tempore",
          value = ppt.mention,
          inline = False
        )
      if senmajldr != None:
        embed.add_field(
          name = "Senate Majority Leader",
          value = senmajldr.mention,
          inline = False
        )
      if senminldr != None:
        embed.add_field(
          name = "Senate Minority Leader",
          value = senminldr.mention,
          inline = False
        )
      embed.set_footer(text = "Capitol Hill Senate")
      embed.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Seal_of_the_United_States_Senate.svg/2000px-Seal_of_the_United_States_Senate.svg.png")
      await ctx.send(embed=embed)

    @commands.hybrid_command(name = "house_leadership", description = "Make an embed showing house leaders! Must be server staff.")
    @commands.has_role(1140349395334873119)
    async def house_leadership(self, ctx, term = None, speaker: discord.Member = None, spt: discord.Member = None, hmajldr: discord.Member = None, hmajw: discord.Member = None, hminldr: discord.Member = None, hminw: discord.Member = None):
      embed = discord.Embed(
        title = "House Leadership",
        description = "*" + term + "*",
        color = discord.Color.blurple()
      )
      if speaker != None:
        embed.add_field(
          name = "Speaker of the House",
          value = speaker.mention,
          inline = False
        )
      if spt != None:
        embed.add_field(
          name = "Speaker Pro-Tempore",
          value = spt.mention,
          inline = False
        )
      if hmajldr != None:
        embed.add_field(
          name = "House Majority Leader",
          value = hmajldr.mention,
          inline = False
        )
      if hmajw != None:
        embed.add_field(
          name = "House Majority Whip",
          value = hmajw.mention,
          inline = False
        )
      if hminldr != None:
        embed.add_field(
          name = "House Minority Leader",
          value = hminldr.mention,
          inline = False
        )
      if hminw != None:
        embed.add_field(
          name = "House Minority Whip",
          value = hminw.mention,
          inline = False
        )
      embed.set_footer(text = "Capitol Hill House")
      embed.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Seal_of_the_United_States_House_of_Representatives.svg/1030px-Seal_of_the_United_States_House_of_Representatives.svg.png")
      await ctx.send(embed=embed)
      
    @commands.hybrid_command(name="scotus", description="Make an embed showing the SCOTUS Composition!")
    async def scotus(
      self, 
      ctx: commands.Context, 
      majority: Literal["Liberal","Conservative","No"], 
      lib: Literal["0","1","2","3","4","5","6","7","8","9"], 
      con: Literal["0","1","2","3","4","5","6","7","8","9"], 
      neutral: Literal["0","1","2","3","4","5","6","7","8","9"], 
      cj: discord.Member = None, 
      cjapp: discord.Member = None, 
      aj1: discord.Member = None, 
      aj1app: discord.Member = None, 
      aj2: discord.Member = None, 
      aj2app: discord.Member = None, 
      aj3: discord.Member = None, 
      aj3app: discord.Member = None, 
      aj4: discord.Member = None, 
      aj4app: discord.Member = None, 
      aj5: discord.Member = None, 
      aj5app: discord.Member = None, 
      aj6: discord.Member = None, 
      aj6app: discord.Member = None, 
      aj7: discord.Member = None, 
      aj7app: discord.Member = None, 
      aj8: discord.Member = None, 
      aj8app: discord.Member = None, 
      courtname = None
    ) -> None:
      embed = discord.Embed(
        title = "Supreme Court of the United States",
        description = f"The {courtname} Court",
        color = discord.Color.blurple()
      )
      embed.set_thumbnail(url = "https://i.imgur.com/OG9BHYp.png")
      if majority == "Liberal":
        embed.set_footer(text = f"🔵 {majority} Majority ({lib}L, {con}C, {neutral}N)")
      elif majority == "Conservative":
        embed.set_footer(text = f"🔴 {majority} Majority ({lib}L, {con}C, {neutral}N)")
      elif majority == "No":
        embed.set_footer(text = f"⚪️ {majority} Majority ({lib}L, {con}C, {neutral}N)")
      if cj != None:
        embed.add_field(
          name = "<:ChiefJustice:1167974621501460520> Chief Justice",
          value = f"{cj.mention} (Appointed by {cjapp.mention})",
          inline = False
        )
      elif cj == None:
        embed.add_field(
          name = "<:ChiefJustice:1167974621501460520> Chief Justice",
          value = "`Vacant`",
          inline = False
        )
      if aj1 != None:
        embed.add_field(
          name = "<:Justice:1167974734965788693> Associate Justice",
          value = f"{aj1.mention} (Appointed by {aj1app.mention})",
          inline = False
        )
      elif aj1 == None:
        embed.add_field(
          name = "<:Justice:1167974734965788693> Associate Justice",
          value = "`Vacant`",
          inline = False
        )
      if aj2 != None:
        embed.add_field(
          name = "<:Justice:1167974734965788693> Associate Justice",
          value = f"{aj2.mention} (Appointed by {aj2app.mention})",
          inline = False
        )
      elif aj2 == None:
        embed.add_field(
          name = "<:Justice:1167974734965788693> Associate Justice",
          value = "`Vacant`",
          inline = False
        )
      if aj3 != None:
        embed.add_field(
          name = "<:Justice:1167974734965788693> Associate Justice",
          value = f"{aj3.mention} (Appointed by {aj3app.mention})",
          inline = False
        )
      elif aj3 == None:
        embed.add_field(
          name = "<:Justice:1167974734965788693> Associate Justice",
          value = "`Vacant`",
          inline = False
        )
      if aj4 != None:
        embed.add_field(
          name = "<:Justice:1167974734965788693> Associate Justice",
          value = f"{aj4.mention} (Appointed by {aj4app.mention})",
          inline = False
        )
      elif aj4 == None:
        embed.add_field(
          name = "<:Justice:1167974734965788693> Associate Justice",
          value = "`Vacant`",
          inline = False
        )
      if aj5 != None:
        embed.add_field(
          name = "<:Justice:1167974734965788693> Associate Justice",
          value = f"{aj5.mention} (Appointed by {aj5app.mention})",
          inline = False
        )
      elif aj5 == None:
        embed.add_field(
          name = "<:Justice:1167974734965788693> Associate Justice",
          value = "`Vacant`",
          inline = False
        )
      if aj6 != None:
        embed.add_field(
          name = "<:Justice:1167974734965788693> Associate Justice",
          value = f"{aj6.mention} (Appointed by {aj6app.mention})",
          inline = False
        )
      elif aj6 == None:
        embed.add_field(
          name = "<:Justice:1167974734965788693> Associate Justice",
          value = "`Vacant`",
          inline = False
        )
      if aj7 != None:
        embed.add_field(
          name = "<:Justice:1167974734965788693> Associate Justice",
          value = f"{aj7.mention} (Appointed by {aj7app.mention})",
          inline = False
        )
      elif aj7 == None:
        embed.add_field(
          name = "<:Justice:1167974734965788693> Associate Justice",
          value = "`Vacant`",
          inline = False
        )
      if aj8 != None:
        embed.add_field(
          name = "<:Justice:1167974734965788693> Associate Justice",
          value = f"{aj8.mention} (Appointed by {aj8app.mention})",
          inline = False
        )
      elif aj8 == None:
        embed.add_field(
          name = "<:Justice:1167974734965788693> Associate Justice",
          value = "`Vacant`",
          inline = False
        )
      await ctx.send(embed=embed)
  
    @commands.hybrid_command(name="custom_embed", description = "Create a custom embed!")
    async def custom_embed(self, ctx: commands.Context, title = None, description = None, body_title_1 = None, body_text_1 = None, body_title_2 = None, body_text_2 = None, body_title_3 = None, body_text_3 = None, thumbnail = None, footertext = None) -> None:
      embed = discord.Embed(
        title = title,
        description = description,
        color = discord.Color.blue()
      )
      embed.add_field(
        name = bodytitle,
        value = bodytext,
        inline = False
      )
      embed.set_thumbnail(url = thumbnail)
      embed.set_footer(text = footertext)
      if body_title_2 != None:
        embed.add_field(
          name = body_title_2,
          value = body_text_2,
          inline = False
        )
      if body_title_3 != None:
        embed.add_field(
          name = body_title_3,
          value = body_text_3,
          inline = False
        )
      await ctx.send(embed = embed)

    @commands.hybrid_command(name = "party_brief", description = "Make an embed showing party briefs")
    @commands.has_role(1060313658053361754)
    async def party_brief(self, ctx: commands.Context, name = None, description = None, party_leader = None, party_charter = None, party_ideology = None, pol_comp = None, thumbnail = None, custom_color = None) -> None:
      sixteenIntegerHex = int(CustomColor.replace("#", ""), 16)
      readableHex = int(hex(sixteenIntegerHex), 0)
      embed = discord.Embed(
        title = name,
        description = description,
        color = readableHex
      )
      embed.add_field(
        name = "**Party Leader**",
        value = party_leader,
        inline = False
      )
      embed.add_field(
        name = "**Party Charter**",
        value = party_charter,
        inline = False
      )
      embed.add_field(
        name = "**Party Ideology**",
        value = party_ideology,
        inline = False
      )
      embed.add_field(
        name = "**Political Compass Position**",
        value = pol_comp,
        inline = False
      )
      embed.set_thumbnail(url = thumbnail)
      await ctx.send(embed = embed)

    @commands.hybrid_command(name = "team", description = "Creates an embed to give information about a server team!")
    @commands.has_role(1060313658053361754)
    async def team(self, ctx: commands.Context, team_name = None, team_description = None, team_lead: discord.Member = None, applications = None, logo = None) -> None:
      if team_name == None:
        await ctx.send("Please specify a team name!")
        return
      if team_description == None:
        await ctx.send("Please specify a team description!")
        return
      if team_lead == None:
        await ctx.send("Please specify a team lead!")
        return
      if logo == None:
        await ctx.send("Please specify a logo link!")
      else:
        embed = discord.Embed(
          title = team_name,
          description = team_description,
          color = discord.Color.blurple()
        )
        embed.add_field(
          name = "**Team Lead**",
          value = team_lead.mention,
          inline = False
        )
        embed.add_field(
          name = "**Accepting Applications?**",
          value = applications,
          inline = False
        )
        embed.set_thumbnail(url = logo)
        await ctx.send(embed = embed)

    @team.error
    async def team_error(self, ctx: commands.Context, error):
      if isinstance(error, commands.MissingRole):
        await ctx.send("You don't have the required role to use this command!")
      elif isinstance(error, commands.BadArgument):
        await ctx.send("Please specify a valid color!")

async def setup(bot):
  await bot.add_cog(Embeds(bot))
  print("My Embed Commands Cog Has Successfully Loaded!")
  return True