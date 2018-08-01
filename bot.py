import discord
from discord.ext import commands
#Make's the bot work
bot = commands.Bot(command_prefix='vb!')
#Makes the bot a bot
#Admin commands below!!
@bot.command(pass_context=True)
@commands.has_role(Admins)
async def kick(ctx, user: discord.Member):
    await ctx.send(':boot: {0} has been kicked by:{1}!!'.format(discord.Member, ctx.message.author))
    await ctx.kick(user)

#Run's the bot
bot.run('NDcyMjcxMTA2MTMzNDU4OTQ0.Dj5hCA.ddJOnn9R_S2gJPNe-LiiMFurlzk')
