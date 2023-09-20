import discord
from discord.ext import commands

class Politics(commands.Cog):
    def __init__(self, client):
        self.client = client


async def setup(bot):
  await bot.add_cog(Politics(bot))
  print("My Politics Cog Has Successfully Loaded!")
  return True