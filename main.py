import discord
from discord.ext import commands
import dotenv
from dotenv import load_dotenv
import asyncio
import os


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

    
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)