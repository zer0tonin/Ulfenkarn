import logging
import random

from discord.ext.commands import Cog, command


logger = logging.getLogger(__name__)


def number_dice(faces):
    return str(random.randint(1, faces))


def square_dice():
    result = random.randint(1, 6)
    if result < 5:
        return "FAIL"
    if result == 5:
        return "SUCCESS"
    return "CRIT"


def triangle_dice():
    result = random.randint(1, 4)
    if result < 3:
        return "FAIL"
    if result == 3:
        return "SUCCESS"
    return "CRIT"


def pentagon_dice():
    result = random.randint(1, 3)
    if result == 1:
        return "FAIL"
    if result == 2:
        return "SUCCESS"
    return "CRIT"


DICES = {
    "d6": lambda : number_dice(6),
    "d8": lambda : number_dice(8),
    "d12": lambda :number_dice(12),
    "s": square_dice,
    "square": square_dice,
    "t": triangle_dice,
    "triangle": triangle_dice,
    "p": pentagon_dice,
    "pentagon": pentagon_dice,
}


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
    async def roll(self, ctx, count: int, dice: str):
        """
        Rolls one or more dice
        Available dices: d6, d8, d12, s(quare), t(riangle), p(entagon)
        """
        results = [DICES[dice]() for i in range(0, int(count))]
        await ctx.send(', '.join(results))
