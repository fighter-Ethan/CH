import discord
from discord.ext import commands
import random
import requests
import json
import os

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["compat" , "lovers"])
    async def compatibility(self, ctx , user : discord.Member , member : discord.Member):
      if user.mention == "<@978047356983455815>" or member.mention == "<@978047356983455815>":
        await ctx.send("Don't try to ship me! I'm taken.")
      elif user.mention == member.mention:
        await ctx.send("wtf... don't ship yourself with yourself.")
      else:
        loverate = random.randint(0 , 100)
        embed = discord.Embed(
        title = ":heart:Compatability Tester:heart:" , description = user.mention + " + " + member.mention, color  = discord.Color.green())
        embed.add_field(name = "Compatability Rate: " , value = str(loverate) + "%", inline = True)
        embed.set_thumbnail(url = "https://www.northeastohioparent.com/wp-content/uploads/2021/01/Cupid.png")
        embed.set_footer(text = "Come up with a good ship name for these two lovebirds!") 
        await ctx.send(embed=embed)

    @commands.command()
    async def dox(self, ctx, user : discord.Member = None):
      if user == None:
        await ctx.send("You can't dox nobody, idiot!")
      elif user.id == 978047356983455815:
        await ctx.send("HA! You thought you could dox me?")
      elif user.id == ctx.author.id:
        await ctx.send("You want to dox yourself? Idiot. Dox your rivals instead.")
      else:
        doxe = await ctx.send(f"Searching for {user.mention}'s IP address...")
        newdoxe = f"{user.mention}'s IP address is: {random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}:2556"
        await asyncio.sleep(2)
        await doxe.edit(content = newdoxe)

    @commands.command()
    async def joke(ctx, topic = None):
      if topic == None:
        response = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist,sexist,explicit")
        data = response.json()
        try:
          joke = data["setup"]
          joke2 = data["delivery"]
          await ctx.send(joke + "\n\u200b" + joke2)
        except KeyError:
          joke = data["joke"]
          await ctx.send(joke)

    @commands.command()
    async def rr(self, ctx):
      brazild = (random.randint(0 , 6))
      if brazild < 4:
        await ctx.send("*Click*" + "\n\u200b" + "\n\u200b" + random.choice(rrmatrix))
      elif brazild > 5:
        await ctx.send("**BANG!**" + "\n\u200b" + "https://78.media.tumblr.com/80b50d102cdf69e5c172d4cbe336f10d/tumblr_mvc0oeWuPY1qd9rjto1_500.gif")
      elif brazild == 5:
        await ctx.send("**BANG!**" + "\n\u200b" + "https://78.media.tumblr.com/80b50d102cdf69e5c172d4cbe336f10d/tumblr_mvc0oeWuPY1qd9rjto1_500.gif")

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def topic(self, ctx):
      topic = [ 
        'Who was the best President of the United States? Why?', 'Do you code? What language?', 
        'Who is your favorite Avenger?', 
        'What do you do to relax?', 
        "Should pot be legal? Why or why not?", 
        "Have you ever tried pot? How was it?", 
        "What country are you from?", 
        'Which is better: Marvel or DC?', 
        'If you had the chance to meet ONE celebrity right now, who would it be?', 
        'Who is/was your celebrity crush?', 
        'What is your favorite real-life activity?', 
        'What is your favorite video game and why?', 
        'How many friends do you have?', 
        'Is Biden unfit for office?', 
        'Will Kamala Harris ever become president?', 
        'If you work, what is your favorite part of your job?', 
        'Why did you join this server?', 
        'How did you get into politics?', 
        "Where were you on January 6?",
        'If you were alive then, where were you on September 11, 2001? What were you doing when you heard the news?',
        'Do you have a favorite parent?', 
        'Is Hillary Clinton guilty of treason?', 
        'Who will win the Russo-Ukraine War?', 
        'Do you have a favorite sibling?', 
        'Should Trump go to prison?', 
        'Should there be a maximum age for President?', 
        'Have you caught COVID at any point since the start of the breakout?', 
        'What are your official 2024 Presidential Primaries predictions?', 
        'Should the electoral college be abolished?', 
        'What are your thoughts on affirmative action?', 
        'Should gay citizens be allowed to marry? Explain.',
        'Should we abolish the death penalty?', 
        'Do teachers deserve higher pay?', 
        'Should college tuition be regulated by the government?', 
        'How did you realize you are liberal/conservative/etc?', 
        'What is your opinion on QAnon?', 
        'Are you in/do you want to be in politics in real life?', 
        'Thoughts on gun control?', 
        "What would you do if you won the lottery tomorrow morning?", 
        'What do you find the most attractive quality to be in friends?', 
        'Share an embarassing story.', 
        'How old were you when you realized that you wanted to work in your current job?', 
        "Do you have any mental conditions you wouldn't mind sharing?", 
        "What's the creepiest thing you've witnessed?", 
        'What is your favorite music genre?', 
        'Should the United States cancel student loans?',
        'What is the last thing you do before you go to sleep?' , 
        'Who is your oldest friend? Where did you meet them?' , 
        'What do you do to get rid of stress?', 
        'Thoughts on Democratic Socialism?', 
        'Should the United States remain neutral in foreign affairs?', 
        'Is the United Nations good or bad for the world?', 
        'Should we put America first or consider the needs of other countries?', 
        'Do you support Israel, Palestine, both, or neither? Why?', 
        'Who do you think will be president in 2024?', 
        'What are some good things and bad things about the education system in your country?', 
        'What is the strangest dream you have ever had?', 
        'What problems will technology solve in the next 5 years? What problems will it create?', 
        'Do you believe in love at first sight?', 
        'What is the silliest fear you have?', 
        "What is something that really annoys you but doesn't bother most people?", 
        'What book has influenced you the most?', 
        'What technology from a science fiction movie would you most like to have?', 
        'If you lived in Star Wars, would you be a Jedi, Sith, or in between?', 
        'Do You Have Any Phobias Or Fears?', 
        'Would you rather be 3 feet tall or 8 feet tall?', 
        'Do you think people are basically bad or basically good?', 
        'How old do you have to be before it can be said you died of old age?', 
        'What or who made you smile today?', 
        'What is your favorite form of social media?', 
        'What was the last good book you read?', 
        'Do you listen to any podcasts?', 
        'Tell a good joke.', 
        'Tell a bad joke.', 
        'Tell a dad joke.', 
        'Tell a riddle.', 
        'Thoughts on police reform?', 
        "What is your opinion on Puerto Rican statehood? Explain.", 
        "What do you think is the best show on Netflix right now?", 
        "What do you think is the best show on Hulu right now?", 
        "What is the best streaming platform?", 
        "Apple or Samsung?", 
        "Macbook or PC?", 
        "Are you pro-life or pro-choice? Explain.", 
        "In an ideal world, who would you choose to become POTUS?", 
        "Would you support Universal Background Checks? Why or why not?", 
        'Should the United States take in more refugees?', 
        "Should transgender citizens be allowed to play on a team that corresponds with their gender identity? Explain.", 
        "Should transgender people have separate bathrooms? Explain.", 
        "Should the government take more action to recognize non-binary genders? Why?", 
        "Should DC be granted statehood? Why?", 
        "What song describes your current mood?", 
        "Should consenting adults be allowed to receive gender-affirming care? Explain.", 
        "Should polygamy be legalized in the United States?",
        "Is climate change an immediate threat to our health?", 
        "How much of an issue is racism today in America?", 
        "Who is the most oppressed group in the US?", 
        "Does white privelege exist? Justify your answer.",
        "Should the police be defunded? Why or why not?", 
        "Should we practice court packing?", 
        "Should police wear body cams?", 
        "Should the police of the United States be federalized?", 
        "Should church & state be separate? Explain.", 
        "Who won the Space Race?",
        "Should the United States have Universal Healthcare?",
        "Should the United States Military Budget be lowered?", 
        "What religion are you? Why?", 
        "What one Supreme Court precedent would you overturn? Why?",
        "Whoever used this command gets to decide the topic."
      ] 
      topic_print = random.choice(topic)
      embed = discord.Embed(title = "**Topic**" , description = str(topic_print) , color =  discord.Color.blue())
      embed.set_footer(text = f".topic | Requested by {ctx.author.name}")
      await ctx.reply(embed=embed)

    @topic.error
    async def topic_error(ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title = "**Cooldown**" , description = f"This command is on cooldown, try again in {round(error.retry_after)} seconds.", color = discord.Color.red())
        embed.set_footer(text = f"{ctx.author.name}")
        await ctx.send(embed=embed)

async def setup(bot):
  await bot.add_cog(Fun(bot))
  print("My Fun Cog Has Successfully Loaded!")
  return True