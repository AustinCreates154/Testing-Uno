import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "tb.")


def user_is_me(ctx):
    return ctx.message.author.id == "369256915479560192"

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
    
    await ctx.send(embed=embed)
    
@bot.command()
async def botinfo(ctx):
    embed = discord.Embed(title="Bot's Info", description='This is all of my info!', color=0x00ff00)
    embed.add_field(name='Bot ID', value='472569699041804298')
    embed.add_field(name='Bot name', value='Testing Bot Uno')
    embed.add_field(name='Studio invite', value="https://discord.gg/NMyjKak")
    embed.add_field(name='Developer',value='Wolfbane#5559')
    
    await ctx.send(embed=embed)

    
@bot.command()
@commands.check(user_is_me)
async def botsgonnabedown(ctx):
    await ctx.send('The bot\'s gonna be down for a little bit sorry!')
    await ctx.send('You can thank WolfBane#5559 for the update!')
    


bot.run('NDcyNTY5Njk5MDQxODA0Mjk4.Dj1Smg.MbbM1cKvQYDRO0E8U50tb82mf1s')
