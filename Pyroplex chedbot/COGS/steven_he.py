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
            
            if '.steven' in msg.content:
                x = random.randint(1,6)
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
                
                
def setup(client):
    client.add_cog(steven(client))