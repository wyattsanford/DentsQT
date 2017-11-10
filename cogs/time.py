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
        """
        Gives the current EVE time.

        Time PST gives current time in USTZ: West Coast
        """
        if ctx.invoked_subcommand is None:
            await asyncio.sleep(.5)
            return await self.bot.say(
                embed=embeds.Embed(title='Current Eve Time:', description=pendulum.utcnow().to_datetime_string()))

    @time.command()
    async def pst(self):
        await asyncio.sleep(.5)
        return await self.bot.say(embed=embeds.Embed(title='Current USTZ (West Coast):',
                                                     descrpition=pendulum.now(tz='US/Pacific').tz)

def setup(bot):
            bot.add_cog(Time(bot))