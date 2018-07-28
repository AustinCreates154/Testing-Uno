import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "tb.")

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await ctx.send(':boot: Cya, {}, Ya loser!'.format(user.name))
    await bot.kick(user)


bot.run('NDcyNTY5Njk5MDQxODA0Mjk4.Dj1Smg.MbbM1cKvQYDRO0E8U50tb82mf1s')
