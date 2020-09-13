from redbot.core import Config, checks, commands
import discord

class ownertools(commands.Cog):
    """Do good bot owner things, like checking who uses your bot etc."""

    @commands.command()
    @checks.is_owner()
    async def check_members(self, ctx, guild_id: int = None, num_members: int = 10):
        """Adds a channel with the given name"""
        #work on it lol
        if guild_id is None:
            await ctx.send("Error: a server ID is required (hint: you may need dev mode enabled")
        elif guild_id is not None:
            try:
                if num_members > 1000:
                  num_members = 1000
                 
                gld = bot.get_guild(guild_id)
                print('Members in **' + gld.name + '**:')
                print('```')
                async for member in gld.fetch_members(num_members):
                    print(member.name + '#' +member.discriminator)

                print('```')
                
            except Exception as e:
                await ctx.send('Command failed. Error: ' + str(e)) #if error
