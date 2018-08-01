import discord
from discord.ext import commands
#Make's the bot work
bot = commands.Bot(command_prefix='vb!')
#Makes the bot a bot
#Admin commands below!!
@bot.command(pass_context=True)
@commands.has_role('Admins')
async def kick(ctx, user: discord.Member):
    await ctx.send(':boot:{} has been kicked!!'.format(discord.Member))
    await ctx.kick(user)
#Suggestion command below!
@bot.command()
async def suggestions(ctx):
    await ctx.send(Here is my suggestions form!)
    await ctx.send(https://docs.google.com/forms/d/e/1FAIpQLSe0R6BrOnXXWYhjLAr0IGHN7atdIy65OooH7fhRPLjyBm6tpw/viewform)
    
#Run's the bot
bot.run('NDcyMjcxMTA2MTMzNDU4OTQ0.Dj5hCA.ddJOnn9R_S2gJPNe-LiiMFurlzk')
