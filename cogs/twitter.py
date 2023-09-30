import discord
from discord.ext import commands

class Twitter(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
      if message.author.nick != None:
        nick = message.author.nick
      else:
        nick = message.author.name
      if message.channel.id == 1065325485506170891:
        if message.author.id == 1117224998537547817:
          return
        else:
          await message.delete()
          embed = discord.Embed(
            title=f"Tweet:", 
            description=message.content,
            color=discord.Color.blue(),
          )
          embed.set_author(name=f"{nick} (@{message.author.name})", icon_url=message.author.avatar.url)
          embed.set_footer(text=f"Twitter", icon_url="https://png.pngtree.com/png-vector/20221018/ourmid/pngtree-twitter-social-media-round-icon-png-image_6315985.png")
          msg = await message.channel.send(embed=embed)
          await msg.add_reaction("❤️")
          await msg.add_reaction("🗑️")
        

async def setup(bot):
  await bot.add_cog(Twitter(bot))
  print("My Twitter Cog Has Successfully Loaded!")
  return True