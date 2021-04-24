# Ulfenkarn: the unofficial Warhammer Quest: Cursed City bot

Ulfenkarn is a bot made to help remote games of the Cursed City tabletop games through discord.

The project follows the [gazr](https://gazr.io) specs.

To launch it:
* make sure you have docker and docker-compose installed
* copy config/config.example.yml into config/config.yml and add your own bot token + customize the strings
* modify gifs.csv to add your own gifs
* just do `make run` or `docker-compose build ulfenkarn && docker-compose up ulfenkarn` to launch it
