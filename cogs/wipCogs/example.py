from nextcord.ext import commands
#Don't Remove this import, you need it

class Example(commands.Cog): #Declares a cog name
  """Example Commands""" #Description of cog

  def __init__(self, bot: commands.Bot):
    self.bot = bot #Assigns the bot to self.bot
    #Needed to have the main.py file work with it

  @commands.Cog.listener()
  async def on_ready(self):
    print('Example Cog is ready')

  @commands.command() #Command decorator
  async def ping(self, ctx: commands.Context): #Always enter these attributes into the parenthisis for cogs- If you don't it will not work.
    """Display the bot latency""" #Describes the command

    await ctx.send(f"Pong! | {round(self.bot.latency * 1000)}ms")
    #Basic ping command code. You can replace this with whatever you want.
  
  @commands.command()
  async def hello(self, ctx: commands.Context):
    """The bot will reply with hello"""

    await ctx.send("Hello!")
    #An example of a simple command

# DO NOT REMOVE! #
def setup(bot: commands.Bot):
  bot.add_cog(Example(bot))
# DO NOT REMOVE! OR PLACE ANYTHING BELOW! #