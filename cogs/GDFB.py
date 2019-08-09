<<<<<<< HEAD
import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from config import token
import asyncio
import os
import random

class Example(commands.Cog):
    def __init__(self, client):
        self.client= client

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        role = discord.utils.get(ctx.guild.roles, name ="Creators")
        if role in ctx.author.roles:
            await member.kick(reason=reason)
            await ctx.send(f'{member.mention} has been kicked.')
        else:
            await ctx.send('You don\'t have the permissions to use that command')

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        role = discord.utils.get(ctx.guild.roles, name ="Creators")
        if role in ctx.author.roles:
            await member.ban(reason = reason)
            await ctx.send(f'{member.mention} has been banned.')
        else:
            await ctx.send('You don\'t have the permissions to use that command')

    @commands.command()
    async def gulag(self, ctx, member: discord.Member, *, reason=None):
        yikes = discord.utils.get(ctx.guild.roles, name="Creators")
        if yikes in ctx.author.roles:
            role = discord.utils.get(ctx.guild.roles, name='Gulag\'d')
            await member.add_roles(role)
            await ctx.send(f'{member.mention} has been gulaged.')
        else: 
            await ctx.send('You don\'t have the permissions to use that command')

    @commands.command()
    async def ungulag(self, ctx, member: discord.Member, *, reason=None):
        yikes = discord.utils.get(ctx.guild.roles, name ="Creators")
        if yikes in ctx.author.roles:
            role = discord.utils.get(ctx.guild.roles, name='Gulag\'d')
            await member.remove_roles(role)
            await ctx.send(f'{member.mention} has been ungulaged.')
        else:
            await ctx.send('You don\'t have the permissions to use that command')


def setup(client):
    client.add_cog(Example(client))

            


=======
import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from config import token
import asyncio
import os
import random

class Example(commands.Cog):
    def __iniit__(self, client):
        self.client= client

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        role = discord.utils.get(ctx.guild.roles, name ="Creators")
        if role in ctx.author.roles:
            await member.kick(reason=reason)
            await ctx.send(f'{member.mention} has been kicked.')
        else:
            await ctx.send('You don\'t have the permissions to use that command')

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        role = discord.utils.get(ctx.guild.roles, name ="Creators")
        if role in ctx.author.roles:
            await member.ban(reason = reason)
            await ctx.send(f'{member.mention} has been banned.')
        else:
            await ctx.send('You don\'t have the permissions to use that command')

    @commands.command()
    async def gulag(self, ctx, member: discord.Member, *, reason=None):
        yikes = discord.utils.get(ctx.guild.roles, name="Creators")
        if yikes in ctx.author.roles:
            role = discord.utils.get(ctx.guild.roles, name='Gulag\'d')
            await member.add_roles(role)
            await ctx.send(f'{member.mention} has been gulaged.')
        else: 
            await ctx.send('You don\'t have the permissions to use that command')

    @commands.command()
    async def ungulag(self, ctx, member: discord.Member, *, reason=None):
        yikes = discord.utils.get(ctx.guild.roles, name ="Creators")
        if yikes in ctx.author.roles:
            role = discord.utils.get(ctx.guild.roles, name='Gulag\'d')
            await member.remove_roles(role)
            await ctx.send(f'{member.mention} has been ungulaged.')
        else:
            await ctx.send('You don\'t have the permissions to use that command')

    @commands.command()
    async def k(self, ctx):
        message = await ctx.send('@everyone') 
        await ctx.message.delete()
        if ctx.message.content.startsWith('@everyone'):
            await ctx.message.delete
        

def setup(client):
        client.add_cog(Example(client))

            


>>>>>>> 8a6e62b2288342cba79f3033a17480ac4b735143
