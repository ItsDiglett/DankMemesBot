import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from config import token
import asyncio
import os
import random

class Embed(commands.Cog):
        def __init__(self, client):
                self.client=client

        @commands.command(pass_context=True)
        async def help(self, ctx):
                author = ctx.message.author
                channel = ctx.message.channel
                
                page1 = discord.Embed(
                        colour = discord.Colour.red()
                )

                page1.set_author(name='List of commands:')
                page1.add_field(name='help', value='shows all commands', inline=False)
                page1.add_field(name='Jordan peterson', value='&okso and &bloodycomplex', inline=False)
                page1.add_field(name='Spongebob', value='&claws, &bringitoff, &coochie', inline=False)
                page1.add_field(name='JLP', value='&beta and &amazin', inline=False)
                page1.add_field(name='DiscordDoneLeft Memes', value='&tdong and &liz', inline=False)
                page1.add_field(name='Bernie', value='&goodthing and &yourwrong' inline=False)
                page1.add_field(name='WKUK', value='&president and &anarchy', inline=False)
                page1.add_field(name='Random Memes', value='&stupid, &possible, &racist, &believe, &thicc, &graph, \n &brainblast, &blunder, and &cringe', inline=False)
                page1.add_field(name='Songs', value='&rats and &uwu', inline=False)

                await channel.send(embed=page1)
               
        @commands.command()
        async def github(self, ctx):
                await ctx.send('Check out the github here: https://github.com/ItsDiglett/DankMemesBot ')
        

        #This tells the bot too fuck off from vc
        @commands.command(pass_context=True)
        async def leave(self, ctx):
                server = ctx.message.guild.voice_client
                await server.disconnect() 

def setup(client):
        client.add_cog(Embed(client))