from redbot.core import Config, checks, commands
import discord

class ownertools(commands.Cog):
    """Do good bot owner things, like checking who uses your bot etc."""

    @commands.command()
    @checks.is_owner()
    async def guildmembers(self, ctx, guild_id: int = None, num_members: int = 10):
        """Adds a channel with the given name"""
        #work on it lol
        if guild_id is None:
            await ctx.send("Error: a server ID is required (hint: you may need dev mode enabled to get the ID)")
        elif guild_id is not None:
            str_message = ''Members in **' + gld.name + '**:' \n'
            try:
                if num_members > 1000:
                  num_members = 1000
                
                gld = bot.get_guild(guild_id)
                str_message += '``` \n'
                
                async for member in gld.fetch_members(num_members):
                    str_message +=  member.name + '#' +member.discriminator + '\n'

                str_message += '``` \n'
                await ctx.send(str_message)
            except Exception as e:
                await ctx.send('Command failed. Error: ' + str(e)) #if error
