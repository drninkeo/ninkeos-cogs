from redbot.core import commands

class muteuser(commands.Cog):
    """Mute a user"""

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")
