import discord
from discord.ext import commands

class Dev(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command(name = "source", description = "View the bot's source code!")
    async def source(self, ctx: commands.Context) -> None:
      source_embed = discord.Embed(
        title = "Source Code",
        description = "[Click Here](https://github.com/fighter-Ethan/CH)",
        color = discord.Color.green()
      )
      source_embed.set_footer(text = "Licensed under GNU General Licensing v3.0. Property of Auxillium DB.")
      await ctx.reply(embed = source_embed)

    @commands.hybrid_command(name = "ping", description = "View the bot's latency, in milliseconds")
    async def ping(self, ctx):
      embed = discord.Embed(
        title = ":ping_pong: Pong!",
        description = '{0}'.format(round(self.client.latency * 1000 , 0)) + "ms",
        color = discord.Color.green()
      )
      await ctx.send(embed=embed)
      
async def setup(bot):
  await bot.add_cog(Dev(bot))
  print("My Dev Cog Has Successfully Loaded!")
  return True