from redbot.core import commands
import discord

class admintools(commands.Cog):
    """Do admin things, like managing your channels, members and the like."""

    @commands.command()
    async def muterole(self, ctx, user: discord.Member = None):
        """Mutes a user by giving them a specific mute role instead of applying per channel permissions. This respects server hiearchy."""
        # Your code will go here
        if user is None:
            await ctx.send("Error: you need to define a user to mute.")
        await ctx.send("I can do stuff!")
