import os
from discord.ext import commands
import random
from keep_alive import keep_alive
bot = commands.Bot(command_prefix='tp ')

c_id=937568599567130714 #put lambda channel id here
# server=bot.get_server(s_id)
@bot.event
async def on_ready():
    print('{0.user}'.format(bot))


# @bot.event
# async def on_message(message):

#     if message.author==bot.user:
#       return
#     # if message.content.startswith('send ```') and message.content.endswith('```'):
#     if message.content.startswith('send') :
#         id=random.randint(1000000,9999999)
#         x=message.content
#         i=x.find('```')
#         j=x.find('```',i+1)
#         # print(i,j)
#         # print(x[i:j+3])
#         channel = message.channel
#         await channel.send('id : '+ str(id))
#         channel=bot.get_channel(c_id)
#         await channel.send('id-'+str(id)+'\n'+x[i:j+3])
#     if message.content=='transporter help':
#       channel=message.channel
#       await channel.send('input format: send <codeblock>')
    
#     if message.content=='transporter dm':
#       try:
#         channel= message.author
#         await channel.send('hellooooo')
#       except:
#         await message.channel.send('open dms pls')


@bot.command()
async def dm(ctx):
  await ctx.author.send('hellloooo')

@bot.command()
async def post(ctx,*,code):
  try:
    id=random.randint(1000000,9999999)
    x=code
    i=x.find('```')
    j=x.find('```',i+1)
    if i==-1 or j==-1:
      await ctx.channel.send('better codeblock pls')
    # print(i,j)
      # print(x[i:j+3])
    else:
      channel = ctx.channel
      # print(channel)
      await channel.send('id : '+ str(id))
      channel=bot.get_channel(c_id)
      # print(channel)
      await channel.send('id-'+str(id)+'\n'+x[i:j+3])
  except:
    await ctx.channel.send('something went wrong')


keep_alive()
bot.run(os.environ['token2'])