from redbot.core import commands
import discord

class admintools(commands.Cog):
    """Do admin things, like managing your channels, members and the like."""

    @commands.command()
    async def muterole(self, ctx, user: discord.Member = None, role: discord.Role = None):
        """Mutes a user by giving them a specific mute role instead of applying per channel permissions. This respects server hiearchy."""
        # Your code will go here
        if user is None:
            await ctx.send("Error: a user is required.")
        if role is None:
            await ctx.send("Error: you need to define a role to apply to the user.")
        if role is not None and user is not None:
            await ctx.send("all good")
