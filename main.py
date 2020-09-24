import discord
from discord.ext import commands
import requests
client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("Bot is ready.")


@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')


@client.event
async def on_message(message):
    trigger = ['nigger', 'nigga', 'nig', 'niga', "n*gger"]
    format = message.content.replace(" ", "").lower()
    if any(x in format for x in trigger):
        await message.channel.send("https://www.streamscheme.com/wp-content/uploads/2020/04/Cmonbruh.png.webp")


@client.command()
async def gay(ctx):
    await ctx.send("Why are you gay?")


@client.command()
async def pussy(ctx):
    payload = {"type": 'pussy'}
    r = requests.get('https://nekobot.xyz/api/image', params=payload)
    r_dist = r.json()
    await ctx.send(r_dist["message"])

client.run('NzU4MzU0MTg3NjQ5MTU1MTAy.X2tuXw.2EqSydlOFSZBfnVkik4jZpYNVbw')