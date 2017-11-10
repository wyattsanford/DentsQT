import sys
import traceback

import aiohttp
import aioredis
import pendulum
from discord.ext import commands
from discord.ext.commands import Bot
import discord
import random
import asyncio

try:
    import uvloop
except ImportError:
    pass
else:
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

try:
    import config
except ImportError:
    print('Config not found, please ensure you have set it up correctly')
    sys.exit(1)

description = """This is a barebones bot to learn discord.py"""
bot = commands.Bot(command_prefix='d.', description=description)

print(discord.__version__)

initial_cogs = (
    'cogs.time',
)

for cog in initial_cogs:
    try:
        bot.load_extension(cog)
        print('loaded cog {}'.format(cog), file=sys.stderr)
    except Exception as e:
        print('Failed to load cog {}'.format(cog), file=sys.stderr)
        traceback.print_exc()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print('Ready')


async def process_commands(bot, message):
    ctx = await bot.get_context(message, cls=context.Context)

    if ctx.command is None:
        return
    await bot.invoke(ctx)


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    await bot.process_commands(message)


def run(self):
    super().run(config.token, reconnect=True)


@bot.command()
async def roll(dice: str):
    """Rolls a dice, format = NdN"""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format must be NdN')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)


@bot.command()
async def shutdown():
    await bot.say('Thx for fleet, Tau!')
    sys.exit('Thx for fleet, Tau!')


bot.run(config.token)
