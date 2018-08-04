import discord
from discord.ext import commands
import json
#Make's the bot work
bot = commands.Bot(command_prefix='vb!')
#Makes the bot a bot
#Admin commands below!!
#@bot.command(pass_context=True)
#@commands.has_role('Admins')
#async def ban(ctx, user: discord.Member):
#    await ctx.send(':hammer: {} has been banned! :wave:'.format(user))
#    await ctx.guild.ban(user)
#@bot.command(pass_context=True)
#@commands.has_role('Admins')
#async def kick(ctx, user: discord.Member):
#    await ctx.send(':boot:{} has been kicked!'.format(user))
#    await ctx.guild.kick(user)
#Suggestion command below!
@bot.command()
async def suggestions(ctx):
    await ctx.send('Here is my suggestions form!')
    await ctx.send('https://docs.google.com/forms/d/e/1FAIpQLSe0R6BrOnXXWYhjLAr0IGHN7atdIy65OooH7fhRPLjyBm6tpw/viewform')
#Info command below!
@bot.command(pass_context=True)
async def expose(ctx, user: discord.Member):
    embed=discord.Embed(title='{}\'s info!'.format(user.name), description='Here\'s what I could find!', color=0x00ff00)
    embed.add_field(name='Username', value=user.name, inline=True)
    embed.add_field(name='User ID', value=user.id, inline=True)
    embed.add_field(name='User Stauts', value=user.status, inline=True)
    embed.add_field(name='User\'s Top Role', value=user.top_role, inline=True)
    embed.add_field(name='User join server at', value=user.joined_at, inline=True)
    
    await ctx.send(embed=embed)
    await ctx.send('ExPoSeD')

@bot.command()
async def wanted(ctx):
    embed=discord.Embed(title='Wanted', Description='THIS COMMAND IS A JOKE.', color=0xff0000)
    embed.add_field(name='Umi', value='For being the best sister.')
    embed.add_field(name='Cheshire Fire', value='Being the best admin.')
    embed.add_field(name='Soulz', value='Because there the best!, Chesh:Being a damn aussie')
    embed.add_field(name='Hentai God', value='Chesh:Lolies')
    
    await ctx.send(embed=embed)
    
    
    
#Leveling Events
#@bot.event
#async def on_member_join(member):
#    with open('level.json', 'r') as f:
#        users = json.load(f)
#    
#    #Code
#        with open('level.json', 'w') as f:
#            json.dump(users, f)
#    
#@bot.event
#async def on_message(message):
#    with open('level.json', 'r') as f:
#        users = json.load(f)
#    
#    #Code
#     with open('level.json', 'w') as f:
#         json.dump(users, f)
    
    
#Run's the bot
bot.run('NDcyMjcxMTA2MTMzNDU4OTQ0.DkU4vg.kR6hcwFg7bt6BJ0u5j3BQw6jRaI')
