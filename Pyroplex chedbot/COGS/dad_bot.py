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

#fun thing to muck around with, adds dad-bot functionality
class dad_bot(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Dad online')
        guild = self.client.get_guild(913509940050665482)
        channel = guild.get_channel(915058380551376926)
        embed=discord.Embed(description=f'Dad status:\n ONLINE', color=discord.Color.blurple())
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, msg, *, member = discord.Member):
            #test command
            if '!yesyesyes' in msg.content:
                await msg.channel.send('ping!')

        
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author.bot == False: #ensures it doesnt perma loop
            if "im" in msg.content or "I'm" in msg.content or "Im" in msg.content:
                 # store arguments in x, excluding the first element (!rip)
                x = msg.content.split(" ",)
                await msg.channel.send(f'Hey {x}, Im Dad!')
            
def setup(client):
    client.add_cog(dad_bot(client))