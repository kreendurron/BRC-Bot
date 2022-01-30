import discord
import json
import sys
from datetime import date
from discord.ext import commands
#Don't Remove this import, you need it
import random
sys.path.insert(0,'./utils/misc')
from randStuff import randEncouragments

import aiohttp
import asyncio



# // DEFINE THE COG CLASS
class Plan2(commands.Cog): #Declares a cog name
  """Commands that will display the reading plan.""" #Description of cog

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  # // ON READY EVENT
  @commands.Cog.listener()
  async def on_ready(self):
    print('The Plan2 Cog is locked, loaded and ready.')      
  
  # // DAILY READING PLAN
  @commands.command()
  async def v2(self,ctx: commands.context):
    results = []
    
    async with aiohttp.ClientSession() as session:
      response = await session.get(f'https://bible-api.com/romans+12?translation=kjv', ssl=False)
      results.append(await response.json())
      await ctx.send(results[0]['verses'][0])
  

# DO NOT REMOVE! #
def setup(bot: commands.Bot):
  bot.add_cog(Plan2(bot))
# DO NOT REMOVE! OR PLACE ANYTHING BELOW! #