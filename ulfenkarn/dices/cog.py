import logging

from discord.ext.commands import Cog, command


logger = logging.getLogger(__name__)


class Dices(Cog):
    """
    Rolls the dices available in game
    """

    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        logger.info("We have logged in as {0.user}".format(self.bot))

    @command()
    async def roll(self, ctx, *_):
        # TODO
        return
