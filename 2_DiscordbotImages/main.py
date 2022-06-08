import discord
import requests
import json
import os
from dotenv import load_dotenv

client = discord.Client()

def get_pic():
    response = requests.get("https://api.waifu.pics/sfw/waifu")
    data = json.loads(response.text)['url']
    return data

@client.event
async def on_ready():
    print('Logged on as {0.user}!'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user: 
        return
    if message.content.startswith('$pic'):
        pic = get_pic()
        await message.channel.send(pic)
load_dotenv()
client.run(os.getenv('TOKEN'))

# Token is gained from discord developer portal