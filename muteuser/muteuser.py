from redbot.core import commands

class muteuser(commands.Cog):
    """Mute a user"""

    @commands.command()
    async def mute(self, ctx, user: discord.Member = None):
        """This does stuff!"""
        # Your code will go here
        if user is None:
            await ctx.send("Error: you need to define a user to mute.")
        await ctx.send("I can do stuff!")
