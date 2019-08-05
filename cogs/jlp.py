import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from config import token
from config import place
from config import flusers
import asyncio
import os
import random


class Example(commands.Cog):
        def __iniit__(self,client):
                self.client=client

        @commands.command(pass_context=True)
        async def amazin(self, ctx):
            channel = ctx.message.author.voice.channel
            server = ctx.message.guild.voice_client
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio((place) + '/' + 'amazin'+ str(random.randint(1, 4)) + ".mp3")) 
            await asyncio.sleep(0.1)
            while vc.is_playing():
                    await asyncio.sleep(0.1)
            vc.stop()
            await vc.disconnect()

        @commands.command(pass_context=True, name="beta", help="beta")
        async def beta(self, ctx):
            channel = ctx.message.author.voice.channel
            server = ctx.message.guild.voice_client
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio((place) + '/' + 'beta'+ str(random.randint(1, 4)) + ".mp3"))
            await asyncio.sleep(0.1)
            while vc.is_playing():
                    await asyncio.sleep(0.1)
            vc.stop()
            await vc.disconnect()

def setup(client):
        client.add_cog(Example(client))               