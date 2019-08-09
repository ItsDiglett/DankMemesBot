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
        async def coochie(self, ctx):   
            channel = ctx.message.author.voice.channel
            server = ctx.message.guild.voice_client
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio('soundclips/coochie.wav'), after=lambda e: print('done', e))
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
            vc.play(discord.FFmpegPCMAudio('soundclips/bringitoff.wav'), after=lambda e: print('done', e))
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
            vc.play(discord.FFmpegPCMAudio('soundclips/claws1.wav'), after=lambda e: print('done', e))
            await asyncio.sleep(0.1)
            while vc.is_playing():
                await asyncio.sleep(0.1)
            vc.stop()
            await vc.disconnect()

        @commands.command(pass_context=True)
        async def harrass(self, ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/Sexual_Harrasment.mp3'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()


        @commands.command(pass_context=True)
        async def bloodycomplex(self,ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/bloody_complex.mp3'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()


        @commands.command(pass_context=True)
        async def president(self,ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/president'+ str(random.randint(1, 4)) + ".wav"))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()
        @commands.command(pass_context=True)
        async def brainblast(self,ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/brainblast.wav'))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()

        @commands.command(pass_context=True)
        async def notfunny(self,ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/notfunny.mp3'))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()

def setup(client):
        client.add_cog(Example(client))