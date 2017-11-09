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

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	print('Ready')

def run(self):
	super().run(config.token, reconnect=True)

@bot.command(pass_context=True)
async def roll(ctx, dice : str):
	"""Rolls a dice, format = NdN"""
	try:
		rolls, limit = map(int, dice.split('d'))
	except Exception:
		await ctx.send('Format must be NdN')
		return
	
	result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
	await ctx.send(result)
	
bot.run(config.token)
