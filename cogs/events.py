import discord
from discord.ext import commands
import os
import json
import requests

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(user):
      if user.id == "803101128433991732": 
        await user.ban(reason="User banned for breaking the rules.")

  
    @commands.Cog.listener()
    async def on_message(self, message):
      if message.channel.id == 1116375497480351806:
        await message.add_reaction(":Aye:1117197441381437562")
        await message.add_reaction(":Nay:1117192973109698590")
        await message.add_reaction(":Abstain:1117196931123388496")
      elif message.channel.id == 1120744405855375410:
        await message.add_reaction(":Aye:1117197441381437562")
        await message.add_reaction(":Nay:1117192973109698590")
        await message.add_reaction(":Abstain:1117196931123388496")
      elif message.channel.id == 1121653384877981707:
        await message.add_reaction(":Aye:1117197441381437562")
        await message.add_reaction(":Nay:1117192973109698590")
        await message.add_reaction(":Abstain:1117196931123388496")
  
async def setup(bot):
  await bot.add_cog(Events(bot))
  print("My Events Listener Cog Has Successfully Loaded!")
  return True