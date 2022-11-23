import discord
import random
# from datetime import date, datetime, timedelta
# from replit import db | can probably delete this now that we migrated to mongodb
from discord.ext import commands
from main import brc_users
# // END IMPORTS


# // COG CLASS
class BRC_User(commands.Cog): #Declares a cog name
  """User Commands for The Bible Reading Challenge""" #Description of cog

  def __init__(self, client: commands.client):
    self.client = client
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
      await ctx.message.delete()
      
    else:
      author = ctx.author.display_name
      XP = 100
      streak = 0
      
      self.users.insert_one({"_id":str(ctx.author.id),"Name":str(author),"XP":XP,"readingStreak":streak, "last_claim":1643736997})
      
      print(f"{author} was not in the database originally but is now")      

      embed = discord.Embed(title=f"A New Challenger Has Entered The Arena!", description=f"Everyone welcome {author} along for the challenge! Here's {XP} experience points to start you off with!")
      
      embed.add_field(name=f"Experience Points:",value=f"{XP}",inline=True)
      embed.add_field(name=f"Reading Streak:",value=f"{streak}",inline=True)
      embed.set_footer(text=f"This client is still a work in progress. If you're feeling friendly my owner runs on coffee: paypal.me/revivallibrary")
      await ctx.message.delete()
      msg = await ctx.send(embed=embed)
      await msg.add_reaction("💖")
      

  # // CHECKIN COMMAND
  @commands.command(aliases=['check'])
  @commands.has_role('Brave client Testers')
  @commands.cooldown(1,86400,commands.BucketType.user)
  async def checkin(self,ctx):
    """
    This let's us know your reading along with us. 86400
    It will increase your reading streak and give you an XP boost.
    """
    if not self.users.count_documents({"_id":str(ctx.author.id)},limit=1):
          
      print(f"Someone tried to checkin without joining the bible challenge first...")
      
      await ctx.send(f"Sorry you need to join the bible challenge first...\nPlease use the **`!join`** command first.")
      await ctx.message.delete()
      
    else:
      # DO THE THING
      for user in self.users.find({"_id":str(ctx.author.id)}):
        username = user["Name"]
        xp = user["XP"]
        streak = user["readingStreak"]
        last_claim_stamp = user["last_claim"]
        

        print(f"\nusername: {username}\nxp: {xp}\nstreak: {streak}\nlastclaim: {last_claim_stamp}")
        print("///////////////")
        last_claim = datetime.fromtimestamp(float(last_claim_stamp))
        now = datetime.now()
        delta = now -last_claim
        
        if delta < timedelta(hours=48):
          print("reset streak")
          self.users.update_one({"_id":str(ctx.author.id)},{"$inc":{"readingStreak":1}})
        else:
          print("increase streak")
          self.users.update_one({"_id":str(ctx.author.id)},{"$set":{"readingStreak":1}})

        base = int(50)
        bonus = base + (streak * 5)

        self.users.update_one({"_id":str(ctx.author.id)},{"$set":{"XP":base + bonus}})
        self.users.update_one({"_id":str(ctx.author.id)},{"$set":{"last_claim":datetime.timestamp(now)}})

      for user in self.users.find({"_id":str(ctx.author.id)}):
        username = user["Name"]
        xp = user["XP"]
        streak = user["readingStreak"]
        last_claim_stamp = user["last_claim"]

        print(f"\nusername: {username}\nxp: {xp}\nstreak: {streak}\nlastclaim: {last_claim_stamp}")
        print("///////////////")

      # Display The Thing      
      embed = discord.Embed(
        title=f"{username} Completed the Daily Reading!", colour=random.randint(0, 0xffffff),
        description=f"**Command:** `!checkin` | **Used By:** {username}")
      embed.add_field(
         name=f"Great Job!!",
         value=f"By checking in daily, the amount of XP you recieve will be increased. \n**You just earned: {base}xp**, now you have **XP: {xp}**",inline=True
        )
      embed.set_footer(text=f"Your daily streak: `{streak}`")
      await ctx.send(embed=embed)
      await ctx.message.delete()

  # // STATS COMMAND
  @commands.command(aliases=['data', 'list'])
  @commands.has_role('Brave client Testers')
  async def stats(self,ctx):
    
    """Displays your statistics for the challenge."""
      
    if self.users.count_documents({"_id":str(ctx.author.id)},limit=1):
      ctxuser = self.users.find({"_id":str(ctx.author.id)})
      for user in ctxuser:
        username = user["Name"]
        xp = user["XP"]
        streak = user["readingStreak"]

      embed = discord.Embed(
        title = f"{username}'s Statistics",
        description = f"**Command:** `!stats` | **Used By:** {username}")

      embed.add_field(
        name=f"Experience Points:",
        value=f"{xp}",
        inline=True)
      embed.add_field(name=f"Reading Streak:",
        value=f"{streak}",
        inline=True)
      
      embed.set_footer(text=f"This client is still a work in progress. If you're feeling friendly my owner runs on coffee: paypal.me/revivallibrary")
    
      await ctx.send(embed=embed)     
      await ctx.message.delete()
    else:
      print(f"Sorry you need to join the bible challenge first...")
      
      await ctx.send(f"Sorry you need to join the bible challenge first...")
      await ctx.message.delete()
  

  # // LEADERBOARD COMMAND
  # @commands.command()
  # @commands.has_role('Brave client Testers')
  # async def leaderboard(self,ctx):
  #   """Displays a list of users who have joined the challenge."""
    
  #   await ctx.send(f'Here is a list of users who have joined The Bible Reading Challenge and have a reading streak of 5 or higher:')
  #   keys = self.users.values()
  #   streakLimit = 5
  #   embed = discord.Embed(
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
def setup(client: commands.client):
  client.add_cog(BRC_User(client))
# DO NOT REMOVE! OR PLACE ANYTHING BELOW! #