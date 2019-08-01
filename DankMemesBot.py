import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from config import token
from config import place
import asyncio
import os

client = commands.Bot(command_prefix = '&')
print(os.getcwd())
client.remove_command('help')

for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
                client.load_extension(f'cogs.{filename[:-3]}')

@client.command(pass_context=True)
async def amazin(ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio((place) + '/' + 'amazin'+ str(random.randint(1, 4)) + ".mp3")) 
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()

@client.command(pass_context=True, name="okso", help="ok so")
async def okso(ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio((place) + '/' + 'ok_so.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()
@client.command(pass_context=True)
async def bringitoff(ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio((place) + '/' + 'bringitoff.wav'), after=lambda e: print('done', e))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()
@client.command(pass_context=True, name="beta", help="beta")
async def beta(ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio((place) + '/' + 'beta'+ str(random.randint(1, 4)) + ".mp3"))
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
        vc.play(discord.FFmpegPCMAudio((place) + '/' + 'bloody_complex.mp3'), after=lambda e: print('done', e))
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
        vc.play(discord.FFmpegPCMAudio((place) + '/' + 'thicc.mp3'), after=lambda e: print('done', e))
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
        vc.play(discord.FFmpegPCMAudio((place) + '/' + 'graph.mp3'), after=lambda e: print('done', e))
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
        vc.play(discord.FFmpegPCMAudio((place) + '/' + 'tdong.wav'), after=lambda e: print('done', e))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()
@client.command(pass_context=True)
async def claws(ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio((place) + '/' + 'claws1.wav'), after=lambda e: print('done', e))
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
        vc.play(discord.FFmpegPCMAudio((place) + '/' + 'president'+ str(random.randint(1, 4)) + ".wav"))
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
        vc.play(discord.FFmpegPCMAudio((place) + '/' + 'brainblast.wav'))
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
        vc.play(discord.FFmpegPCMAudio((place) + '/' + 'racist.wav'))
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
        vc.play(discord.FFmpegPCMAudio((place) + '/' + 'anarchy.wav'), after=lambda e: print('done', e))
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
                vc.play(discord.FFmpegPCMAudio((place) + '/' + 'possible.mp3'), after=lambda e: print('done', e))
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
                vc.play(discord.FFmpegPCMAudio((place) + '/' + 'uwu.mp3'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()
        else:
                await ctx.send("You can't use that command.")

@client.command(pass_context=True)
async def blunder(ctx):
                print(rand)
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio((place) + '/' + 'blunder.wav'), after=lambda e: print('done', e))
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
        vc.play(discord.FFmpegPCMAudio((place) + '/' + 'rats_birthday_mixtape.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()
@client.command()
async def believe(ctx):
                print(rand)
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio((place) + '/' + 'cantbelieve.mp3'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()                 
@client.command()
async def cringe(ctx):
                print(rand)
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio(r(place) + '/' + 'Cringe.wav'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()
@client.command()
async def goodthing(ctx):

                print(rand)  
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio((place) + '/' +'goodthing.wav'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()            
@client.command()
async def coochie(ctx):
                print(rand)
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio((place) + '/' + 'coochie.wav'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()
@client.command()
async def attention(ctx):
                print(rand)
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio((place) + '/' + 'attention.mp3'), after=lambda e: print('done', e))
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
                vc.play(discord.FFmpegPCMAudio((place) + '/' + 'liz.wav'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()        
@client.command()
async def d10(ctx):
        rand = random.randint(1,10)
        await ctx.send('You rolled a ' + str(rand) + '.')

#This tells the bot too fuck off from vc
@client.command(pass_context=True)
async def leave(ctx):
        server = ctx.message.guild.voice_client
        await server.disconnect()

client.run(token)
