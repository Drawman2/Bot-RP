import discord
from discord.ext import commands

import os
import dotenv

#On windows only:
dotenv.load_dotenv()

client = commands.Bot(command_prefix = "/")

#This is a decorator. It calls the following function within itself in
#order to execute code before and after.
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="/help"))
    print("Bot online and running...")

@client.command()

#The name of each function is the same as the command you want to have
#in Discord.
#ctx: read as "context". This is like an overview of the command. It
#contains informations about it and allows to send things on Discord.
async def ping(ctx):
    #latency is multiplied by 1000 because it was originally in seconds.
    await ctx.send("Pong! {}ms".format(round(client.latency * 1000)))

#This needs to be at the end
client.run(os.getenv("BOT_TOKEN"))