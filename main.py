import discord

from discord.ext import commands

client = commands.Bot(command_prefix='/')

@client. command()
async def ping(ctx):
    await ctx. send("Pong!")

client.run('ODk5NDY1OTE4MTMwODI3MzE1.YWzK6g.QcxvSYCgWdHVeZQ4b9vOmVoWBbw')