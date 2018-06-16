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
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "")

@client.event
async def on_ready():
    print('Bot is online and ready!')

@client.event
async def on_message(message):
    if message.content.upper().startswith('/PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> :ping_pong: **Pong!**" % (userID))
    if message.content.upper().startswith('/SAY'):
        args = message.content.split(' ')
        if message.auhorid ==
        #args [0] = !SAY
        #args [1] = Hey
        #args [2] = There
        #args [1:] = Hey There
        await client.send_message(message.channel, "%s" % (' '.join(args[1:])))

client.run("NDU3NTA4NDI5MDYyMzQwNjA4.DgaV2g.ZH5iQ1JYY4Sx89eZl00NQORmOro")

# Bot initialization on Heroku
client.run(str(os.environ.get('BOT_TOKEN')))
