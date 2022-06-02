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

#para wanted this, so he can have it! (as long as he has admin WHICH HE DOESNT MWAHAHAHA)
class spam(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Dad online')
        guild = self.client.get_guild(913509940050665482)
        channel = guild.get_channel(915058380551376926)
        embed=discord.Embed(description=f'Dad status:\n ONLINE', color=discord.Color.blurple())
        await channel.send(embed=embed)
    
    #spam someone
    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def spam(self, ctx, user : discord.User):
        await ctx.message.delete()
        for i in range (1):
            try:
                for i in range (5):
                    await user.send(f'{ctx.author.name} wants you :)')
                await ctx.send(f"Successfully DMed user!")
                
            except:
                await ctx.send(f"Unsuccessfully DMed user, try again later.")
    @spam.error
    async def spam_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(description='Sorry, you are not allowed to use this command.', color=discord.Color.dark_blue())
            await ctx.send(embed=embed)
            
def setup(client):
    client.add_cog(spam(client))