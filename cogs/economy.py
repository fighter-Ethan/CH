import discord
from discord.ext import commands

class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def t(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        

async def setup(bot):
  await bot.add_cog(Economy(bot))
  print("My Economy Cog Has Successfully Loaded!")
  return True