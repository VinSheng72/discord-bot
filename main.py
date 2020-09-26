import discord
from discord.ext import commands, tasks
import os
client = commands.Bot(command_prefix="-")

msgId = None


@client.event
async def on_ready():
    drinkMsg.start()
    print('Bot is online.')


@tasks.loop(hours=1)
async def drinkMsg():
    global msgId
    # Live
    channel = client.get_channel(694379147065163806)

    # Test
    # channel = client.get_channel(758361628642246670)
    if msgId is not None:
        await client.http.delete_message(694379147065163806, msgId.id)
    msgId = await channel.send('Remember to drink water :cup_with_straw: !')


if __name__ == '__main__':
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')

# Heroku LIVE
#  client.run(os.environ['TOKEN'])

# DEBUG
client.run("NzU4OTAzMjc2NDQ2OTQxMTg0.X21twA.207fR9hkn_Q0eXhudnAMH4Bqi7s")
