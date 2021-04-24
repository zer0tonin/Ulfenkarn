import asyncio
import logging
import yaml

from discord.ext.commands import Bot

from ulfenkarn.dices.cog import Dices

logger = logging.getLogger(__name__)


async def start_bot(config):
    bot = Bot(command_prefix="!", description="Warhammer Quest: Cursed City Helper")
    bot.add_cog(Dices(bot))
    await bot.start(config["token"])


def run():
    with open("config/config.yml", "r") as stream:
        try:
            config = yaml.safe_load(stream)
            logging.basicConfig(level=config["logging_level"])
            asyncio.run(start_bot(config))

        except yaml.YAMLError:
            logger.exception("Failed to parse config")
            exit(1)
