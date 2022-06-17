# Usage
# $waifu for waifu pics
# $cry for crying pics

import discord
import requests
import json
import os
from dotenv import load_dotenv

client = discord.Client()

def get_waifu():
    response = requests.get("https://api.waifu.pics/sfw/megumin")
    waifu = json.loads(response.text)['url']
    return waifu
def get_cry():
    response = requests.get("https://api.waifu.pics/sfw/cry")
    cry = json.loads(response.text)['url']
    return cry
# def get_nsfw():
#     response = requests.get("https://api.waifu.pics/nsfw/waifu")
#     nsfw = json.loads(response.text)['url']
#     return nsfw
@client.event
async def on_ready():
    print('Logged on as {0.user}!'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user: 
        return
    if message.content.startswith('$waifu'):
        pic = get_waifu()
        await message.channel.send(pic)
    if message.content.startswith('$cry'):
        pic = get_cry()
        await message.channel.send(pic)
    # if message.content.startswith('$nsfw'):
    #     pic = get_nsfw()
    #     await message.channel.send(pic)
load_dotenv()
client.run(os.getenv('TOKEN'))

# Token is gained from discord developer portal