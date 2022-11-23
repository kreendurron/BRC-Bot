import discord
from discord.ext import commands
# from main import brc_users

class test(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.users = brc_users

  @commands.Cog.listener()
  async def on_ready(self):
    print("yeah the test cog is working.")

  @commands.command()
  async def test(self, ctx):
    await ctx.send("testing is working")

async def setup(bot):
  await bot.add_cog(test(bot))