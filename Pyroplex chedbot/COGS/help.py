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
                embed=discord.Embed(description=f"**Hi there {msg.author.mention}! My command prefix is '.'**", color=discord.Color.magenta())
                embed.add_field(name='General commands:', value='``.help general``', inline=True)
                embed.add_field(name='Reddit commands:', value='``.help reddit``', inline=True)
                embed.add_field(name='Fun commands:', value='``.help fun``',inline=True)
                embed.add_field(name='Hypixel commands:', value='``.help hypixel``',inline=True)
                embed.add_field(name='Moderation commands:', value='``.help moderation``',inline=True)
                embed.add_field(name='``.README``', value='Also please run this when adding Chedbot to a server', inline=True)
                await msg.channel.send(embed=embed)
                
        if msg.content.startswith("."):

            if ".help general" in msg.content or '.Help general' in msg.content:
                embed=discord.Embed(title=f"***__General commands:__***", color=discord.Color.magenta())
                embed.add_field(name='``.Help``', value='Shows the list of commands', inline=True)
                embed.add_field(name='``.Ping``', value='Shows response time', inline=True)
                embed.add_field(name='``.Github``', value='Gives the Chedbot github link', inline=True)
                embed.add_field(name='``.Members``', value='Shows the servers member count', inline=True)
                embed.add_field(name='``.Support``', value='Shows a permanent link to the support/testing server', inline=True)
                embed.add_field(name='``.Avatar``', value='Shows the specified users avatar', inline=True)
                embed.add_field(name='``.Servers``', value='Shows how many servers chedbot is in', inline=True)
                embed.add_field(name='``.Times``', value='Displays the time for each member of Kingdom', inline=True)
                embed.add_field(name='``.README``', value='Run it!', inline=True)
                await msg.channel.send(embed=embed)
            
            if ".help fun" in msg.content or '.Help fun' in msg.content:
                embed=discord.Embed(title=f"***__Fun commands:__***", color=discord.Color.magenta())
                embed.add_field(name='``.8ball``', value='Let the divine ones answer your call!', inline=True)
                embed.add_field(name='``.Dad_joke``', value='Tells a dad joke!', inline=True)
                embed.add_field(name='``.Captain_Obvious``', value='Tells you an obvious fact!', inline=True)
                embed.add_field(name='``.Ship``', value='Ships two members of the server of your specification ;)', inline=True)
                embed.add_field(name='``.Smite``', value='By the power vested in me I SMITE YOU!', inline=True)
                embed.add_field(name='``.Quote``', value="Quotes a user, '.quote @user *insert quote*", inline=True)
                embed.add_field(name='``.Say``', value='Says a message back to you!', inline=True)
                embed.add_field(name='``.Coinflip``', value='Flip a coin!', inline=True)
                await msg.channel.send(embed=embed)
    
            if ".help reddit" in msg.content or '.Help reddit' in msg.content:
                embed=discord.Embed(title=f"***__Reddit commands:__***", color=discord.Color.magenta())
                embed.add_field(name='``.Meme``', value='Displays a fresh meme from r/memes', inline=True)
                embed.add_field(name='``.LPT``', value='Shows you a Life Pro Tip', inline=True)
                embed.add_field(name='``.Rminecraft``', value='Shows the latest post from r/minecraft', inline=True)
                embed.add_field(name='``.Mildly_interesting``', value='This command is mildly interesting...', inline=True)
                embed.add_field(name='``.CC``', value='Shows a cursed comment fom r/Cursed_Comments (:underage:)', inline=True)
                embed.set_footer(text='*NOTE - The reddit commands may take a while to load, please be patient :)')
                await msg.channel.send(embed=embed)

            if ".help moderation" in msg.content or '.Help moderation' in msg.content:
                embed=discord.Embed(title=f"***__Moderation commands:__***", color=discord.Color.magenta())
                embed.add_field(name='``.User``', value='Brings up information about a user', inline=True)
                embed.add_field(name='``.Purge``', value='Purge messages from the chat', inline=True)
                embed.add_field(name='``.Kick``', value='Kicks a player', inline=True)
                embed.add_field(name='``.Ban``', value='Bans a player', inline=True)
                embed.add_field(name='``.Unban``', value='Unbans a player', inline=True)
                embed.add_field(name='``.Dm_announce``', value='Sends a DM to everyone in the server', inline=True)
                embed.add_field(name='``.Dm``', value='Sends a DM to the specified user', inline=True)
                embed.add_field(name='``.Setup``', value='A command to run upon the bots entry to the server', inline=True)
                embed.add_field(name='``.Ticket``', value='Creates the message to make a ticket', inline=True) #to add to chedbot
                embed.add_field(name='``.Ticket``', value='Creates the message to make a ticket', inline=True) #to add to chedbot
                embed.add_field(name='``.Lock``', value='Locks the channel it is sent in', inline=True) #to add to chedbot
                embed.add_field(name='``.Unlock``', value='Unlocks the channel it is sent in', inline=True) #to add to chedbot
                embed.add_field(name='``.Lockdown``', value='Locks every channel in the server', inline=True) #to add to chedbot
                await msg.channel.send(embed=embed)

            if ".help hypixel" in msg.content or '.Help hypixel' in msg.content:
                embed=discord.Embed(title=f"***__Hypixel commands:__***", color=discord.Color.magenta())
                embed.add_field(name='``.kol``', value='Find out who in kingdom is online on hypixel', inline=True)
                embed.add_field(name='``.huser``', value="Look up a user's general hypixel stats", inline=True)
                embed.set_footer(text='*More hypixel commands coming soon! :)')
                await msg.channel.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))
