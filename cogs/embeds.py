import discord
from discord.ext import commands

class Embeds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rules(self, ctx):
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
      await ctx.send(embed=embed_rules)

    @commands.command()
    async def custom_embed(self, ctx, Title = None, Description = None, BodyTitle = None, BodyText = None, Thumbnail = None, FooterText = None):
      embed = discord.Embed(
        title = Title,
        description = Description,
        color = discord.Color.blue()
      )
      embed.add_field(
        name = BodyTitle,
        value = BodyText,
        inline = False
      )
      embed.set_thumbnail(url = Thumbnail)
      embed.set_footer(text = FooterText)
      await ctx.send(embed = embed)

    @commands.command()
    async def party_brief(self, ctx, Name = None, Description = None, PartyLeader = None, PartyCharter = None, PartyIdeology = None, PolComp = None, WikiPage = None, Thumbnail = None, CustomColor = None):
      sixteenIntegerHex = int(CustomColor.replace("#", ""), 16)
      readableHex = int(hex(sixteenIntegerHex), 0)
      embed = discord.Embed(
        title = Name,
        description = Description,
        color = readableHex
      )
      embed.add_field(
        name = "**Party Leader**",
        value = PartyLeader,
        inline = False
      )
      embed.add_field(
        name = "**Party Charter**",
        value = PartyCharter,
        inline = False
      )
      embed.add_field(
        name = "**Party Ideology**",
        value = PartyIdeology,
        inline = False
      )
      embed.add_field(
        name = "**Political Compass Position**",
        value = PolComp,
        inline = False
      )
      embed.set_thumbnail(url = Thumbnail)
      await ctx.send(embed = embed)

async def setup(bot):
  await bot.add_cog(Embeds(bot))
  print("My Embed Commands Cog Has Successfully Loaded!")
  return True