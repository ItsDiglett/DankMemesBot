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
                page1.add_field(name='amazin', value='says AMAZIN', inline=False)
                page1.add_field(name='stupid', value='says "You\'re not just wrong, you\'re stupid."', inline=False)
                page1.add_field(name='okso', value='says "ok so"', inline=False)
                page1.add_field(name='bringitoff', value='says "Let\'s be smart and bring it off"', inline=False)
                page1.add_field(name='beta', value='says "beta!"', inline=False)
                page1.add_field(name='bloodycomplex', value='says "That\'s so bloody complicated"', inline=False)
                page1.add_field(name='thicc', value='says "damn boi he thicc"', inline=False)
                page1.add_field(name='graph', value='says "look at this graph"', inline=False)
                page1.add_field(name='tdong', value='says "tdong"', inline=False)
                page1.add_field(name='claws', value='says "big meaty claws"\n \n **React with any emoji to see page 2**', inline=False)


                message = await channel.send(embed=page1)
                await self.client.wait_for('reaction_add')
                
                page2 = discord.Embed(
                        colour = discord.Colour.red()
                )

                page2.set_author(name='List of commands:')
                page2.add_field(name='president', value='says "i want to kill the president"', inline=False)
                page2.add_field(name='brainblast', value='says "brainblast"', inline=False)
                page2.add_field(name='racist', value='says "You can\'t say the n word"', inline=False)
                page2.add_field(name='anarchy', value='says "anarchy"', inline=False)
                page2.add_field(name='possible', value='says "it\'s entirely possible"', inline=False)
                page2.add_field(name='uwu', value='uWu', inline=False)
                page2.add_field(name='blunder', value='says "You commited one of the classic blunders"', inline=False)
                page2.add_field(name='rats', value='rats rats we are the rats', inline=False)
                page2.add_field(name='believe', value='says "I can\'t believe you\'ve done this"', inline=False)
                page2.add_field(name='cringe', value='says "cringe(7d clear)"', inline=False)
                page2.add_field(name='goodthing', value='says "that\'s a good thing"', inline=False)
                page2.add_field(name='liz', value='says "read theory"', inline=False)

                await channel.send(embed=page2)

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