import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from config import token
from config import place
import asyncio
import os
import random

client = commands.Bot(command_prefix = '&')
client.remove_command('help')
print(os.getcwd())
print(os.listdir('soundclips'))
for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
                client.load_extension(f'cogs.{filename[:-3]}')
@client.event
async def on_ready():
        print('It\'s alive!')

@client.command(pass_context=True, name="okso", help="ok so")
async def okso(ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('ok_so.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()

@client.command(pass_context=True)
async def bloodycomplex(ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(('bloody_complex.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()

@client.command(pass_context=True)
async def thicc(ctx):
        await ctx.send('乇乂ㄒ尺卂   ㄒ卄丨匚匚')
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('thicc.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()
@client.command(pass_context=True)
async def graph(ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('graph.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()
@client.command(pass_context=True)
async def tdong(ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('tdong.wav'), after=lambda e: print('done', e))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()
@client.command(pass_context=True)
async def president(ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('president'+ str(random.randint(1, 4)) + ".wav"))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()
@client.command(pass_context=True)
async def brainblast(ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('brainblast.wav'))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()
@client.command(pass_context=True)
async def racist(ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('racist.wav'))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()
@client.command(pass_context=True)
async def anarchy(ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('anarchy.wav'), after=lambda e: print('done', e))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()
@client.command(pass_context=True)
async def possible(ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('possible.mp3'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()

@client.command(pass_context=True)
async def uwu(ctx):
        if ctx.guild.id == (413059339138629632):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('uwu.mp3'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()
        else:
                await ctx.send("You can't use that command.")
@client.command(pass_context=True)
async def blunder(ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('blunder.wav'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()
@client.command()
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
        vc.play(discord.FFmpegPCMAudio('rats_birthday_mixtape.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()
@client.command()
async def believe(ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('cantbelieve.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()                 
@client.command()
async def cringe(ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('Cringe.wav'), after=lambda e: print('done', e))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()

@client.command()
async def hoesmad(ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('hoes mad.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()        

@client.command()
async def attention(ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('attention.mp3'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()

@client.command()
async def liz(ctx):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('liz.wav'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()        

client.run(token)