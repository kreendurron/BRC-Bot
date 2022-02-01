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
class BRC_USER(commands.Cog): #Declares a cog name
  """User Commands for The Bible Reading Challenge""" #Description of cog

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
      author = ctx.author.display_name
      exp = 100
      streak = 1
      
      self.users.update({str(ctx.author.id):{"Name":str(author),"exp":exp,"readingStreak":streak}})
      # self.users[str(ctx.author.id)]["Name"] = author
      # self.users[str(ctx.author.id)]["exp"] = exp      
      # self.users[str(ctx.author.id)]["readingStreak"] = streak

      
      print(f"self.users: {self.users}")
      print(f"{author} was not in the database originally but is now")

      

      embed = nextcord.Embed(title=f"A New Challenger Has Entered The Arena!", description=f"Everyone welcome {author} along for the challenge! Here's {exp} experience points to start you off with!")
      
      embed.add_field(name=f"Experience Points:",value=f"{exp}",inline=True)
      embed.add_field(name=f"Reading Streak:",value=f"{streak}",inline=True)
      embed.set_footer(text=f"This bot is still a work in progress. If you're feeling friendly my owner runs on coffee: paypal.me/revivallibrary")

      print(f"{author} was not found in database...but was added \n{self.users[str(ctx.author.id)]}")
      msg = await ctx.send(embed=embed)
      await msg.add_reaction("💖")


  # // CHECKIN COMMAND
  @commands.command(aliases=['check'])
  @commands.has_role('Brave Bot Testers')
  @commands.cooldown(1,86400,commands.BucketType.user)
  async def checkin(self,ctx):
    """Increases your reading streak (work in progress)"""

    if str(ctx.author.id) not in self.users:
      
      print(f"Someone tried to checkin without joining the bible challenge first...")
      
      await ctx.send(f"Sorry you need to join the bible challenge first...\nPlease use the **`!join`** command first.")
      
    else:
      

      author = self.users[str(ctx.author.id)]["Name"]
      self.users[str(ctx.author.id)]["last_claim"]
      streak = self.users[str(ctx.author.id)]["readingStreak"]  
      print(f"streak: {streak}")   
      exp = self.users[str(ctx.author.id)]["exp"]
      last_claim_stamp = self.users[str(ctx.author.id)]["last_claim"]

      print(f"last_claim_stamp: {last_claim_stamp}")
      last_claim = datetime.fromtimestamp(float(last_claim_stamp))
      print(f"last_claim: {last_claim}")
      now = datetime.now()
      delta = now - last_claim
      xp = int(25)
      # bonusXP = 50

      if delta > timedelta(hours=48):
        print("reset streak")
        streak = 1
      else:
        print("increase streak")
        streak += 1

      daily = xp + (int(streak) * int(5))
      amount_after = exp + daily
      print(f"amount_after: {amount_after}")
      self.users[str(ctx.author.id)]["readingStreak"] = streak
      self.users[str(ctx.author.id)]["exp"] += int(daily)
      self.users[str(ctx.author.id)]["last_claim"] = str(now.timestamp())
      
      print(self.users[str(ctx.author.id)])
      embed = nextcord.Embed(title=f"{author} Completed the Daily Reading!", colour=random.randint(0, 0xffffff), description=f"Great Job {author}!! By checking in daily, the amount of XP you recieve will be increased. \n**You just earned: {daily}xp**, now you have **XP: {amount_after}**")
      embed.set_footer(text=f"Your daily streak: {streak}")
      await ctx.send(embed=embed)


  # // STATS COMMAND
  @commands.command(aliases=['data', 'list'])
  @commands.has_role('Brave Bot Testers')
  async def stats(self,ctx):
    
    """Displays your statistics for the challenge."""
      
    if str(ctx.author.id) not in self.users:
      
      print(f"Sorry you need to join the bible challenge first...")
      
      await ctx.send(f"Sorry you need to join the bible challenge first...")
      
    else:
      author = self.users[str(ctx.author.id)]["Name"]
      exp = self.users[str(ctx.author.id)]["exp"]
      streak = self.users[str(ctx.author.id)]["readingStreak"]

      embed = nextcord.Embed(
        title = f"{author}'s Statistics",
        description = f"Keep in the word!")

      embed.add_field(
        name=f"Experience Points:",
        value=f"{exp}",inline=True)
      embed.add_field(name=f"Reading Streak:",value=f"{streak}",inline=True)
      embed.set_footer(text=f"This bot is still a work in progress. If you're feeling friendly my owner runs on coffee: paypal.me/revivallibrary")
    
      await ctx.send(embed=embed)
  

  # // LEADERBOARD COMMAND
  @commands.command()
  @commands.has_role('Brave Bot Testers')
  async def leaderboard(self,ctx):
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
    
    # await ctx.send(embed=embed)
    await ctx.author.send(embed=embed)
    


  

# DO NOT REMOVE! #
def setup(bot: commands.Bot):
  bot.add_cog(BRC_USER(bot))
# DO NOT REMOVE! OR PLACE ANYTHING BELOW! #