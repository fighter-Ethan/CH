import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked.")

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, amt = 1):
      if amt == 1:
        await ctx.channel.purge(limit = 2)
      else:
        await ctx.channel.purge(limit = amt + 1)

    @purge.error
    async def purge_error(error, ctx):
      if isinstance(error, CheckFailure):
        await ctx.send(ctx.message.channel, "Looks like you don't have the permissions needed.")


async def setup(bot):
  await bot.add_cog(Admin(bot))
  print("My Admin Cog Has Successfully Loaded!")
  return True