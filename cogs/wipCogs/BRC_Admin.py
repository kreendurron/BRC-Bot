import discord
# from datetime import date, datetime, timedelta
from discord.ext import commands


# // END IMPORTS

# // DEFINE THE COG CLASS
class BRC_Admin(commands.Cog):  #Declares a cog name
  """Admin Commands for The Bible Reading Challenge"""  #Description of cog

  def __init__(self, bot: commands.bot):
      self.bot = bot
      self.brcusers = bot.brc_users

  # // ON READY COMMAND
  @commands.Cog.listener()
  async def on_ready(self):
      print('The BRC_Admin Cog is locked, loaded and ready.')

    

# DO NOT REMOVE! #
   
# // ON READY COMMAND
async def setup(bot):
  await bot.add_cog(BRC_Admin(bot))
  
# DO NOT REMOVE! OR PLACE ANYTHING BELOW! #
