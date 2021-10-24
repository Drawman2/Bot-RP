import discord
from discord.ext import commands
from keep_alive import keep_alive

import os

#On windows only:
#import dotenv
#dotenv.load_dotenv()

#Gives access to members events.
intents = discord.Intents().all()

client = commands.Bot(command_prefix="/", intents=intents)
client.remove_command('help')

async def displayWelcome(member):
  channel = client.get_channel(901069733594546207)
  message = member.mention + ", vous pouvez faire votre fiche de personnage ici."
  await channel.send(message)

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

@client.command()
@commands.has_role("Modérateur")
async def clear(ctx, amount=10):
  await ctx.channel.purge(limit=amount+1)

@client.command()
async def welcome(ctx):
  await displayWelcome(ctx.author)

@client.command()
async def help(ctx):
  embed = discord.Embed(
    title = "Aide",
    description = "Essayez ces commandes :",
    colour = discord.Colour.gold()
  )
  embed.add_field(name="/help", value="Affiche ce message.", inline=False)
  embed.add_field(name="/ping", value="Affiche votre latence avec le serveur.", inline=False)
  embed.add_field(name="/clear <nombre de messages>", value="Supprime le nombre de message indiqués.", inline=False)
  await ctx.send(embed=embed)

#Mentions the player when they join to create a character.
@client.event
async def on_member_join(member):
  await displayWelcome(member)

keep_alive()
#This needs to be at the end
client.run(os.getenv("BOT_TOKEN"))