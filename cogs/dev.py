import discord
from discord.ext import commands

class Dev(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def source(self, ctx):
      source_embed = discord.Embed(
        title = "Source Code",
        description = "[Click Here](https://github.com/fighter-Ethan/CH)",
        color = discord.Color.green()
      )
      source_embed.set_footer(text = "Licensed under GNU General Licensing v3.0. Property of Auxillium DB.")
      await ctx.reply(embed = source_embed)

    @commands.command()
    async def ping(self, ctx):
      await ctx.send(':ping_pong: {0}'.format(round(self.client.latency * 1000 , 0)) + "ms")
      
async def setup(bot):
  await bot.add_cog(Dev(bot))
  print("My Dev Cog Has Successfully Loaded!")
  return True