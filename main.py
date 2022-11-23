import discord
import os

from discord.ext import commands
from discord import app_commands

import pymongo

class Bot(commands.Bot):
  def __init__(self):  
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    super().__init__(command_prefix = "!",  intents = intents)

  async def setup_hook(self):
    await self.tree.sync(guild = discord.Object(id = os.getenv("my_guild_id")))
    print(f"Synced slash commands for {self.user}")
  
  async def on_command_error(self, ctx, error):
    await ctx.reply(error, ephemeral = True)
  

bot = Bot()

@bot.hybrid_command(name= "test", with_app_command = True, description = "Testing")
@app_commands.guilds(discord.Object(id = os.getenv("my_guild_id")))
@commands.has_permissions(administrator = True)
async def test(ctx: commands.Context):
  await ctx.defer(ephemeral = True)
  await ctx.reply('Hi!')
  
    
# /// MONGO DB
mongoCreds = os.environ['mongoAdminPass']
client = pymongo.MongoClient(
    f"mongodb+srv://admin:{mongoCreds}@brc.hsdnc.mongodb.net/brc?retryWrites=true&w=majority"
)
brc = client.brc
brc_users = brc.users

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name="any Humans."))
    print(f"{bot.user} is online!"
          )  #Checks when the bot is online and prints it to the console

 

# ----------
bot.run(os.getenv("TOKEN"))