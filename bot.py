import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():

    await client.change_presence(status=discord.status.online)
    await client.change_presence(activity=discord.Game(name="게임 하는중"))

    print("bird bot:",client.user.name,"#4622:",client.user.id,"1.0.0:",discord.__version__)


    client.run(os.environ['token'])