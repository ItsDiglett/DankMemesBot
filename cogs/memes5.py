import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from config import token
import asyncio
import os
import random
class Example(commands.Cog):
        def __init__(self,client):
            self.client=client
        
        @commands.command()
        async def d10(self, ctx):
            rand = random.randint(1,10)
            await ctx.send('You rolled a ' + str(rand) + '.')
        @commands.command()
        async def d12(self, ctx):
            rand = random.randint(1,12)
            await ctx.send('You rolled a ' + str(rand) + '.')
        @commands.command()
        async def d20(self, ctx):
            rand = random.randint(1,20)
            await ctx.send('You rolled a ' + str(rand) + '.')
        @commands.command()
        async def d8(self, ctx):
            rand = random.randint(1,8)
            await ctx.send('You rolled a ' + str(rand) + '.')
        @commands.command()
        async def d6(self, ctx):
            rand = random.randint(1,6)
            await ctx.send('You rolled a ' + str(rand) + '.')
        @commands.command()
        async def d4(self,ctx):
            rand = random.randint(1,4)
            await ctx.send('You rolled a ' + str(rand) + '.')

def setup(client):
        client.add_cog(Example(client))