import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "tb.")

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member):
    await ctx.send(':boot: Cya, {}, Ya loser!'.format(user.name))
    await ctx.guild.kick(user)
    print('{} Has issued the kick command'.format(message.author))
    
@bot.command(pass_contex=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member):
    await ctx.send(':hammer: {} has been banned!!!'.format(user.name))
    await ctx.guild.ban(user)
    print('{} Has issues the kick command'.format (message.author))


bot.run('NDcyNTY5Njk5MDQxODA0Mjk4.Dj1Smg.MbbM1cKvQYDRO0E8U50tb82mf1s')
