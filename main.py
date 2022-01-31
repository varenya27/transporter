import os
from discord.ext import commands
import random
import json
from keep_alive import keep_alive
from datetime import date, datetime
bot = commands.Bot(command_prefix='tp ')
bot.sesh=1
bot.today= date.today()
bot.now= datetime.now()
bot.count=0
msg= bot.today.strftime("%d/%m/%Y")+' #'
c_id=937568599567130714 #put lambda channel id here
# server=bot.get_server(s_id)

with open('user.json','w')as f:
  d= {}
  json.dump(d,f)

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
  # try:
    if bot.today!=date.today():
      bot.today=date.today()
      bot.sesh=1
      #reset the sheet everyday
      with open('user.json','r+')as f:
        d= {}
        json.dump(d,f)
    with open('user.json','r+') as f:
      data=json.load(f)
      if ctx.message.author.name not in data:
        (data[ctx.message.author.name])={'id':'', 'message':[], 'count':0}
      (data[ctx.message.author.name])['id']=ctx.message.author.id
      (data[ctx.message.author.name])['message'].append(ctx.message.content)
      (data[ctx.message.author.name])['count']+=1
      bot.count=(data[ctx.message.author.name])['count']

      f.seek(0)
      json.dump(data, f, indent = 4)

    if bot.now.strftime("%M")==55:
      print('rude')
      bot.sesh=1
    x=code
    i=x.find('```')
    j=x.find('```',i+1)
    if i==-1 or j==-1:
      await ctx.channel.send('better codeblock pls')
    else:
      if bot.count>3:
        await ctx.channel.send('daily limit reached')
      else:
        channel = ctx.channel
        await channel.send('id : '+ msg+str(bot.sesh))
        channel=bot.get_channel(c_id)
        await channel.send(msg+str(bot.sesh)+'\n'+x[i:j+3])
        bot.sesh+=1

  # except:
  #   await ctx.channel.send('something went wrong')


keep_alive()
bot.run(os.environ['token2'])