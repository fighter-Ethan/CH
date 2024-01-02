import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont, ImageOps
import aiohttp
import textwrap
from textwrap import wrap
import datetime
from datetime import datetime, timedelta
import asyncio
import json
import pytz

class twitter(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.session = aiohttp.ClientSession()


    @commands.Cog.listener()
    async def on_message(self, message):
        nickname = message.author.nick
        if nickname is None: 
          nickname = message.author.name 
        if message.author.bot:
          return
        elif message.channel.id == 1065325485506170891:
          await message.delete()
          avatar_url = str(message.author.avatar.url)
          async with self.session.get(avatar_url) as resp:
            avatar_data = await resp.read()
          with open("json/pfp.png", "wb") as f:
            f.write(avatar_data)
          pfp = Image.open("json/pfp.png").convert("RGBA")
          size = (75, 75)
          mask = Image.new("L", size, 0)
          draw = ImageDraw.Draw(mask)
          draw.ellipse((0, 0) + size, fill=255)
          pfp = ImageOps.fit(pfp, mask.size, centering=(0.5,0.5))
          pfp.putalpha(mask)
          pfp = pfp.resize(size, Image.LANCZOS)
          img = Image.open('json/Tweet_Template.png') 
          draw = ImageDraw.Draw(img)
          img.paste(pfp, (15, 70), pfp)
          font2 = ImageFont.truetype('fonts/Cantarell-Regular.ttf', 20)
          font5 = ImageFont.truetype('fonts/Cantarell-Bold.ttf', 20)
          draw = ImageDraw.Draw(img)
          message_tweet = str(message.content)
          mentions = message.mentions
          output = message_tweet
          for member in mentions:
              output = output.replace(f"<@{member.id}>", f"@{member.display_name}")
          if message.attachments:
            wrapped = textwrap.wrap(output, width=40)
          else:
            wrapped = textwrap.wrap(output, width= 60)
          wrapped_message = '\n'.join(wrapped)
          draw.text((90, 140), wrapped_message, box_width=50, fill='black',font=font2)
          draw.text((111, 111), message.author.name, fill='gray', font=font2)
          draw.text((95, 85), nickname, fill='black', font=font5)
          timezone = pytz.timezone('America/New_York')
          timestamp = datetime.now()
          est = str(timestamp.astimezone(timezone).strftime("%I:%M:%S %p EST • %B %d"))
          draw.text((20, 230), est, fill='gray', font=font2)
          if message.attachments:
            attachment = message.attachments[0]
            url = attachment.url
            async with self.session.get(url) as resp:
              attachment_data = await resp.read()
            with open("json/attachment.png", "wb") as f:
              f.write(attachment_data)     
            attachment = Image.open("attachment.png")
            attachment = attachment.resize((200, 175), Image.LANCZOS)
            img.paste(attachment, (400, 75), attachment)
          img.save('json/Tweet.png')
          react_here = await message.channel.send(file=discord.File('json/Tweet.png'))
          await react_here.add_reaction("❤️")
          await react_here.add_reaction("↪️")



async def setup(bot):
  await bot.add_cog(twitter(bot))
  print("Twitter extension has been loaded") 
  return True