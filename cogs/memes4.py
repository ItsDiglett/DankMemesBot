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
        def __init__(self,client):
                self.client=client


        @commands.command()
        async def nice(self, ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/nice.mp3'))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()

        @commands.command()
        async def skype(self, ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/twomad.mp3'))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()

        @commands.command(pass_context=True)
        async def thicc(self, ctx):
                await ctx.send('乇乂ㄒ尺卂   ㄒ卄丨匚匚')
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/thicc.mp3'))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()
        @commands.command(pass_context=True)
        async def graph(self, ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/graph.mp3'))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()
        @commands.command(pass_context=True)
        async def tdong(self, ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/tdong.wav'))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()
def setup(client):
=======
import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from config import token
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


        @commands.command(pass_context=True)
        async def skype(ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/twomad.mp3'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()

        @commands.command(pass_context=True)
        async def thicc(ctx):
                await ctx.send('乇乂ㄒ尺卂   ㄒ卄丨匚匚')
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/thicc.mp3'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()
        @commands.command(pass_context=True)
        async def graph(ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/graph.mp3'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()
        @commands.command(pass_context=True)
        async def tdong(ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/tdong.wav'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()
def setup(client):
>>>>>>> 8a6e62b2288342cba79f3033a17480ac4b735143
        client.add_cog(Example(client))