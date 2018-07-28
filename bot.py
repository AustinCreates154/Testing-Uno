import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "tb.")

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member):
    await ctx.send(':boot: Cya, {}, Ya loser!'.format(user.name))
    await ctx.guild.kick(user)
    print('Someone Had issued the kick command')
    
@bot.command(pass_contex=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member):
    await ctx.send(':hammer: {} has been banned!!!'.format(user.name))
    await ctx.guild.ban(user)
    print('Someone Had issued the ban command')
    
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description='Heres what I can find on {}'.format(user.name), color=0x00ff00)
    embed.add_field(name='Username', value=user.name)
    embed.add_field(name='User Id', value=user.id)
    embed.add_field(name='User Status', value=user.status)
    embed.add_field(name='Highest Role', value=user.top_role)
    embed.add_field(name='User joined at', value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_footer(text="This is all of {}'s info".format(user.name))


bot.run('NDcyNTY5Njk5MDQxODA0Mjk4.Dj1Smg.MbbM1cKvQYDRO0E8U50tb82mf1s')
