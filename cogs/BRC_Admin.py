import nextcord
from datetime import date, datetime, timedelta
from nextcord.ext import commands
from main import brc_users
# // END IMPORTS

# // DEFINE THE COG CLASS
class BRC_Admin(commands.Cog):  #Declares a cog name
    """Admin Commands for The Bible Reading Challenge"""  #Description of cog

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.users = brc_users

    # // ON READY COMMAND
    @commands.Cog.listener()
    async def on_ready(self):
        print('The MongoTest Cog is locked, loaded and ready.')

    # // Display Users Database
    @commands.command(aliases=["users"])
    @commands.has_role('BRC-Admin')
    async def brcUsers(self, ctx):
        """Displays all mongodb users and attributes."""

        embed = nextcord.Embed(
            title="Bible Reading Challengers",
            description=
            "Work In Progress, will eventually display the top 5 users with the highest rankings."
        )

        results = self.users.find({})

        for result in results:
            embed.add_field(
                name=f"{result['Name']}",
                value=f"XP: {result['XP']}\nReadingStreak: {result['readingStreak']}",
                inline=True)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    # // DELETE USER COMMAND
    @commands.command()
    @commands.has_role('BRC-Admin')
    async def delUser(self, ctx, *, userid):
        """Delete a user from the challenge. Takes a userID as an argument."""

        self.users.delete_one({"_id": str(userid)})

        embed = nextcord.Embed(
            title=f"Deleted A User!",
            description=
            f"User: {userid} has been removed from the reading challenge.")

        await ctx.send(embed=embed)
        await ctx.message.delete()

        await ctx.invoke(self.bot.get_command('brcUsers'))

    

# DO NOT REMOVE! #
def setup(bot: commands.Bot):
    bot.add_cog(BRC_Admin(bot))


# DO NOT REMOVE! OR PLACE ANYTHING BELOW! #
