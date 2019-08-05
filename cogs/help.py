import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from config import token
from config import place
from config import flusers
import asyncio
import os
import random
import youtube_dl

class Example(commands.Cog):
        def __iniit__(self,client):
                self.client=client

        @commands.command()
        async def github(self, ctx):
                await ctx.send('Check out the github here: https://github.com/ItsDiglett/DankMemesBot ')

        @commands.command(pass_context=True)
        async def help(self, ctx):
                author = ctx.message.author
                channel = ctx.message.channel
            
                embed = discord.Embed(
                        colour = discord.Colour.red()
                )

                embed.set_author(name='List of commands:')
                embed.add_field(name='help/help2', value='shows all commands', inline=False)
                embed.add_field(name='amazin', value='says AMAZIN', inline=False)
                embed.add_field(name='stupid', value='says "You\'re not just wrong, you\'re stupid."', inline=False)
                embed.add_field(name='methode', value='says "FBI OPEN UP"', inline=False)
                embed.add_field(name='methode2', value='says "I invoke my fifth amendment privilege"', inline=False)
                embed.add_field(name='methode3', value='says some yikesy shit', inline=False)
                embed.add_field(name='okso', value='says "ok so"', inline=False)
                embed.add_field(name='bringitoff', value='says "Let\'s be smart and bring it off"', inline=False)
                embed.add_field(name='beta', value='says "beta!"', inline=False)
                embed.add_field(name='bloodycomplex', value='says "That\'s so bloddy complicated"', inline=False)
                embed.add_field(name='thicc', value='says "damn boi he thicc"', inline=False)
                embed.add_field(name='graph', value='says "look at this graph"', inline=False)
                embed.add_field(name='tdong', value='says "tdong"', inline=False)
                embed.add_field(name='claws', value='says "big meaty claws"', inline=False)


                await channel.send(embed=embed)


        @commands.command(pass_context=True)
        async def help2(self, ctx):
                author = ctx.message.author
                channel = ctx.message.channel

                embed = discord.Embed(
                        colour = discord.Colour.red()
                )

                embed.set_author(name='List of commands(cont.)')
                embed.add_field(name='president', value='says "i want to kill the president"', inline=False)
                embed.add_field(name='brainblast', value='says "brainblast"', inline=False)
                embed.add_field(name='racist', value='says "You can\'t say the n word"', inline=False)
                embed.add_field(name='anarchy', value='says "anarchy"', inline=False)
                embed.add_field(name='possible', value='says "it\'s entirely possible"', inline=False)
                embed.add_field(name='uwu', value='uWu', inline=False)
                embed.add_field(name='blunder', value='says "You commited one of the classic blunders"', inline=False)
                embed.add_field(name='rats', value='rats rats we are the rats', inline=False)
                embed.add_field(name='believe', value='says "I can\'t believe you\'ve done this"', inline=False)
                embed.add_field(name='cringe', value='says "cringe(7d clear)"', inline=False)
                embed.add_field(name='goodthing', value='says "that\'s a good thing"', inline=False)
                embed.add_field(name='liz', value='says "read theory"', inline=False)

                await ctx.channel.send(embed=embed)



        #This tells the bot too fuck off from vc
        @commands.command(pass_context=True)
        async def leave(self, ctx):
                server = ctx.message.guild.voice_client
                await server.disconnect() 

def setup(client):
        client.add_cog(Example(client))