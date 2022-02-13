import nextcord
import random
from datetime import date, datetime, timedelta
from replit import db
from nextcord.ext import commands
from main import brc_users
# // END IMPORTS


# // COG CLASS
class BRC_User(commands.Cog): #Declares a cog name
  """User Commands for The Bible Reading Challenge""" #Description of cog

  def __init__(self, bot: commands.Bot):
    self.bot = bot
    self.users = brc_users # new mongo database
    # self.users = db['users'] # old replit database
    
  
  # // ON READY COMMAND
  @commands.Cog.listener()
  async def on_ready(self):
    print('The BRC Cog is locked, loaded and ready.')


  # // JOIN COMMAND
  @commands.command(aliases=['enter', 'begin', 'j'])
  async def join(self,ctx):
    """Use this command to join the challenge."""
      
    
    if self.users.count_documents({"_id":str(ctx.author.id)},limit=1):
      
      print(f"{ctx.author.display_name} user tried to join but was already in the database..")
      
      await ctx.send(f"Hi {ctx.author.display_name}!")
      await ctx.send(f"Woah there, we certainly love the enthusiasm... however, you have already joined The Bible Reading Challenge.")
      
    else:
      author = ctx.author.display_name
      XP = 100
      streak = 0
      
      self.users.insert_one({"_id":str(ctx.author.id),"Name":str(author),"XP":XP,"readingStreak":streak, "last_claim":0})
      
      print(f"{author} was not in the database originally but is now")

      

      embed = nextcord.Embed(title=f"A New Challenger Has Entered The Arena!", description=f"Everyone welcome {author} along for the challenge! Here's {XP} experience points to start you off with!")
      
      embed.add_field(name=f"Experience Points:",value=f"{XP}",inline=True)
      embed.add_field(name=f"Reading Streak:",value=f"{streak}",inline=True)
      embed.set_footer(text=f"This bot is still a work in progress. If you're feeling friendly my owner runs on coffee: paypal.me/revivallibrary")

      msg = await ctx.send(embed=embed)
      await msg.add_reaction("💖")


  # // CHECKIN COMMAND
  # @commands.command(aliases=['check'])
  # @commands.has_role('Brave Bot Testers')
  # @commands.cooldown(1,86400,commands.BucketType.user)
  # async def checkin(self,ctx):
  #   """
  #   This let's us know your reading along with us. 
  #   It will increase your reading streak and give you an XP boost.
  #   """

  #   if str(ctx.author.id) not in self.users:
      
  #     print(f"Someone tried to checkin without joining the bible challenge first...")
      
  #     await ctx.send(f"Sorry you need to join the bible challenge first...\nPlease use the **`!join`** command first.")
      
  #   else:
      

  #     author = self.users[str(ctx.author.id)]["Name"]
  #     self.users[str(ctx.author.id)]["last_claim"]
  #     streak = self.users[str(ctx.author.id)]["readingStreak"]  
  #     print(f"streak: {streak}")   
  #     exp = self.users[str(ctx.author.id)]["exp"]
  #     last_claim_stamp = self.users[str(ctx.author.id)]["last_claim"]

  #     print(f"last_claim_stamp: {last_claim_stamp}")
  #     last_claim = datetime.fromtimestamp(float(last_claim_stamp))
  #     print(f"last_claim: {last_claim}")
  #     now = datetime.now()
  #     delta = now - last_claim
  #     xp = int(25)
  #     # bonusXP = 50

  #     if delta > timedelta(hours=48):
  #       print("reset streak")
  #       streak = 1
  #     else:
  #       print("increase streak")
  #       streak += 1

  #     daily = xp + (int(streak) * int(5))
  #     amount_after = exp + daily
  #     print(f"amount_after: {amount_after}")
  #     self.users[str(ctx.author.id)]["readingStreak"] = streak
  #     self.users[str(ctx.author.id)]["exp"] += int(daily)
  #     self.users[str(ctx.author.id)]["last_claim"] = str(now.timestamp())
      
  #     print(self.users[str(ctx.author.id)])
  #     embed = nextcord.Embed(title=f"{author} Completed the Daily Reading!", colour=random.randint(0, 0xffffff), description=f"Great Job {author}!! By checking in daily, the amount of XP you recieve will be increased. \n**You just earned: {daily}xp**, now you have **XP: {amount_after}**")
  #     embed.set_footer(text=f"Your daily streak: {streak}")
  #     await ctx.send(embed=embed)


  # // STATS COMMAND
  @commands.command(aliases=['data', 'list'])
  @commands.has_role('Brave Bot Testers')
  async def stats(self,ctx):
    
    """Displays your statistics for the challenge."""
      
    if self.users.count_documents({"_id":str(ctx.author.id)},limit=1):
      ctxuser = self.users.find({"_id":str(ctx.author.id)})
      for user in ctxuser:
        username = user["Name"]
        xp = user["XP"]
        streak = user["readingStreak"]

      embed = nextcord.Embed(
        title = f"{username}'s Statistics",
        description = f"Keep in the word!")

      embed.add_field(
        name=f"Experience Points:",
        value=f"{xp}",
        inline=True)
      embed.add_field(name=f"Reading Streak:",
        value=f"{streak}",
        inline=True)
      embed.set_footer(text=f"This bot is still a work in progress. If you're feeling friendly my owner runs on coffee: paypal.me/revivallibrary")
    
      await ctx.send(embed=embed)     
      
    else:
      print(f"Sorry you need to join the bible challenge first...")
      
      await ctx.send(f"Sorry you need to join the bible challenge first...")
      
  

  # // LEADERBOARD COMMAND
  # @commands.command()
  # @commands.has_role('Brave Bot Testers')
  # async def leaderboard(self,ctx):
  #   """Displays a list of users who have joined the challenge."""
    
  #   await ctx.send(f'Here is a list of users who have joined The Bible Reading Challenge and have a reading streak of 5 or higher:')
  #   keys = self.users.values()
  #   streakLimit = 5
  #   embed = nextcord.Embed(
  #       title="Bible Reading Challengers",
  #       description=f"Here is a list of all users who have joined the bible reading challenge and have a reading streak of {streakLimit} or more:"
  #     )
      
  #   for key in keys:      
      
  #     if key['readingStreak'] >= streakLimit:
  #       embed.add_field(
  #        name=f"{key['Name']}",
  #        value=f"Reading Streak: {key['readingStreak']} \nExperiece Points: {key['exp']}",inline=True
  #       )
    
  #   # await ctx.send(embed=embed)
  #   await ctx.author.send(embed=embed)
    


  

# DO NOT REMOVE! #
def setup(bot: commands.Bot):
  bot.add_cog(BRC_User(bot))
# DO NOT REMOVE! OR PLACE ANYTHING BELOW! #