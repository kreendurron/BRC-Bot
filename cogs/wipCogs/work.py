import discord
import json
from discord.ext import commands

class Work(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  
  @commands.command()
  async def jobs(self,ctx: commands.context):
    """Display list of jobs."""
    with open("./utils/json/jobs.json", "r") as f:
      jobslist = json.load(f)

      embed = discord.Embed(title="Reading Schedule")

      for job in jobslist:
        embed.add_field(name=f"{job.title()}", value=f"{jobslist[job]['description']}\n\nSalary: :coin:{jobslist[job]['salary']}",inline=True)
        print(job)

    await ctx.reply(embed=embed)


def setup(bot):
  bot.add_cog(Work(bot))