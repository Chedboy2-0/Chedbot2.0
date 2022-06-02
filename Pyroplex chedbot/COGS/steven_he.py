#---STARTUP---#
from turtle import title
import discord
from discord.ext import commands
from discord.ext.commands.converter import clean_content
from discord.utils import time_snowflake
import praw
import os
from discord import user
from discord import colour
from discord import message
from discord import role
from discord.message import Message
from discord.channel import VoiceChannel
from discord.client import Client
from discord.ext import commands 
from discord.guild import Guild
from discord.guild import GroupChannel
from discord.channel import TextChannel
import random
from discord.role import Role, RoleTags
import contextlib
import datetime
import time

#at the request of dak:
#    EMOTIONAL DAMAGE

#gifs library
a = str('https://tenor.com/view/emotional-damage-emotional-damage-meme-funny-gif-24332819')
b = str('https://tenor.com/view/steven-he-asian-dont-be-a-dick-gif-21836317')
c = str('https://tenor.com/view/steven-he-what-the-hell-you-say-whaat-da-haill-u-sai-asian-parent-gif-21836333')
d = str('https://tenor.com/view/steven-he-what-the-hell-gif-21811925')
e = str('https://tenor.com/view/failure-steven-he-gif-21298141')
f = str('https://tenor.com/view/steven-he-dont-do-drugs-funny-expensive-advice-gif-23537466')
g = str('https://tenor.com/view/stoobid-steven-he-dumb-you-so-stoobid-gif-21984392')
h = str('https://tenor.com/view/stop-crying-you-get-constipated-steven-he-gif-21957461')
i = str('https://tenor.com/view/steven-he-bruh-moment-funny-gif-24202171')
j = str('https://tenor.com/view/steven-he-i-will-send-you-to-jezus-gif-24191118')



class steven(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Steven online')
        guild = self.client.get_guild(913509940050665482)
        channel = guild.get_channel(915058380551376926)
        embed=discord.Embed(description=f'Steven status:\n ONLINE', color=discord.Color.red())
        await channel.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author.bot == False:
            if 'emotional damage' in msg.content or 'Emotional damage' in msg.content or 'EMOTIONAL DAMAGE' in msg.content:
                    await msg.channel.send(a)
                    
            if "wtf" in msg.content or 'wot' in msg.content or 'what the hell' in msg.content:
                    x = random.randint(1,2)
                    if x == 1:
                        await msg.channel.send(c)
                    else:
                        await msg.channel.send(d)
            
            if 'dude stop' in msg.content or 'dickhead' in msg.content:
                await msg.channel.send(b)
            
            if 'fail' in msg.content or 'failure' in msg.content or 'not good enough' in msg.content:
                await msg.channel.send(e)
            
            if 'drugs' in msg.content:
                await msg.channel.send(f)
            
            if 'STUPID' in msg.content or 'you stupid' in msg.content or 'stupid' in msg.content or 'idiot' in msg.content:
                await msg.channel.send(g)
            
            if 'crying' in msg.content or 'stop crying' in msg.content:
                await msg.channel.send(h)
            
            if 'confusion' in msg.content or 'im confused' in msg.content or 'confused' in msg.content or 'heeehhhhhhhhhh' in msg.content:
                await msg.channel.send(i)
            
            if 'Chedbot, use threaten' in msg.content or 'chedbot use threaten' in msg.content or 'chedbot back me up' in msg.content or 'threaten em' in msg.content:
                await msg.channel.send(j)

            if '.steven' in msg.content:
                x = random.randint(1,10)
                if x == 1:
                        await msg.channel.send(a)
                elif x == 2:
                        await msg.channel.send(b)
                elif x == 3:
                        await msg.channel.send(c)
                elif x == 4:
                        await msg.channel.send(d)
                elif x == 5:
                        await msg.channel.send(e)
                elif x == 6:
                        await msg.channel.send(f)
                elif x == 7:
                        await msg.channel.send(g)
                elif x == 8:
                        await msg.channel.send(h)
                elif x == 9:
                        await msg.channel.send(i)
                elif x == 10:
                        await msg.channel.send(j)
                
            if 'insult' in msg.content:
                dj = ['Failure.',
                "You got straight back but no straight A's",
                'A = Average. You below average.',
                'I raised a doughnut',
                'I swam all the way from China for you to turn out like this...?!',
                'WHAT DA HELLL YOU SAY? FAILURE.',
                'Why you no like your cousin? He got 15 years work experience. Hes 9.',
                '*whips head around* TALK TO THE SLIPPER',
                'Oh you want to be actor? I tell you what i tell all aspiring actors: milk and 2 sugars in my latte.',
                'Why cant you be more cultured like your cousin? Timmy speaks six languages, only language you speak is FAILURE',
                'I thought you would be taller',
                'I will send you to jesus'
                ]
                embed=discord.Embed(description=f"'{random.choice(dj)}' - Steven's dad", color=discord.Color.dark_purple())
                await msg.channel.send(embed=embed)
                
def setup(client):
    client.add_cog(steven(client))
