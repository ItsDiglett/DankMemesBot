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
    async def methode(self, ctx):                
        channel = ctx.message.author.voice.channel
        server = ctx.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio((place) + '/' + 'methode.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()  

    @commands.command()
    async def methode2(self, ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio((place) + '/' + 'methode.wav'))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()

    @commands.command(pass_context=True)
    async def methode3(self, ctx):
            if ctx.guild.id == (413059339138629632) or ctx.message.author.id == (admin):
                    channel = ctx.message.author.voice.channel
                    server = ctx.voice_client
                    vc = await channel.connect()
                    vc.play(discord.FFmpegPCMAudio((place) + '/' + 'methode3.wav'), after=lambda e: print('done', e))
                    await asyncio.sleep(0.1)
                    while vc.is_playing():
                            await asyncio.sleep(0.1)
                    vc.stop()
                    await vc.disconnect()

            else:
                    await ctx.send("You can't use that.")
def setup(client):
        client.add_cog(Example(client))