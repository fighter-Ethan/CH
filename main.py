import discord
import discord.ext
import discord.utils
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, check
import dotenv
from dotenv import load_dotenv
import asyncio
import os
import json
import requests
import random 
import PIL
from PIL import Image, ImageFont, ImageDraw
import openai
import re

from io import BytesIO
from discord import ActionRow, Button, ButtonStyle
from io import BytesIO
import os
from discord.ui import Button, View
from discord import guild
import fandom
from fandom import FandomPage
from bs4 import BeautifulSoup

intents = discord.Intents.all()
client = commands.Bot(command_prefix=".", intents=intents)

client.remove_command('help')

member = discord.Member
load_dotenv()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Love & Marriage | .help"))
    print('Bot is ready')
    for f in os.listdir("./cogs"):
        if f.endswith(".py"):
            await client.load_extension("cogs." + f[:-3])
@client.event
async def on_member_join(user):
    if user.id == "803101128433991732": 
        await user.ban(reason="User banned for breaking the rules.")
            
    
@client.event
async def on_message(message):
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
    await client.process_commands(message)
    
@client.command()
async def ping(ctx):
    await ctx.send(':ping_pong: {0}'.format(round(client.latency * 1000 , 0)) + "ms")

@client.command()
async def yapms(ctx):
    await ctx.send("https://www.yapms.com/")

@client.command()
async def clause(ctx, clause = None):
    if clause == None:
        await ctx.send("Invalid command!")
    elif clause == "commerce":
        embed = discord.Embed(title = "Commerce Clause, in the Constitution of the United States" , description = "Article 1, Section 8, Clause 3" , color = discord.Color.green())
        embed.add_field(name = "\n\u200b" , value = "*Congress shall have the power... to regulate commerce with foreign nations, and among the several states, and with the Indian tribes;*" , inline = True)
        embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
        await ctx.send(embed=embed)

    
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)