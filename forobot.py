'''
Name: ForoBot
Description: This Discord bot is used to help admin with commands and bring fun to the server
Author: Kleberson "Foromir" Gomes
Author's contact: Twitter.com/_kleb
Version: 0.1a
'''

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from random import randint

Client = discord.Client()
client = commands.Bot(command_prefix = ';')

@client.event
async def on_ready():
    print('Bot is online and ready!')
    await client.change_presence(game=discord.Game(name="Commands? Just say ;help"))

@client.event
async def on_message(message):
    if message.content.lower().startswith(';ping'):
        userID = message.author.id
        await client.send_message(message.channel, ":ping_pong: **Pong!** {0}".format(round(Client.latency, 1)))

    if message.content.lower().startswith(';SAY'):
        args = message.content.split(' ')
        await client.send_message(message.channel, "%s" % (' '.join(args[1:])))

    # This command makes the bot flip a coin
    if message.content.lower().startswith(';flip'):
        choice = randint(1, 2)
        if choice == 1:
            await client.add_reaction(message, ':performing_arts:')
        if choice == 2:
            await client.add_reaction(message, ':crown:')

    # Author's and bot information!
    if message.content.lower().startswith(";info"):
        info = discord.Embed(
            title="I am IRO... I mean, Foro Bot!",
            color=0x751be2,
            description="Obrigado por usar o Foro Bot/Thank you for use Foro Bot:\n"
                        "If you have any suggestions or found bugs in this bot, contact me at:\n"
                        "DiscordID: Foromir#5783\n"
                        "Twitter: _kleb"
                        "\n"
                        "\n"
                        "Version: 0.3a"

        )

    # This command shows help command
    if message.content.lower().startswith(';help'):
        help = discord.Embed(
            title='Commands and help bellow',
            color=0x751be2,
            description='Here is a list of all Foro\'s commands\n'
            'flip, ping, help, info, roll, '
        )

# Bot token to work properly
client.run("NDU3NTA4NDI5MDYyMzQwNjA4.DgaV2g.ZH5iQ1JYY4Sx89eZl00NQORmOro")

# Bot initialization on Heroku
Client.run(str(os.environ.get('BOT_TOKEN')))
