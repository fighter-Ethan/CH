import discord
from discord.ext import commands

class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def placeholder(self, ctx):
      await ctx.send("Placeholder Command for the Economy Cog")
        

async def setup(bot):
  await bot.add_cog(Economy(bot))
  print("My Developer Utilities Cog Has Successfully Loaded!")
  return True