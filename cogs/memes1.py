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
        async def narcissism(ctx):
                await ctx.send('https://en.wikipedia.org/wiki/Narcissism_of_small_differences')

        @commands.command(pass_context=True)
        async def piss(self, ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/piss.wav'))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()
        
                            
        @commands.command(pass_context=True, name="okso", help="ok so")
        async def okso(self, ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/ok_so.mp3'))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()

        @commands.command()
        async def rats(self, ctx):
                await ctx.send("""```md
        Rats, rats, we are the rats.
        Celebrating yet another birthday bash.
        <MICHAEL> it's your birthday today.
        Cake and ice cream is on its way.
        and <MICHAEL> been such a good boy this year.
        Open up your gifts while we all cheer.```""")
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/rats_birthday_mixtape.mp3'))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()
        @commands.command()
        async def believe(self, ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/cantbelieve.mp3'))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()
                
        @commands.command()
        async def gotcha(self, ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/gotcha.mp3'))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()
                
        @commands.command()
        async def here(self, ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/here.wav'))
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

class Example(commands.Cog):
        def __iniit__(self,client):
                self.client=client

        @commands.command(pass_context=True, name="okso", help="ok so")
        async def okso(ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/ok_so.mp3'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()

        @commands.command()
        async def rats(ctx):

                await ctx.send("""```md
        Rats, rats, we are the rats.
        Celebrating yet another birthday bash.
        <MICHAEL> it's your birthday today.
        Cake and ice cream is on its way.
        and <MICHAEL> been such a good boy this year.
        Open up your gifts while we all cheer.```""")
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/rats_birthday_mixtape.mp3'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()
        @commands.command()
        async def believe(ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('soundclips/cantbelieve.mp3'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()                 
def setup(client):
>>>>>>> 8a6e62b2288342cba79f3033a17480ac4b735143
        client.add_cog(Example(client))