import nextcord
import json
import sys
from datetime import date
from nextcord.ext import commands
#Don't Remove this import, you need it
import random
sys.path.insert(0,'./utils/misc')
from randStuff import randEncouragments

today = date.today()
print("Today's date:", today)

# // TIME STUFF
day = today.strftime("%d")
# print("day =", day)
month = today.strftime("%B")
# print("month =", month)
year = today.strftime("%y")
# print("year =", year)

# // DEFINE THE COG CLASS
class Plan(commands.Cog): #Declares a cog name
  """Commands that will display the reading plan.""" #Description of cog

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  # // ON READY EVENT
  @commands.Cog.listener()
  async def on_ready(self):
    print('The Plan Cog is locked, loaded and ready.')      
  
  # // DAILY READING PLAN
  @commands.command()
  @commands.has_role('BRC-Admin')
  async def day(self,ctx: commands.context):
    """Display's Today's Reading Schedule"""
    with open(f"./utils/json/{year}.json", "r") as f:
      readingList = json.load(f)
      
      dailyReading = str(readingList[month][day])
      
      if not "," in dailyReading:
        print("comma not found")
        if "Catch" in dailyReading:
          embed = nextcord.Embed(title=f"Catchup Day!", description=f"{dailyReading}\n\nDaily Encouragment: {random.choice(randEncouragments)}")
          print("Catch-up day!")
        elif "Lord's Day" in dailyReading:
          embed = nextcord.Embed(title=f"Happy Lord's Day!", description=f"We will pick back up tomorrow!")
          print("Lord's Day")
        else:
          firstReading = dailyReading.split(",")[0] #Luke 7-12
          
          cv1 = firstReading.split(" ")
          firstBook = cv1[0]
          # firstChapterRange = cv1[1]
          firstChapter = cv1[1].split("–")[0] # This dash was different in the json that on the keyboard, copy/paste the dash from json data
          
          embed = nextcord.Embed(title=f"Today's Reading for {month} {day}", description=f"**{dailyReading}**\n\nDaily Encouragment: {random.choice(randEncouragments)}")
          embed.set_image(url="https://biblereading.christkirk.com/wp-content/uploads/2021/08/7.-Replacement-for-website-header-1024x369.jpg")
          embed.set_author(name="The Bible Reading Challenge", url="https://revival-library.com/bible-reading-challenge")
          embed.add_field(name=f"Link",value=f"https://www.blueletterbible.org/kjv/{firstBook}/{firstChapter}")
          embed.set_footer(text="This bot is still a work in progress. If you're feeling friendly my owner runs on coffee: paypal.me/revivallibrary ")

      else:
        print("comma found")
        if "Catch" in dailyReading:
          embed = nextcord.Embed(title=f"Catchup Day!", description=f"{dailyReading}\n\nDaily Encouragment: {random.choice(randEncouragments)}")
          print("Catch-up day!")
        if "optional" in dailyReading:
          firstReading = dailyReading.split(",")[0] #Luke 7-12
          
          cv1 = firstReading.split(" ")
          firstBook = cv1[0]
          # firstChapterRange = cv1[1]
          firstChapter = cv1[1].split("–")[0] # This dash was different in the json that on the keyboard, copy/paste the dash from json data
          
          embed = nextcord.Embed(title=f"Today's Reading for {month} {day}", description=f"**{dailyReading}**\n\nDaily Encouragment: {random.choice(randEncouragments)}")
          embed.set_image(url="https://biblereading.christkirk.com/wp-content/uploads/2021/08/7.-Replacement-for-website-header-1024x369.jpg")
          embed.set_author(name="The Bible Reading Challenge", url="https://revival-library.com/bible-reading-challenge")
          embed.add_field(name=f"Link",value=f"https://www.blueletterbible.org/kjv/{firstBook}/{firstChapter}")
          embed.set_footer(text="This bot is still a work in progress. If you're feeling friendly my owner runs on coffee: paypal.me/revivallibrary ")
        else:
          firstReading = dailyReading.rsplit(",",2)[0] #Luke 7-12
          secondReading = dailyReading.rsplit(",",2)[1].lstrip() #John 5-13

          cv1 = firstReading.split(" ") #['Luke', '7-12']
          firstBook = cv1[0]
          firstChapter = cv1[1].split("–")[0]
          cv2 = secondReading.split(" ") #['John', '5-13']
          secondBook = cv2[0]
          secondChapter = cv2[1].split("–")[0]

          # // EMBED
          embed = nextcord.Embed(title=f"Today's Reading for {month} {day}", description=f"{dailyReading}\n\nDaily Encouragment: {random.choice(randEncouragments)}")
          embed.set_image(url="https://biblereading.christkirk.com/wp-content/uploads/2021/08/7.-Replacement-for-website-header-1024x369.jpg")
          embed.set_author(name="The Bible Reading Challenge", url="https://revival-library.com/bible-reading-challenge")
          embed.add_field(name=f"First Reading",value=f"https://www.blueletterbible.org/kjv/{firstBook}/{firstChapter}")
          embed.add_field(name=f"Second Reading",value=f"https://www.blueletterbible.org/kjv/{secondBook}/{secondChapter}")
          embed.set_footer(text="This bot is still a work in progress. If you're feeling friendly my owner runs on coffee: paypal.me/revivallibrary ")

      
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("✅") #To get the emoji, in discord type "\:emoji_name:" then highlight with cursor and copy paste into code

# DO NOT REMOVE! #
def setup(bot: commands.Bot):
  bot.add_cog(Plan(bot))
# DO NOT REMOVE! OR PLACE ANYTHING BELOW! #
