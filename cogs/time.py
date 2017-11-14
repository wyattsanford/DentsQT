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
            async with ctx.typing():
                await asyncio.sleep(.5)
                return await self.bot.say(embed=embeds.Embed(title='Current Eve Time:', description=pendulum.utcnow().to_datetime_string()))

    @time.command(pass_context=True)
    async def pst(self, ctx):
        await asyncio.sleep(.5)

        tz = pendulum.timezone('US/Pacific')

        print(tz)

        now_in_pst = pendulum.now(tz)

        print(now_in_pst)

        converted_pst = now_in_pst.to_datetime_string()

        print(converted_pst)

        return await self.bot.say(embed=embeds.Embed(title='Current USTZ (West Coast):', description=converted_pst))


def setup(bot):
    bot.add_cog(Time(bot))
