#---STARTUP---#
import secrets
from discord import embeds, member
import praw
import discord
import os
from discord import user
from discord import colour
from discord.channel import VoiceChannel
from discord.client import Client
from discord.ext import commands 
from discord.guild import Guild
from discord.guild import GroupChannel
from discord.channel import TextChannel
import logging
import random
import time
import mojang
from mojang import MojangAPI
import requests

from discord.role import Role, RoleTags


#intents
intents = discord.Intents.all()
intents.presences = True 
intents.members = True
intents.guilds =True

#Reddit validation stuff
reddit = praw.Reddit(client_id = "BsZC4qVYaLpCEclkm545zw",
                        client_secret = "hehe",
                        username = "Brilliant_Opening225",
                        password = "hehe wouldnt you like to know",
                        user_agent = "pythonpraw")

#hypixle api
key = str('hehe')
#prefix
client = commands.Bot(command_prefix='.', intents=intents)

#COGS
@client.command()
@commands.has_permissions(administrator = True)
async def load(ctx, extension):
    client.load_extension(f'COGS.{extension}')
    embed = discord.Embed(description = f'Loaded cogs ({extension})', color = discord.Color.greyple())
    await ctx.send(embed=embed)
@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed=discord.Embed(description='Sorry, you are not allowed to use this command.', color=discord.Color.dark_blue())
        await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator = True)
async def unload(ctx, extension):
    client.unload_extension(f'COGS.{extension}')
    embed = discord.Embed(description = f'Unloaded cogs ({extension})', color = discord.Color.greyple())
    await ctx.send(embed=embed)
@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed=discord.Embed(description='Sorry, you are not allowed to use this command.', color=discord.Color.dark_blue())
        await ctx.send(embed=embed)


for filename in os.listdir('D:\code\Pyroplex chedbot\COGS'):
    if filename.endswith('.py'):
        client.load_extension(f'COGS.{filename[:-3]}')

#help remove
client.remove_command('help')

#bot online confirm
@client.event
async def on_ready():
    print('Bot ready')
    guild = client.get_guild(913509940050665482)
    channel = guild.get_channel(915058380551376926)
    embed=discord.Embed(description=f'Bot status:\n ONLINE', color=discord.Color.red())
    await channel.send(embed=embed)

#bot status
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='.Help or ping me!'))


#---USER LEAVE/JOIN LOGS---#

#member join bot logs
@client.event
async def on_member_join(member : discord.Member):
    channel = discord.utils.get(member.guild.channels, name="🦕｜bot-logs")
    embed = discord.Embed(title = f'Member joined: {member.name} \n', discription = f'{member.mention}', color = discord.Color.magenta())
    embed.add_field(name = "User", value = member.mention, inline=False)
    embed.add_field(name = "ID", value = member.id, inline=True)
    embed.add_field(name = "Status", value = member.activity, inline=True)
    embed.add_field(name = "User", value = member._user, inline=True)
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(text=f'Time joined: {member.joined_at.strftime("%a, %b %d %Y at %H:%M:%S %p")}')
    await channel.send(embed=embed)

#member leave bot logs
@client.event
async def on_member_remove(member : discord.Member):
    channel = discord.utils.get(member.guild.channels, name="🦕｜bot-logs")
    embed = discord.Embed(title = f'Member left: {member.name} \n', discription = f'{member.mention}', color = discord.Color.magenta())
    embed.add_field(name = "User", value = member.mention, inline=False)
    embed.add_field(name = "ID", value = member.id, inline=True)
    embed.add_field(name = "Status", value = member.activity, inline=True)
    embed.add_field(name = "Top role", value = member.top_role.mention, inline=True)
    embed.add_field(name = "User", value = member._user, inline=True)
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(text=f'Time left: *whenever this message was sent*')
    await channel.send(embed=embed)


#---COMMANDS---#

#discord support server
@client.command(aliases=['Support', 'testing', 'test_server'])
async def support(ctx):
    embed=discord.Embed(description='Hey there! You can join the support/testing server for me here:\n https://discord.gg/enXNPj6ts2', color=discord.Color.dark_orange())
    await ctx.send(embed=embed)

#github
@client.command(aliases=['Github','git','Git','source_code'])
async def github(ctx):
    embed = discord.Embed(title='GitHub', description=f'Hey there {ctx.author.mention}! You can find the Chedbot source code below!',color=discord.Color.magenta())
    embed.add_field(name='Github link:', value='||https://github.com/Chedboy2-0/Chedbot2.0||')
    embed.set_footer(text='*Please dont rip the code :)')
    await ctx.send(embed=embed)
    
#member count/list
@client.command()
async def members(ctx):
    embed=discord.Embed(description=f'This server has {ctx.guild.member_count} members! How cool is that?', color=discord.Color.magenta())
    await ctx.send(embed=embed)

#latency
@client.command()
async def ping(ctx):
    embed=discord.Embed(description=f"Pong! I responded in {float(round(client.latency * 100))} ms. Ain't that impressive!", color=discord.Color.magenta())
    await ctx.send(embed=embed)

#avatar
@client.command(aliases=['Avatar'])
async def avatar(ctx, member : discord.Member):
    embed = discord.Embed(title = f'Avatar of {member.name} \n', discription = f'{member.mention}', color = discord.Color.magenta())
    embed.add_field(name='User:', value=member.mention, inline=True)
    embed.set_thumbnail(url = member.avatar_url)
    await ctx.send(embed=embed)

#servers
@client.command(aliases=['Servers'])
async def servers(ctx):
    activeservers = list(client.guilds)
    embed=discord.Embed(description=f'Chedbot is in {str(len(client.guilds))} servers.', color=discord.Color.blue())
    await ctx.send (embed=embed)

##--HYPIXEL STUFF---#

#waf tracker
@client.command()
async def run(ctx):
    guild = client.get_guild(762718463575064636)
    channel = guild.get_channel(980466259005157436)
    embed=discord.Embed(description=f"WAF'S ONLINEEEEEEE!", color=discord.Color.dark_magenta())
    user = str('STUFFEDWAFFLES')
    uuid =MojangAPI.get_uuid(user)
    onlinelink = str(f'https://api.hypixel.net/status?key={hehe}&uuid={uuid}')
    print(onlinelink)
    x=0
    while x < 1:
        online1 = requests.get(onlinelink).json()
        print(online1)
        if online1['session']['online'] == False:
            print(f' {user} is offline.')
            await channel.send('wafs not online :(')
            time.sleep(60)
        else:
            print(f'{user} is online.')
            embed.add_field(name='Game Type:',value=online1['session']['gameType'], inline=False)
            embed.add_field(name='Mode:',value=online1['session']['mode'], inline=False)
            embed.add_field(name='Map:',value=online1['session']['map'], inline=False)
            embed.set_footer(text='This action was brought to you by the Hypixel API!')
            await channel.send(embed=embed)
            time.sleep(1800)
#the bois online?
@client.command(aliases=['kol'])
async def kingdomonline(ctx):
                                            #waffles:
    user = str('STUFFEDWAFFLES')
    uuid =MojangAPI.get_uuid(user)
    onlinelink = str(f'https://api.hypixel.net/status?key={key}&uuid={uuid}')
    print(onlinelink)
    online1 = requests.get(onlinelink).json()
    print(online1)
    if online1['session']['online'] == False:
        print(f' {user} is offline.')
        a = str('Offline')
    else:
        print(f'{user} is online.')
        a = str('Online')
                                                #daklol
    user = str('Daklol')
    uuid =MojangAPI.get_uuid(user)
    onlinelink = str(f'https://api.hypixel.net/status?key={key}&uuid={uuid}')
    print(onlinelink)
    online1 = requests.get(onlinelink).json()
    print(online1)
    if online1['session']['online'] == False:
        print(f' {user} is offline.')
        b = str('Offline')
    else:
        print(f'{user} is online.')
        b = str('Online')
                                                #ched
    user = str('Chedboy2_0')
    uuid =MojangAPI.get_uuid(user)
    onlinelink = str(f'https://api.hypixel.net/status?key={key}&uuid={uuid}')
    print(onlinelink)
    online1 = requests.get(onlinelink).json()
    print(online1)
    if online1['session']['online'] == False:
        print(f' {user} is offline.')
        c = str('Offline')
    else:
        print(f'{user} is online.')
        c = str('Online')
                                                #Jedi
    user = str('ItsJedi')
    uuid =MojangAPI.get_uuid(user)
    onlinelink = str(f'https://api.hypixel.net/status?key={key}&uuid={uuid}')
    print(onlinelink)
    online1 = requests.get(onlinelink).json()
    print(online1)
    if online1['session']['online'] == False:
        print(f' {user} is offline.')
        d = str('Offline')
    else:
        print(f'{user} is online.')
        d = str('Online')
                                                #Para
    user = str('paracreeper21')
    uuid =MojangAPI.get_uuid(user)
    onlinelink = str(f'https://api.hypixel.net/status?key={key}&uuid={uuid}')
    print(onlinelink)
    online1 = requests.get(onlinelink).json()
    print(online1)
    if online1['session']['online'] == False:
        print(f' {user} is offline.')
        e = str('Offline')
    else:
        print(f'{user} is online.')
        e = str('Online')
                                                #destiny
    user = str('SuperDestinyRD')
    uuid =MojangAPI.get_uuid(user)
    onlinelink = str(f'https://api.hypixel.net/status?key={key}&uuid={uuid}')
    print(onlinelink)
    online1 = requests.get(onlinelink).json()
    print(online1)
    if online1['session']['online'] == False:
        print(f' {user} is offline.')
        f = str('Offline')
    else:
        print(f'{user} is online.')
        f = str('Online')
                                                #Frank
    user = str('ThunderMesa')
    uuid =MojangAPI.get_uuid(user)
    onlinelink = str(f'https://api.hypixel.net/status?key={key}&uuid={uuid}')
    print(onlinelink)
    online1 = requests.get(onlinelink).json()
    print(online1)
    if online1['session']['online'] == False:
        print(f' {user} is offline.')
        g = str('Offline')
    else:
        print(f'{user} is online.')
        g = str('Online')

    embed = discord.Embed(title='Members of kingdom that are online:', description = '(On hypixel)', color=discord.Colour.dark_orange())
    embed.add_field(name='STUFFEDWAFFLES:', value=a, inline=True)
    embed.add_field(name='Daklol:', value=b, inline=True)
    embed.add_field(name='Chedboy2_0:', value=c, inline=True)
    embed.add_field(name='Jedi:', value=d, inline=True)
    embed.add_field(name='Para:', value=e, inline=True)
    embed.add_field(name='Destiny:', value=f, inline=True)
    embed.add_field(name='Frank:', value=g, inline=True)
    embed.set_footer(icon_url=ctx.author.avatar_url, text = f'Requested by {ctx.author.name}')
    await ctx.send(embed=embed)

#basic stats
@client.command(aliases=['huser'])
async def hypixeluser(ctx, playername):
    uuid = MojangAPI.get_uuid(playername)
    onlinelink1 = str(f'https://api.hypixel.net/status?key={key}&uuid={uuid}')
    print(onlinelink1)
    online1 = requests.get(onlinelink1).json()
    print(online1)
    if online1['session']['online'] == False:
        print(f' {playername} is offline.')
        g = str('Offline')
    else:
        print(f'{playername} is online.')
        g = str('Online')
    onlinelink2 = str(f'https://api.hypixel.net/player?key={key}&uuid={uuid}')
    onlinelink = requests.get(onlinelink2).json()
    print(onlinelink)
    a = str(onlinelink['player']['displayname'])
    player = await hypixel.get_player(uuid)
    embed = discord.Embed(title=f"{playername}'s Basic hypixel stats:", color=discord.Color.dark_orange())
    embed.add_field(name='Display name:', value=a, inline=True)
    embed.add_field(name='Online?', value=g, inline=True)
    embed.add_field(name='Rank:',value=player.rank, inline=True)
    embed.add_field(name='Rank colour:', value=player.rank_plus, inline=True)
    embed.add_field(name='Level:', value=player.level, inline=True)
    embed.add_field(name='Karma:', value=player.karma, inline=True)
    embed.set_footer(icon_url=ctx.author.avatar_url, text = f'Requested by {ctx.author.name}')
    await ctx.send(embed=embed)
    await ctx.send('Note: This will not record any ranks bought after the Hypixel API rank changes, as the PyPixel wrapper does not support it.')
 

#---FUN---#


#say
@client.command(aliases=['Say'])
async def say(ctx, *, user_message, amount=1):
    await ctx.channel.purge(limit= amount)
    embed = discord.Embed(description=user_message, color=discord.Color.dark_gold())
    await ctx.send(embed=embed)

#quote
@client.command(aliases=['Quote'])
async def quote(ctx, member : discord.Member, *, user_message,  amount=1):
    await ctx.channel.purge(limit= amount)
    embed = discord.Embed(description=f'"{user_message}" - {member.mention}', color=discord.Color.dark_gold())
    await ctx.send(embed=embed)

#fatals ship cmd
@client.command()
async def ship(ctx):
    embed=discord.Embed(description='***Insert picture of ship here***', color=discord.Color.dark_gold())
    await ctx.send(embed=embed)

#dad jokes
@client.command(aliases=['dad joke'])
async def dad_joke(ctx):
    dj = ['What kind of noise does a witch’s vehicle make?\n ||Brrrroooom, brrroooom||',
        'What kind of drink can be bitter and sweet?\n||Reali-tea||',
        'When does a joke become a “dad joke?” \n||When it becomes apparent||',
        'What do you call an angry musician flipping someone off? \n||A song bird||',
        'Why do bees have sticky hair? \n||Because they use a honeycomb||',
        'How does a penguin build his house? \n||Igloos it together||',
        'Why is cold water so insecure? \n||Because it’s never called hot||',
        'What kind of music do chiropractors like?\n||Hip pop||',
        'What kind of car does a sheep like to drive?\n||A lamborghini||',
        'What did the accountant say while auditing a document?\n||This is taxing||',
        'What did the two pieces of bread say on their wedding day? \n||It was loaf at first sight||',
        'If the early bird gets the worm, I’ll sleep in until there’s pancakes.',
        'Why do melons have weddings? \n||Because they cantaloupe.||',
        'I signed up for a marathon, but how will I know if it’s the real deal or just a run through?',
        'When you have a bladder infection, urine trouble.',
        'What did the drummer call his twin daughters?\n||Anna One, Anna Two!||',
        'What did the juicer say to the orange during self-quarantine? \n||Can’t wait to squeeze you!||',
        'What do you call a toothless bear? \n||A gummy bear!||',
        'Want to hear a joke about construction? \n||I’m still working on it.||',
        'Someone told me that I should write a book. I said, “That’s a novel concept.”',
        'Two goldfish are in a tank. One says to the other, “Do you know how to drive this thing?”',
        ]
    embed=discord.Embed(description=f'{random.choice(dj)}', color=discord.Color.dark_purple())
    await ctx.send(embed=embed)

#8ball
@client.command(aliases=['8ball', 'G8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                "It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    embed=discord.Embed(description=f'Question: {question}\nAnswer: {random.choice(responses)}', color=discord.Color.dark_purple())
    await ctx.send(embed=embed)
@_8ball.error
async def _8ball_error(ctx, error):
    embed=discord.Embed(description='You need to put a question with that one bossman', color=discord.Color.dark_purple())
    await ctx.send(embed=embed)

#captain obvious
@client.command(aliases=['cpt','obviously'])
async def captain_obvious(ctx):
    yes = ["The floor is made of floor",
    "The sky is above you.",
    "I am smarter than dak.",
    "Fish like to swim.",
    "I'm powered by electricity.",
    "At some point, you were born.",
    "I'm better coded than daklol knows.",
    "Daklol doesn't know how to code well.",
    "People enjoy thinngs that they enjoy",
    "Error_404:\nIntelligence not found.",
    "Your desktop wallpaper (or lack thereof) is on your desktop.",
    "The wall nearest to you is joined to another wall.",
    "Jedi's bot is not as good as me.",
    "The desk is made of desk-making materials.",
    "You are the result of a star taking a fat dump.",
    "If you can search things on google, you have internet connection.",
    "You have internet connection right now.",
    "Jedi is a poggers child, arent ya m'boy?",]
    embed=discord.Embed(description=f'{random.choice(yes)}', color=discord.Color.dark_purple())
    await ctx.send(embed=embed)

#coinflip
@client.command(aliases=['Coinflip'])
async def coinflip(ctx):
    responses = ["Heads",
                "Tails",
                "Heads",
                "Tails",
                "Heads",
                "Tails",
                "Heads",
                "Tails",
                "Heads",
                "Tails",
                "Heads",
                "Tails",
                "Heads",
                "Tails",
                "Heads",
                "Tails",
                "Heads",
                "Tails",
                "Heads",
                "Tails",
                "Heads",
                "Tails",
                "On its side"]
    n = random.choice(responses)
    embed=discord.Embed(description=f'And the answer is:\n {n}!', color=discord.Color.dark_purple())
    if n == "On its side":
        e=discord.Embed(description=f"It landed on its side...\nLMAO GET REKT\nMaybe respin? Or don't, idc", color=discord.Color.dark_purple())
        await ctx.send(embed=e)
    else:
        await ctx.send(embed=embed)

#smite
@client.command(aliases=['Smite'])
async def smite(ctx, member : discord.Member,*, reason='Lmao get smote bitch', amount=1):
    await ctx.channel.purge(limit= amount)
    embed=discord.Embed(description=f'***{member.mention} was smited by {ctx.author.mention}***\n||*"{reason}"*||', color=discord.Color.dark_gold())
    await ctx.send(embed=embed)

#---REDDIT---#


#meme
@client.command()
async def meme(ctx):
    subreddit = reddit.subreddit("memes")
    all_subs = []
    top = subreddit.top(limit = 100)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title = name, color=discord.Color.dark_gold())
    em.set_image(url = url)
    await ctx.send(embed = em)

#LifeProTips
@client.command()
async def lpt(ctx):
    subreddit = reddit.subreddit("LifeProTips")
    all_subs = []
    top = subreddit.top(limit = 100)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title = name, color=discord.Color.dark_gold())
    em.set_image(url = url)
    await ctx.send(embed = em)

#Minecraft
@client.command()
async def rminecraft(ctx):
    subreddit = reddit.subreddit("minecraft")
    all_subs = []
    top = subreddit.top(limit = 100)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title = name, color=discord.Color.dark_gold())
    em.set_image(url = url)
    await ctx.send(embed = em)

#mildlyinteresting
@client.command(aliases=['mi'])
async def mildly_interesting(ctx):
    subreddit = reddit.subreddit("mildlyinteresting")
    all_subs = []
    top = subreddit.top(limit = 100)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title = name, color=discord.Color.dark_gold())
    em.set_image(url = url)
    await ctx.send(embed = em)

#cursed comments
@client.command(aliases=['cc'])
async def cursed_comments(ctx):
    subreddit = reddit.subreddit("cursed_comments")
    all_subs = []
    top = subreddit.top(limit = 100)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(description = name, color=discord.Color.dark_gold())
    em.set_image(url = url)
    await ctx.send(embed = em)

client.run(secrets1['TOKEN'])
