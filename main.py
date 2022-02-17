import nextcord
import os
from datetime import date, datetime, timedelta
from keep_alive import keep_alive
from nextcord.ext import commands
import logging
import pymongo
# import dns # did this once just to have the package installed leaving this note as a reminder in case I decide to rebuild this in another environment

logging.basicConfig(level=logging.INFO)

intents = nextcord.Intents.default()
intents.members = True
#To gather server members from whatever server the bot is in
#REQUIRES ENABLING "SERVER MEMBER INTENT" FROM THE discord DEVELOPER PORTAL

mongoCreds = os.environ['mongoAdminPass']
client = pymongo.MongoClient(
    f"mongodb+srv://admin:{mongoCreds}@brc.hsdnc.mongodb.net/brc?retryWrites=true&w=majority"
)
brc = client.brc
brc_users = brc.users

bot = commands.Bot(command_prefix="!")  #Change the prefix however you'd like


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f"The {extension} extension has been loaded")


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f"The {extension} extension has been unloaded")


@bot.command(aliases=['r'])
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f"The {extension} extension has been unloaded")
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f"The {extension} extension has been reloaded")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
#Loads every file in the cogs folder
#This will add the .py extension for you so do not do it yourself in the cogs table


@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Activity(
        type=nextcord.ActivityType.listening, name="any Humans."))
    print(f"{bot.user} is online!"
          )  #Checks when the bot is online and prints it to the console


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      mins = error.retry_after/int(60)
      await ctx.send(
          'Sorry, you wont be able to run that command for another  %.2f mins.'
          % mins)
    raise error


keep_alive()
bot.run(
    os.getenv("TOKEN")
)  #Runs the bot, I suggest NOT pasting your token in the string which is why I used the os import to get it through a SECRET TOKEN (Read the README.md for more info)

#If people get access to your token they can and probably will run yout bot with their code instead so ALWAYS USE ENV VARIABLES
