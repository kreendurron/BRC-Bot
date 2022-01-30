import discord
import json
# import asyncio
from replit import db
from datetime import date
from discord.ext import commands
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
class BRC(commands.Cog): #Declares a cog name
  """Commands for The Bible Reading Challenge""" #Description of cog

  def __init__(self, bot: commands.Bot):
    self.bot = bot
    self.users = db['users']
  
  # // ON READY COMMAND
  @commands.Cog.listener()
  async def on_ready(self):
    print('The BRC Cog is locked, loaded and ready.')

  # // JOIN COMMAND
  @commands.command(aliases=['enter', 'begin', 'j'])
  async def join(self,ctx):
    """Use this command to join the challenge."""
      
    if str(ctx.author.id) in self.users:
      
      print(f"{ctx.author.display_name} successfully found in database...")
      
      await ctx.send(f"Hi {ctx.author.display_name}!")
      await ctx.send(f"Woah there, we certainly love the enthusiasm... however, you have already joined The Bible Reading Challenge.")
      
    else:
      self.users[str(ctx.author.id)] = {}
      author = self.users[str(ctx.author.id)]["Name"] = ctx.author.display_name
      exp = self.users[str(ctx.author.id)]["exp"] = 100
      streak = self.users[str(ctx.author.id)]["readingStreak"] = 0
      print(f"{author} was not in the database originally but is now")

      embed = discord.Embed(title=f"A New Challenger Has Entered The Arena!", description=f"Everyone welcome {author} along for the challenge! Here's {exp} experience points to start you off with!")
      
      embed.add_field(name=f"Experience Points:",value=f"{exp}",inline=True)
      embed.add_field(name=f"Reading Streak:",value=f"{streak}",inline=True)
      embed.set_footer(text=f"This bot is still a work in progress. If you're feeling friendly my owner runs on coffee: paypal.me/revivallibrary")

      print(f"{author} was not found in database...but was added \n{self.users[str(ctx.author.id)]}")
      msg = await ctx.send(embed=embed)
      await msg.add_reaction("💖")

  # // STATS COMMAND
  @commands.command(aliases=['data', 'list'])
  async def stats(self,ctx):
    
    """Displays your statistics for the challenge."""
      
    if str(ctx.author.id) not in self.users:
      
      print(f"Sorry you need to join the bible challenge first...")
      
      await ctx.send(f"Sorry you need to join the bible challenge first...")
      
    else:
      author = self.users[str(ctx.author.id)]["Name"]
      exp = self.users[str(ctx.author.id)]["exp"]
      streak = self.users[str(ctx.author.id)]["readingStreak"]

      embed = discord.Embed(title=f"{author}'s Statistics", description=f"Keep in the word!")

      embed.add_field(name=f"Experience Points:",value=f"{exp}",inline=True)
      embed.add_field(name=f"Reading Streak:",value=f"{streak}",inline=True)
      embed.set_footer(text=f"This bot is still a work in progress. If you're feeling friendly my owner runs on coffee: paypal.me/revivallibrary")
    
      await ctx.send(embed=embed)
  
  # // TEST COMMAND
  @commands.command(aliases=['members','users'])
  async def displayMembers(self,ctx):
    """Displays a list of users who have joined the Challenge."""
    await ctx.send(f'Here is a list of users who have joined The Bible Reading Challenge and have a reading streak of 5 or higher:')
    keys = self.users.values()
    for key in keys:      
      
      if key['readingStreak'] >= 5:
        await ctx.send('Name: {}\nStreak: {}'.format(key['Name'],key['readingStreak']))

    

  # // CHECKIN COMMAND
  @commands.command(aliases=['check in'])
  async def checkin(self,ctx):
    """Increases your reading streak (work in progress)"""
    
      
    if str(ctx.author.id) not in self.users:
      
      print(f"Someone tried to checkin without joining the bible challenge first...")
      
      await ctx.send(f"Sorry you need to join the bible challenge first...")
      
    else:
      streak = self.users[str(ctx.author.id)]["readingStreak"]     
      exp = self.users[str(ctx.author.id)]["exp"]
      xp = 25
      bonusXP = 50
      
      exp =  int(exp) + int(xp)
      streak = int(streak) + 1
      print(streak)
      self.users[str(ctx.author.id)]["readingStreak"] = streak
      self.users[str(ctx.author.id)]["exp"] = exp + bonusXP

      print(self.users)
      
      await ctx.send(f"You've earned {xp} Experience Points plus an additional {bonusXP} bonus Experience Points for being an such an awseome bot beta tester!")
      # await asyncio.sleep(1)
      await ctx.invoke(self.bot.get_command('stats'))

# DO NOT REMOVE! #
def setup(bot: commands.Bot):
  bot.add_cog(BRC(bot))
# DO NOT REMOVE! OR PLACE ANYTHING BELOW! #