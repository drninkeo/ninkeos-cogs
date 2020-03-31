from redbot.core import Configs, checks, commands
import discord

_ = lambda s: s
GENERIC_FORBIDDEN = _(
    "I attempted to do something that Discord denied me permissions for."
    " Your command failed to successfully complete."
)

HIERARCHY_ISSUE_ADD = _(
    "I can not give {role.name} to {member.display_name}"
    " because that role is higher than or equal to my highest role"
    " in the Discord hierarchy."
)

HIERARCHY_ISSUE_REMOVE = _(
    "I can not remove {role.name} from {member.display_name}"
    " because that role is higher than or equal to my highest role"
    " in the Discord hierarchy."
)

ROLE_HIERARCHY_ISSUE = _(
    "I can not edit {role.name}"
    " because that role is higher than my or equal to highest role"
    " in the Discord hierarchy."
)

USER_HIERARCHY_ISSUE_ADD = _(
    "I can not let you give {role.name} to {member.display_name}"
    " because that role is higher than or equal to your highest role"
    " in the Discord hierarchy."
)

USER_HIERARCHY_ISSUE_REMOVE = _(
    "I can not let you remove {role.name} from {member.display_name}"
    " because that role is higher than or equal to your highest role"
    " in the Discord hierarchy."
)

ROLE_USER_HIERARCHY_ISSUE = _(
    "I can not let you edit {role.name}"
    " because that role is higher than or equal to your highest role"
    " in the Discord hierarchy."
)

NEED_MANAGE_ROLES = _("I need manage roles permission to do that.")
_ = T_

class verifyme(commands.Cog):
  """Verification Tool for servers."""
    def __init__(self):
        self.conf = Config.get_conf(self, 5222552557454535)
        
        self.conf.register_guild(
            verify_role=False,
            verify_channel=None,  # Integer ID
            verifyrole=None,  # List of integer ID's
        )
        
     @staticmethod
    def pass_hierarchy_check(ctx: commands.Context, role: discord.Role) -> bool:
        """
        Determines if the bot has a higher role than the given one.
        :param ctx:
        :param role: Role object.
        :return:
        """
        return ctx.guild.me.top_role > role

    @staticmethod
    def pass_user_hierarchy_check(ctx: commands.Context, role: discord.Role) -> bool:
        """
        Determines if a user is allowed to add/remove/edit the given role.
        :param ctx:
        :param role:
        :return:
        """
        return ctx.author.top_role > role or ctx.author == ctx.guild.owner
      
    async def _addrole(
        self, ctx: commands.Context, member: discord.Member, role: discord.Role
    ):
        if member is None:
            member = ctx.author
        if not self.pass_hierarchy_check(ctx, role):
            await ctx.send(_(HIERARCHY_ISSUE_ADD).format(role=role, member=member))
            return
        if not ctx.guild.me.guild_permissions.manage_roles:
            await ctx.send(_(NEED_MANAGE_ROLES))
            return
        try:
            await member.add_roles(role)
        except discord.Forbidden:
            await ctx.send(_(GENERIC_FORBIDDEN))
        else:
            await ctx.send(
                _("{member.display_name}, you have now been verified. Enjoy the chat!").format(
                    role=role, member=member
                )
            )

    @commands.command()
    @commands.guild_only()
    async def addrole(
        self, ctx: commands.Context, rolename: discord.Role, *, user: discord.Member = None
    ):
        """
        Add a role to a user.

        Use double quotes if the role contains spaces.
        If user is left blank it defaults to the author of the command.
        """
        if user is None:
            user = ctx.author
        await self._addrole(ctx, user, rolename)
