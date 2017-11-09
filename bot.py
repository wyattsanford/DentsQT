import logging
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

# initial.cogs = (
#	'cogs.time',
#)
print(discord.__version__)
bot.run(config.token)
#def __init__(self):
#	super().__init__(
#		command_prefix='d.',
#		description=description,
#		pm_help=None,
#		help_attrs=dict(hidden=True))
#
#	self.client_id = config.client_id
#	self.token = config.token
#	self.session = aiohttp.ClientSession(loop=self.loop)

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	print('Ready')
#@bot.event
#async def on_message(self, message):
#	if message.author.bot:
#		return
#	await self.process_commands(message)
#
#async def process_commands(self, message):
#	ctx = await self.get_context(message, cls=context.Context)
#
#	if ctx.command is None:
#		return
#	await self.invoke(ctx)

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
