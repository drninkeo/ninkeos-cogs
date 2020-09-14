from redbot.core import Config, checks, commands
import discord

class ownertools(commands.Cog):
    """Do good bot owner things, like checking who uses your bot etc."""

    @commands.command()
    @checks.is_owner()
    async def guildmembers(self, ctx, guild_id: int = None, num_members: int = 10, use_nick: bool = False):
        """Gets members that are currently in the same guild as the bot. This can work in other servers, however the bot must be present. This command gets the original user name of a member, not their in-server nickname."""
        #work on it lol
        if guild_id is None:
            await ctx.send("Error: a server ID is required (hint: you may need dev mode enabled to get the ID)")
        else:
            gld = ctx.bot.get_guild(guild_id)
            if gld is not None: 
                str_message = 'Members in **' + gld.name + '** (ID : ' + str(guild_id) + '): \n'
                try:
                    if num_members > 1000:
                        num_members = 1000

                    str_message += '```'
                
                    async for member in gld.fetch_members(limit=num_members):
                        if use_nick == True:
                            str_message +=  member.nick + '#' +member.discriminator + '\n'
                        else:
                            str_message +=  member.name + '#' +member.discriminator + '\n'

                    str_message += '``` \n'
                    await ctx.send(str_message)
                except Exception as e:
                    await ctx.send('Command failed. Error: ' + str(e)) #if error
            else:
               await ctx.send('Either I am not in this guild, or an unknown error has occured.') #bot is not in this guild
