import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from config import token
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

#Directory
        #Memes1: okso, believe, rats
        #Memes2: bernie, hoesmad, attention, uwu, blunder
        #Memes3: amazin, beta, racist, anarchy, possible
        #Memes4: methode, skype, thicc, graph, tdong 
        #Memes5: roll commands
        #Memes6: spongebob, harrass, bloody complex, brainblast, president    

client.run(token)