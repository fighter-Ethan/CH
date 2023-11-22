import discord
from discord.ext import commands
import asyncio

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client
  
    @commands.hybrid_command(name="kick", description="Kicks a member from the server. Must be a member of Server Staff to execute this command!.") 
    @commands.has_role(1060313658053361754)
    async def kick(self, ctx: commands.Context, member: discord.Member, *, reason=None) -> None:
      await member.kick(reason=reason)
      await ctx.reply(f"{member.mention} has been kicked.")
      
    @kick.error
    async def kick_error(self, ctx, error): 
      if isinstance(error, commands.MissingRole):
       await ctx.reply("You do not have permission to use this command.")   
 
    @commands.hybrid_command(name = "purge", description = "Deletes a specified amount of messages. Must be a member of Server Staff to execute this command!.")
    @commands.has_role(1060313658053361754)
    async def purge(self, ctx: commands.Context, amount = 1) -> None:
      if amount == 1:
        await ctx.channel.purge(limit = 2)
      else:
        await ctx.channel.purge(limit = amount + 1)

    @purge.error
    async def purge_error(error, ctx):
      if isinstance(error, CheckFailure):
        await ctx.send(ctx.message.channel, "Looks like you don't have the permissions needed.")

    @commands.hybrid_command(name = "verify", description = "Verifies a user. Must be a member of Server Staff to execute this command!")
    @commands.has_role(1140349395334873119)
    async def verify(self, ctx: commands.Context, user : discord.Member) -> None:

      Unverify = discord.utils.get(ctx.guild.roles, name="Unverified")
      Verify = discord.utils.get(ctx.guild.roles, name="Verified")
      welcomechat = self.client.get_channel(1065320854059225118)

      await ctx.send(f"Verifying {user.mention}.")
      await asyncio.sleep(1.5)
      await ctx.channel.purge(limit = 2)
      await user.remove_roles(Unverify)
      await user.add_roles(Verify)

      await welcomechat.send(f"{user.mention}")
      embed = discord.Embed(title = "**Welcome to Capitol Hill!**", description = f"Please welcome {user.name}!", color = discord.Color.green())
      embed.add_field(name = "**Getting Started**", value = "To get started, you can head over to <#1150207359117959198> to join the House, or wait for an election!")
      embed.set_footer(text = f"Verified by {ctx.author.name}")
      embed.set_image(url = "https://i.imgur.com/ged66wF.png")
      await welcomechat.send(embed=embed)
      await welcomechat.send("<@&1175490044665008138>")
  
      

    @verify.error
    async def verify_error(self, ctx, error):
      embed = discord.Embed(
        title = "Permissions Error", 
        description = f"{ctx.author.name}, you cannot execute this command!" + "\n\u200b" + "Error: " + str(error), 
        color = discord.Color.red())
      await ctx.send(embed=embed)

    @commands.hybrid_command(name="accept" , description="Accepts a user's application to a department. Must be a member of department leadership to use this!")
    async def accept(self, ctx: commands.Context , user : discord.Member , role : discord.Role, crit = "None Provided") -> None:
      await ctx.channel.purge(limit = 1)
      await ctx.send(f"{user.mention}")
      embed = discord.Embed(title = f"**{user.name}**" , description = "*Welcome to the Team!*" , color = discord.Color.green())
      embed.add_field(name = "**Position / Team**" , value = role , inline = False)
      embed.add_field(name = "**Comments**" , value = crit , inline = False)
      embed.set_footer(text = f"Accepted by {ctx.author.name}")
      await ctx.send(embed = embed)
      await user.add_roles(role)

    @commands.hybrid_command(name="deny" , description="Denies a user's application to a department. Must be a member of department leadership to use this!")
    async def deny(self, ctx: commands.Context , user : discord.Member , role : discord.Role, crit = "None Provided") -> None:
      await ctx.channel.purge(limit = 1)
      await ctx.send(f"{user.mention}")
      embed = discord.Embed(title = f"{user.name}" , description = "Application Rejected." , color = discord.Color.red())
      embed.add_field(name = "**Position / Team**" , value = role , inline = False)
      embed.add_field(name = "**Comments**" , value = crit , inline = False)
      embed.set_footer(text = f"Denied by {ctx.author.name}")
      await ctx.send(embed = embed)


async def setup(bot):
  await bot.add_cog(Admin(bot))
  print("My Admin Cog Has Successfully Loaded!")
  return True