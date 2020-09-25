import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
client = commands.Bot(command_prefix=".")
load_dotenv()
TOKEN = os.getenv('TOKEN')


@client.event
async def on_ready():
    drinkMsg.start()
    print('Bot is online.')


@tasks.loop(hours=1)
async def drinkMsg():
    channel = client.get_channel(694379147065163806)
    await channel.send('Remember to drink water :cup_with_straw: !')

if __name__ == '__main__':
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')


client.run(TOKEN)
