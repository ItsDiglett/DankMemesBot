import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
import random
import ffmpeg
import asyncio
import os

client = commands.Bot(command_prefix = '&')
print(os.getcwd())
client.remove_command('help')

#Shows the bot is ready
@client.event
async def on_ready():
    print('Keem is Ready')

@client.command(pass_context=True)
async def amazin(ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(r'C:\Users\Gaming\Desktop\meme bot\amazin'+ str(random.randint(1, 4)) + ".mp3")) 
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()
@client.command(pass_context=True)
async def stupid(ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(r'stupid.wav'), after=lambda e: print('done', e))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()
@client.command(pass_context=True)
async def methode3(ctx):
        if ctx.guild.id == (413059339138629632):
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio(r'methode3.wav'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()

        else:
                await ctx.send("You can't use that.")
@client.command(pass_context=True, name="okso", help="ok so")
async def okso(ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(r'C:\Users\Gaming\Desktop\meme bot\ok_so.mp3'), after=lambda e: print('done', e))
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
        vc.play(discord.FFmpegPCMAudio(r'bringitoff.wav'), after=lambda e: print('done', e))
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
        vc.play(discord.FFmpegPCMAudio(r'C:\Users\Gaming\Desktop\meme bot\beta'+ str(random.randint(1, 4)) + ".mp3"))
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
        vc.play(discord.FFmpegPCMAudio(r'C:\Users\Gaming\Desktop\meme bot\bloody_complex.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()
@client.command()
async def methode2(ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(r'methode.wav'))
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
        vc.play(discord.FFmpegPCMAudio(r'thicc.mp3'), after=lambda e: print('done', e))
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
        vc.play(discord.FFmpegPCMAudio(r'C:\Users\Gaming\Desktop\meme bot\graph.mp3'), after=lambda e: print('done', e))
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
        vc.play(discord.FFmpegPCMAudio(r'tdong.wav'), after=lambda e: print('done', e))
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
        vc.play(discord.FFmpegPCMAudio(r'claws1.wav'), after=lambda e: print('done', e))
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
        vc.play(discord.FFmpegPCMAudio(r'president'+ str(random.randint(1, 4)) + ".wav"))
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
        vc.play(discord.FFmpegPCMAudio(r'brainblast.wav'))
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
        vc.play(discord.FFmpegPCMAudio(r'racist.wav'))
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
                vc.play(discord.FFmpegPCMAudio(r'anarchy.wav'), after=lambda e: print('done', e))
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
                vc.play(discord.FFmpegPCMAudio(r'C:\Users\Gaming\Desktop\meme bot\possible.mp3'), after=lambda e: print('done', e))
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
                vc.play(discord.FFmpegPCMAudio(r'C:\Users\Gaming\Desktop\meme bot\uwu.mp3'), after=lambda e: print('done', e))
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
                vc.play(discord.FFmpegPCMAudio(r'blunder.wav'), after=lambda e: print('done', e))
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
        vc.play(discord.FFmpegPCMAudio(r'C:\Users\Gaming\Desktop\meme bot\rats_birthday_mixtape.mp3'), after=lambda e: print('done', e))
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
                vc.play(discord.FFmpegPCMAudio(r'C:\Users\Gaming\Desktop\meme bot\cantbelieve.mp3'), after=lambda e: print('done', e))
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
                vc.play(discord.FFmpegPCMAudio(r'Cringe.wav'), after=lambda e: print('done', e))
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
                vc.play(discord.FFmpegPCMAudio(r'goodthing.wav'), after=lambda e: print('done', e))
                await asyncio.sleep(0.1)
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
                await vc.disconnect()
@client.command()
async def methode(ctx):
                print(rand)                
                channel = ctx.message.author.voice.channel
                server = ctx.message.guild.voice_client
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio(r'methode.mp3'), after=lambda e: print('done', e))
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
                vc.play(discord.FFmpegPCMAudio(r'coochie.wav'), after=lambda e: print('done', e))
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
                vc.play(discord.FFmpegPCMAudio(r'C:\Users\Gaming\Desktop\meme bot\attention.mp3'), after=lambda e: print('done', e))
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
                vc.play(discord.FFmpegPCMAudio(r'liz.wav'), after=lambda e: print('done', e))
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


#@client.command(pass_context=True)
#async def tony(ctx):
        #await ctx.send("""you may not like it, but this is peak human performance. this is the ideal human body:
#https://cdn.discordapp.com/attachments/418850379518705675/527371989300805642/unknown.png
#https://cdn.discordapp.com/attachments/418850379518705675/527371997517316118/unknown.png
#https://cdn.discordapp.com/attachments/418850379518705675/527372006866550806/unknown.png
#https://cdn.discordapp.com/attachments/418850379518705675/527372859782332426/unknown.png
#https://cdn.discordapp.com/attachments/418850379518705675/527372895807340560/unknown.png""")


client.run('TOKEN')
