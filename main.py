import discord
from discord.ext import commands

import os

client = commands.Bot(command_prefix = "/")

#This is a decorator. It calls the following function within itself in
#order to execute code before and after.
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="/help"))
    print("Bot online and running...")

client.run(os.get_dotenv(BOT_TOKEN))