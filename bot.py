import sys
import traceback

import aiohttp
import aioredis
import pendulum
from discord.ext import commands
from discord.ext.commands import Bot
import discord
import random


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
bot.run(config.token)

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	print('Ready')

def run(self):
	super().run(token, reconnect=True)

@bot.command()
async def roll(dice : str):
	"""Rolls a dice, format = NdN"""
	try:
		rolls, limit = map(int, dice.split('d'))
	except Exception:
		await bot.say('Format must be NdN')
		return
	
	result = ', '.join(str(randint(1, limit)) for r in range(rolls))
	await bot.say(result)
