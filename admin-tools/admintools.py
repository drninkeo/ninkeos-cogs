from redbot.core import Config, checks, commands
import discord

class admintools(commands.Cog):
    """Do admin things, like managing your channels, members and the like."""
    
    @checks.admin_or_permissions(manage_roles=True)
    @commands.guild_only()
    @commands.command()
    async def setrole(self, ctx, user: discord.Member = None, role: discord.Role = None):
        """Assigns a user a role as given. Only roles that are equal to or less than the bot in the hierachy can work."""
        checkPass = None
        # Your code will go here
        if user is None:
            await ctx.send("Error: a user is required.")
            checkPass = False
        if role is None:
            if checkPass is None:
                await ctx.send("Error: you need to define a role to apply to the user.")
        
        #Apply the muted user role specified by the code.
        if role is not None and user is not None:
            try:
                await user.add_roles(role)
            except Exception as e:
                await ctx.send('Command failed. Error: ' + str(e)) #if error
            else:
                await ctx.send('Gave user **' + user.name + '** the role **' + role.name + '**')
    
    
    @checks.admin_or_permissions(manage_channels=True)
    @commands.guild_only()       
    @commands.command()
    async def addchannel(self, ctx, chan_name: str = None):
        """Adds a channel with the given name"""
        # Your code will go here
        if chan_name is None:
            await ctx.send("Error: a channel name is required.")
        elif chan_name is not None:
            try:
                guild = ctx.message.guild
                await guild.create_text_channel(str(chan_name))
            except Exception as e:
                await ctx.send('Command failed. Error: ' + str(e)) #if error
            else:
                await ctx.send('Created new channel titled **' + chan_name + '**')
            
            
    @checks.admin_or_permissions(manage_messages=True)
    @commands.guild_only()       
    @commands.command()
    async def move(self, ctx, message_id: int = None, chan: discord.TextChannel = None):
        """Moves a message to the specified channel"""
        checkPass = None
        # Your code will go here
        if message_id is None:
            await ctx.send("Error: a message ID is required.")
            checkPass = False
        if chan is None:
            if checkPass is None:
                await ctx.send("Error: a channel to move the message to is required.")
        
        #Apply the muted user role specified by the code.
        if message_id is not None and chan is not None:
            try:
                oldchan = ctx.channel
                msg = await oldchan.fetch_message(message_id)
                if msg.content != "":
                  await chan.send('Originally posted in ' + oldchan.mention + ' by ' + str(msg.author) + '\n' + msg.content)
                else:
                  await chan.send('Originally posted in ' + oldchan.mention + ' by ' + str(msg.author) + '\n' + msg.attachments[0].url)
            except Exception as e:
                await ctx.send('Command failed. Error: ' + str(e)) #if error
            else:
                await msg.add_reaction("\N{WASTEBASKET}")
                # React with a bin to indicate moved
    
    @checks.admin_or_permissions(manage_messages=True)
    @commands.guild_only()       
    @commands.command()
    async def hardmove(self, ctx, message_id: int = None, chan: discord.TextChannel = None):
        """Moves a message to the specified channel and delete the original message"""
        checkPass = None
        # Your code will go here
        if message_id is None:
            await ctx.send("Error: a message ID is required.")
            checkPass = False
        if chan is None:
            if checkPass is None:
                await ctx.send("Error: a channel to move the message to is required.")
        
        #Apply the muted user role specified by the code.
        if message_id is not None and chan is not None:
            try:
                oldchan = ctx.channel
                msg = await oldchan.fetch_message(message_id)
                if msg.content != "":
                  await chan.send('Originally posted in ' + oldchan.mention + ' by ' + str(msg.author) + '\n' + msg.content)
                else:
                  await chan.send('Originally posted in ' + oldchan.mention + ' by ' + str(msg.author) + '\n' + msg.attachments[0].url)
            except Exception as e:
                await ctx.send('Command failed. Error: ' + str(e)) #if error
            else:
                await msg.delete()
                # React with a bin to indicate moved
