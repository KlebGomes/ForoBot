'''
Name: ForoBot
Description: This Discord bot is used to help admin with commands and bring fun to the server
Author: Kleberson "Foromir" Gomes
Author's contact: Twitter.com/_kleb
Version: 0.4
'''

import discord
from discord.ext.commands import Bot
import random

TOKEN = 'NDU3NTA4NDI5MDYyMzQwNjA4.DgcRqA.tg2IQwdBkmUP0_shV7ROg90-Rno'
BOT_PREFIX = ';'
client = Bot(command_prefix=BOT_PREFIX)


@client.event
async def on_ready():
    print('Bot is online and ready!')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='Commands? Just say ;help'))


# This command sends a random famous quote from a sorted game in the list.
@client.command(name='rgq',
                description='Random quotes from various games. Can you guess where they are from?',
                brief='- Random games quotes.',
                aliases=['gamequotes', 'gq'],
                pass_context=True)
async def quotes_games(context):
    possible_responses = [
        'Get over here!',  # Scorpion, Mortal Kombat
        'Chicken chaser. Haha! What a stupid name!',  # Citizens, Fable
        'War, war never changes.',  # Narrator, Fallout 3
        'Hurt me more!',  # Fox Hound, Metal Gear Solid
        'Snake? Snake? SNAAAAAAAAKE!!!',  # The Colonel, Metal Geral Solid
        'Come to me dark warriors!',  # Valkyrie Profile
        'What is a man? A miserable little pile of secrets.',  # Dracula, Castlevania SOTN
        'I kept my axe sharp, especially for you!',  # Mr. Punish, Tibia
        'It\'s dangerous to go alone. Take this!',  # Old man, The Legend Of Zelda
        'Hey! Listen!',  # Na'vi, The Legend of Zelda: Ocarina of Time
        'I used to be an adventurer like you. Then I took an arrow in the knee...',  # Guards, TES: Skyrim
        'It\'s super effective!',  # Pokemon game series
        'Do a barrel roll!',  # Star Fox 64
        'I\'m here to kick ass and chew bubblegum... and I\'m all out of bubblegum.',  # Duke Nukem 3D
        'Guns! Glorious Guns!',  # Borderlands 2
        'Are you a boy or a girl?',  # Pokemon series
        'Stop right there, criminal scum!',  # Guard, TES: Oblivion
        'You\'re not prepared!',  # Illidan, World of Warcraft'
        'Your words are as empty as your soul!',  # Ritcher, Castlevania SOTN
        'C-C-C-C-Combo Breaker!',  # Narrator, Killer Instinct

    ]
    await client.say(random.choice(possible_responses) + ', ' + context.message.author.mention)


# This command shows information about the author and the Foro Bot.
@client.command(description='Show information about author, bot and changelog.',
                brief='- Info about the author and Foro Bot.')
async def info():
    info = discord.Embed(
        title="I am IRO... I mean, Foro Bot!",
        color=0x751be2,
        description="Obrigado por usar o Foro Bot / Thank you for using Foro Bot!\n"
                    "Foro is an open source bot. Its code can be found on Github.\n"
                    "Check the Changelog.\n"
                    "If you have any suggestions or find bugs in this bot, contact me.\n\n"
    )
    discord.Embed.add_field(info, name='**Author**', value='DiscordID: Foromir#5783\nTwitter: _kleb', inline=True),
    discord.Embed.add_field(info, name='Version', value='0.4', inline=True)
    discord.Embed.add_field(info, name='Changelog', value='https://git.io/vhDmQ', inline=False)
    discord.Embed.set_footer(info, text='Thank you so much for choose Foro as one of your bots! <3')
    await client.say(embed=info)


# This command sort two numbers and return an emoticon meaning heards or trails.
@client.command(description='Flip a coin and show an emoticon as result for heads or trails.',
                brief='Flip a coin and show heads or trails.')
async def flip():
    choice = random.randint(1, 2)
    if choice == 1:
        await client.say(':performing_arts:')
    else:
        await client.say(':crown:')


# This command is used to ping the bot and check it's latency.
@client.command(decription='Check the latency between server and bot.',
                brief='Ping Foro Bot.',
                pass_context=True)
async def ping(ctx):
    await client.say(':ping_pong: **Pong!**, ' + ctx.message.author.mention)


# This command makes the bot say what the user sends
@client.command(description='Makes the bot says what you want.',
                brief='Makes the bot says anything.',
                pass_context=True)
async def say(ctx, *args):
    msg = ' '.join(args)
    if ctx.message.server is None:
        await client.say('I can\'t execute this command on a private channel.')
    else:
        await client.delete_message(ctx.message)
        await client.say(msg)


# Bot token to work properly
client.run(TOKEN)
