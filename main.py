import discord
import os
from discord.ext import commands, tasks
from globals import metal_channel

client = commands.Bot(command_prefix=".")

msgId = None


@client.event
async def on_ready():
    drinkMsg.start()
    print('Bot is online.')


@tasks.loop(hours=1)
async def drinkMsg():
    global msgId
    channel = client.get_channel(metal_channel)
    if msgId is not None:
        await client.http.delete_message(metal_channel, msgId.id)

    msgId = await channel.send('Remember to drink water :cup_with_straw: !')


if __name__ == '__main__':
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')

# ADD TOKEN TO ENV VARIABLE
client.run(os.environ['TOKEN'])
