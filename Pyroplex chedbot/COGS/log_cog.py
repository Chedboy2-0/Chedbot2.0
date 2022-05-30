#---STARTUP---#
import discord
from discord.ext import commands
from discord.ext import *
from discord.utils import time_snowflake
from discord.utils import *
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

class Msg_Log1(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logging online')
        guild = self.client.get_guild(913509940050665482)
        channel = guild.get_channel(915058380551376926)
        embed=discord.Embed(description=f'Logging status:\n ONLINE', color=discord.Color.dark_purple())
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, ctx, msg, *, member = discord.Member):
        channel = discord.utils.get(ctx.guild.channels, name="🦕｜bot-logs") #ensures the bot sends in the correct channel
        if msg.author.bot == False:
            if msg.content.startswith('.'): #logs if a command is used
                print(f'{msg.content} Used by {msg.author} in {msg.channel}, {msg.author.guild}')
                embed=discord.Embed(description=f'{msg.content} used by {msg.author} in {msg.channel}, {msg.author.guild}\nUsed at {msg.created_at.strftime("%a, %b %d %Y at %H:%M:%S %p")} UK TIME', color=discord.Color.dark_teal())
                await channel.send(embed=embed)

            #test command
            elif '!pong' in msg.content:
                await msg.channel.send('ping!')



def setup(client):
    client.add_cog(Msg_Log1(client))