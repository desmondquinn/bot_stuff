import discord
import os
import requests
import json 

client = discord.Client()

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

@client.event
async def on_message(message):
  url = get_url()
  if message.author == client.user:
    return
  if message.content.startswith('woof'):
    #await message.channel.send('bop bop')
    await message.channel.send(url)

client.run(os.getenv('TOKEN'))
