import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from config import token
import asyncio
import os
import random


class Example(commands.Cog):
        def __iniit__(self,client):
                self.client=client

        #Contains Amazin, Beta, Racist, Anarchy, Possible


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


        @commands.command(pass_context=True)
        async def racist(ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/racist.wav'))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()
        @commands.command(pass_context=True)
        async def anarchy(ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/anarchy.wav'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()
        @commands.command(pass_context=True)
        async def possible(ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/possible.mp3'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()
        
        @commands.command()
        async def cringe(ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/Cringe.wav'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()


        @commands.command()
        async def liz(ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/liz.wav'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()


def setup(client):
        client.add_cog(Example(client))               