import nextcord
import random
import asyncio
from replit import db
import datetime
from datetime import date, datetime, timedelta
from nextcord.ext import commands
#Don't Remove this import, you need it
today = date.today()
# print("Today's date:", today)

# // TIME STUFF
day = today.strftime("%d")
# print("day =", day)
month = today.strftime("%B")
# print("month =", month)
year = today.strftime("%y")
# print("year =", year)

# // DEFINE THE COG CLASS
class BRC_ADMIN(commands.Cog): #Declares a cog name
  """Admin Role Commands for The Bible Reading Challenge""" #Description of cog

  def __init__(self, bot: commands.Bot):
    self.bot = bot
    self.users = db['users']
    
  
  # // ON READY COMMAND
  @commands.Cog.listener()
  async def on_ready(self):
    print('The BRC Cog is locked, loaded and ready.')

  # // DELETE USER COMMAND
  @commands.command()
  @commands.has_role('BRC-Admin')
  async def delUser(self,ctx,*,userid):
    """Work in progress (Make this an Admin only command)"""
    
    del self.users[str(userid)]
        
    embed = nextcord.Embed(
      title = f"Deleted A User!",
      description = f"User: {userid} has been removed from the reading challenge."
    )
    
    await ctx.send(embed=embed)

    await ctx.invoke(self.bot.get_command('db'))


  # // Display Users Database
  @commands.command(aliases=["db"])
  @commands.has_role('BRC-Admin')
  async def database(self,ctx):
    """Displays all database users (Make this admin only command)"""

    await ctx.send(f'Here is a list of all users:')    
    
    keys = self.users.values()
    for key in keys:
      
      await ctx.send(
        # 'Name: {}\nStreak: {}'.format(key['Name'],key['readingStreak']))
        key.items()
        )


  # // LEADERBOARD ADMIN COMMAND
  @commands.command(aliases=['members','users'])
  @commands.has_role('Brave Bot Testers')
  @commands.has_role('BRC-Admin')
  async def leaders(self,ctx):
    """Displays a list of users who have joined the challenge."""
    
    await ctx.send(f'Here is a list of users who have joined The Bible Reading Challenge and have a reading streak of 5 or higher:')
    keys = self.users.values()
    streakLimit = 5
    embed = nextcord.Embed(
        title="Bible Reading Challengers",
        description=f"Here is a list of all users who have joined the bible reading challenge and have a reading streak of {streakLimit} or more:"
      )
      
    for key in keys:      
      
      if key['readingStreak'] >= streakLimit:
        embed.add_field(
         name=f"{key['Name']}",
         value=f"Reading Streak: {key['readingStreak']} \nExperiece Points: {key['exp']}",inline=True
        )
    
    await ctx.send(embed=embed)
    # await ctx.author.send(embed=embed)



# DO NOT REMOVE! #
def setup(bot: commands.Bot):
  bot.add_cog(BRC_ADMIN(bot))
# DO NOT REMOVE! OR PLACE ANYTHING BELOW! #