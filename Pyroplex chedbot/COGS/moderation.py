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

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderation online')
        guild = self.client.get_guild(913509940050665482)
        channel = guild.get_channel(915058380551376926)
        embed=discord.Embed(description=f'Moderation status:\n ONLINE', color=discord.Color.dark_red())
        await channel.send(embed=embed)

    #test msg
    @commands.Cog.listener()
    async def on_message(self, msg, *, member = discord.Member):
            if '!test' in msg.content:
                await msg.channel.send('test')
                
    #user info
    @commands.command(aliases=['user','info'])
    @commands.has_permissions(kick_members=True)
    async def whois(self, ctx, member : discord.Member):
        embed = discord.Embed(title = f'{member.name} \n', discription = f'{member.mention}', color = discord.Color.dark_red())
        embed.add_field(name = "User", value = member.mention, inline=False)
        embed.add_field(name = "Join date", value = member.joined_at.strftime("%a, %b %d %Y at %H:%M:%S %p"), inline=False)
        embed.add_field(name = "ID", value = member.id, inline=True)
        embed.add_field(name = "Status", value = member.activity, inline=True)
        embed.add_field(name = "Top role", value = member.top_role.mention, inline=True)
        embed.add_field(name = "User", value = member._user, inline=True)
        embed.add_field(name = "Account created at:", value = member.created_at.strftime("%a, %b %d %Y at %H:%M:%S %p"), inline=False)
        embed.set_thumbnail(url = member.avatar_url)
        embed.set_footer(icon_url= ctx.author.avatar_url, text = f'Requested by {ctx.author.name}')
        await ctx.send(embed=embed)
    @whois.error
    async def whois_error(self, ctx, error, member = discord.Member):
        if isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(description='Sorry, you are not allowed to use this command.', color=discord.Color.dark_blue())
            await ctx.send(embed=embed)
    
    # Lock Channel
    @commands.command(aliases=['Lock'])
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx, reason=None):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        embed=discord.Embed(title=f'Channel Locked', description=f'🔒 #{ctx.channel.name} has been locked.\nCode ripped off from Jedi :(', color=discord.Color.blue())
        await ctx.send(embed=embed)
        channel = discord.utils.get(ctx.guild.channels, name="🦕｜bot-logs")
        embed=discord.Embed(title=f'Channel locked', color=discord.Color.dark_blue())
        embed.add_field(name='Channel name:', value=ctx.channel.mention, inline=False)
        embed.add_field(name='Used by:', value=ctx.author.mention, inline=False)
        await channel.send(embed=embed)
    @lock.error
    async def lock_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(description='You are not allowed to use this command.', color=discord.Color.red())
            await ctx.channel.send (embed=embed)

    # Unlock Channel
    @commands.command(aliases=['Unlock'])
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx,):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        embed=discord.Embed(title=f'Channel Unlocked', description=f'🔓 #{ctx.channel.name} has been unlocked.\nCode ripped off from Jedi :(', color=discord.Color.blue())
        await ctx.channel.send(embed=embed)
        channel = discord.utils.get(ctx.guild.channels, name="🦕｜bot-logs")
        embed=discord.Embed(title=f'Channel unlocked', color=discord.Color.dark_blue())
        embed.add_field(name='Channel name:', value=ctx.channel.mention, inline=False)
        embed.add_field(name='Used by:', value=ctx.author.mention, inline=False)
        await channel.send(embed=embed)
    @unlock.error
    async def unlock_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(description='You are not allowed to use this command.', color=discord.Color.red())
            await ctx.channel.send (embed=embed)

    #setup
    commands.command(aliases=['Setup'])
    @commands.has_permissions(manage_messages=True)
    async def setup(self,ctx):
        guild = ctx.message.guild
        overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True)
        }

        await guild.create_text_channel(name ='🦕｜bot-logs', overwrites=overwrites)
    

    #purge
    @commands.command(aliases=['Purge'])
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=0):
        await ctx.channel.purge(limit= amount+1)
    #bot logs
        if amount>1:
            channel = discord.utils.get(ctx.guild.channels, name="🦕｜bot-logs")
            embed=discord.Embed(description=f'Purge used by {ctx.author.mention} in #{ctx.channel.name} \nPurged {amount} messages', color=discord.Color.dark_blue())
            await channel.send(embed=embed)
    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(description='Sorry, you are not allowed to use this command.', color=discord.Color.dark_blue())
            await ctx.send(embed=embed)

    #kick
    @commands.command(aliases=['Kick'])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
    #bot logs
        channel = discord.utils.get(ctx.guild.channels, name="🦕｜bot-logs")
        embed=discord.Embed(description=f'**__Kick used__** \n***Kicked*** {member.mention}\n**__Reason__**: {reason}\n**Used by** {ctx.author.mention}', color=discord.Color.dark_blue())
        await channel.send(embed=embed)
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(description='Sorry, you are not allowed to use this command.', color=discord.Color.dark_blue())
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description="Sorry, you are not allowed to kick this user.\nOr you haven't inputted this right", color=discord.Color.dark_blue())
            await ctx.send(embed=embed)


    #ban
    @commands.command(aliases=['Ban'])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
    #bot logs
        channel = discord.utils.get(ctx.guild.channels, name="🦕｜bot-logs")
        embed=discord.Embed(description=f'**__Ban used__** \n***Banned*** {member.mention}\n**__Reason__**: {reason}\n**Used by** {ctx.author.mention}', color=discord.Color.dark_blue())
        await channel.send(embed=embed)
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(description='Sorry, you are not allowed to use this command.', color=discord.Color.dark_blue())
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description='Sorry, you are not allowed to ban this user.', color=discord.Color.dark_blue())
            await ctx.send(embed=embed)

    #unban
    @commands.command(aliases=['Unban'])
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member : discord.Member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {member}')
                return

    #dm all
    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def dm_announce(self, ctx, *, message):
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                await user.send(message)
                await ctx.send(f"Successfully DMed users!")
            except:
                await ctx.send(f"Unsuccessfully DMed users, try again later.")
    @dm_announce.error
    async def dm_announce_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(description='Sorry, you are not allowed to use this command.', color=discord.Color.dark_blue())
            await ctx.send(embed=embed)

    #dm specfic
    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def dm(self, ctx, user : discord.User, *, message):
        await ctx.message.delete()
        for i in range (1):
            try:
                await user.send(message)
                await ctx.send(f"Successfully DMed user!")
            except:
                await ctx.send(f"Unsuccessfully DMed user, try again later.")
    @dm.error
    async def dm_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(description='Sorry, you are not allowed to use this command.', color=discord.Color.dark_blue())
            await ctx.send(embed=embed)




def setup(client):
    client.add_cog(Moderation(client))
