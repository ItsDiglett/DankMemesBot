import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from config import token
from config import place
from config import admin
import asyncio
import os
import random
import youtube_dl

class Example(commands.Cog):
        def __iniit__(self,client):
                self.client=client

        @commands.command()
        async def coochie(self, ctx):   
            channel = ctx.message.author.voice.channel
            server = ctx.message.guild.voice_client
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio((place) + '/' + 'coochie.wav'), after=lambda e: print('done', e))
            await asyncio.sleep(0.1)
            while vc.is_playing():
                await asyncio.sleep(0.1)
            vc.stop()
            await vc.disconnect()       

        @commands.command(pass_context=True)
        async def bringitoff(self, ctx):
            channel = ctx.message.author.voice.channel
            server = ctx.message.guild.voice_client
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio((place) + '/' + 'bringitoff.wav'), after=lambda e: print('done', e))
            await asyncio.sleep(0.1)
            while vc.is_playing():
                await asyncio.sleep(0.1)
            vc.stop()
            await vc.disconnect()

        @commands.command(pass_context=True)
        async def claws(self, ctx):
            channel = ctx.message.author.voice.channel
            server = ctx.message.guild.voice_client
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio((place) + '/' + 'claws1.wav'), after=lambda e: print('done', e))
            await asyncio.sleep(0.1)
            while vc.is_playing():
                await asyncio.sleep(0.1)
            vc.stop()
            await vc.disconnect()

def setup(client):
        client.add_cog(Example(client))