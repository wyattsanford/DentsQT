import asyncio
import logging

import dateparser
import pendulum
from discord.ext import commands

from discord import embeds


class Time:
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def time(self, ctx):
        if ctx.invoked_subcommand is None:
            await asyncio.sleep(.5)
            return await self.bot.say(embed=embeds.Embed(title='Current Eve Time:', description=pendulum.utcnow().to_datetime_string()))

    @time.command(pass_context=True)
    async def pst(self, ctx):
        await asyncio.sleep(.5)
        return await self.bot.say(embed=embeds.Embed(title='Current USTZ (West Coast):', description=pendulum.now('US/Pacific').to_datetime_string()))


def setup(bot):
    bot.add_cog(Time(bot))
