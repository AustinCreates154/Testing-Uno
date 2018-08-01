import discord
from discord.ext import commands
#Make's the bot work
bot = commands.Bot(command_prefix='vb!')
#Makes the bot a bot
await bot.change_status(game=discord.Game(name='I am a tad bit broken'))

#Run's the bot
bot.run('NDcyMjcxMTA2MTMzNDU4OTQ0.Dj5hCA.ddJOnn9R_S2gJPNe-LiiMFurlzk')
