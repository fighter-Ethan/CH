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

    @commands.command()
    @commands.has_role(1060431985711009904)
    async def verify(self, ctx, user : discord.Member):

      Unverify = discord.utils.get(ctx.guild.roles, name="Unverified")
      welcomechat = client.get_channel(1140349395334873119)

      await ctx.send(f"Verifying {user.mention}.")
      await asyncio.sleep(1.5)
      await ctx.channel.purge(limit = 2)
      await user.remove_roles(Unverify)

      if verify.error:
        await welcomechat.send(f"{user.mention}")
        embed = discord.Embed(title = "**Welcome to Capitol Hill!**", description = f"Please welcome {user.name}!", color = discord.Color.green())
        embed.set_footer(text = f"Verified by {ctx.author.name}")
        embed.set_image(url = "https://i.imgur.com/ged66wF.png")
        await welcomechat.send(embed=embed)
  
      if not verify.error:
  
        await user.send("Welcome to **Capitol Hill!** To start out, please sign up for local congress or, if open, federal!")

        await welcomechat.send(f"{user.mention}")
        embed = discord.Embed(title = "**Welcome to Capitol Hill!**", description = f"Please welcome {user.name}!", color = discord.Color.green())
        embed.set_image(url = "https://i.imgur.com/ged66wF.png")
        await welcomechat.send(embed=embed)

    @verify.error
    async def verify_error(ctx, error):
      embed = discord.Embed(
        title = "Permissions Error", 
        description = f"{ctx.author.name}, you cannot execute this command!" + "\n\u200b" + "Error: " + str(error), 
        color = discord.Color.red())
      await ctx.send(embed=embed)

    @commands.command()
    async def accept(self, ctx , user : discord.Member , role : discord.Role, crit = "None Provided"):
      await ctx.channel.purge(limit = 1)
      await ctx.send(f"{user.mention}")
      embed = discord.Embed(title = f"**{user.name}**" , description = "*Welcome to the Team!*" , color = discord.Color.green())
      embed.add_field(name = "**Position / Team**" , value = role , inline = False)
      embed.add_field(name = "**Comments**" , value = crit , inline = False)
      embed.set_footer(text = f"Accepted by {ctx.author.name}")
      await ctx.send(embed = embed)
      await user.add_roles(role)

    @commands.command()
    async def deny(self, ctx , user : discord.Member , role : discord.Role, crit = "None Provided"):
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