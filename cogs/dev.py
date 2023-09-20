import discord
from discord.ext import commands

class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def source(self, ctx):
      source = discord.Embed(
        title = "Source Code",
        description = "[Click Here](https://github.com/fighter-Ethan/CH)",
        color = discord.Color.green()
      )
      source.set_footer(text = "Track the Source Code across updates with the GitHub Above!")
      await ctx.reply(embed = source)
        

async def setup(bot):
  await bot.add_cog(Economy(bot))
  print("My Economy Cog Has Successfully Loaded!")
  return True