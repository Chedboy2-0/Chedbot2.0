#---STARTUP---#
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

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Help online')
        guild = self.client.get_guild(913509940050665482)
        channel = guild.get_channel(915058380551376926)
        embed=discord.Embed(description=f'Help status:\n ONLINE', color=discord.Color.dark_orange())
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, msg, *, member = discord.Member):
            #test command
            if '!yesyes' in msg.content:
                await msg.channel.send('ping!')

        
    @commands.Cog.listener()
    async def on_message(self, msg):
        if '<@!914569343831015476>' in msg.content or '.Help' in msg.content:
                embed=discord.Embed(description=f"**Hi there {msg.author.mention}! My command prefix is '.'** \n\n **For the general commands type** ``.help general``\n\n **For the fun commands type** ``.help fun``\n\n **For the reddit commands type** ``.help reddit``\n\n **For the moderation commands type** ``.help moderation``", color=discord.Color.magenta())
                await msg.channel.send(embed=embed)
                
        if msg.content.startswith("."):

            if ".help general" in msg.content or '.Help general' in msg.content:
                embed=discord.Embed(description=f"***__General commands:__*** \n\n **Help** - shows the list of commands \n **Ping** - shows response time \n **Members** - Shows the servers member count \n **Support** - Shows a permanent invite link to the support/testing server\n **Avatar** - Shows the specified users avatar \n **Servers** - Shows how many servers the bot is in", color=discord.Color.magenta())
                await msg.channel.send(embed=embed)
            
            if ".help fun" in msg.content or '.Help fun' in msg.content:
                embed=discord.Embed(description=f"***__Fun commands:__*** \n\n **8ball** - Type '.8ball' then your question and let the divine ones answer! \n **dad_joke** - Tells a dad joke! \n **Captain_Obvious** - Tells you an obvious fact\n **Ship** - Ships two members of the server of your specification ;)\n **Smite** - 'By the power vested in me I SMITE YOU' \n **Quote** - Quotes a user, '.quote @user *insert quote*' \n **Say** - Says a message back to you \n **Coinflip** - Flip a coin!", color=discord.Color.magenta())
                await msg.channel.send(embed=embed)
    
            if ".help reddit" in msg.content or '.Help reddit' in msg.content:
                embed=discord.Embed(description=f"***__Reddit commands:__*** \n\n **meme** - Displays a fresh meme from r/memes \n **lpt** - Shows you a Life Pro Tip \n **rminecraft** - Shows the latest post from r/minecraft\n **mildly_interesting** - This command is mildly interesting...", color=discord.Color.magenta())
                await msg.channel.send(embed=embed)

            if ".help moderation" in msg.content or '.Help moderation' in msg.content:
                embed=discord.Embed(description=f"***__Moderation commands:__*** \n\n  **User** - brings up information about a user \n **Purge** - Requires manage messages permissions, '.purge number of messages to be deleted \n **Kick** - Requires kick members permissions, '.kick @member '\n **Ban** - Requires ban players permissions, '.ban @member  '\n **Unban** - Requires ban players permissions, '.unban @member#number ' \n **dm_announce** - Sends a DM to everyone in the server \n **dm** - Sends a DM to the specified user", color=discord.Color.magenta())
                await msg.channel.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))