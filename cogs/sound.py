import discord
from discord.ext import commands
from discord.utils import get
import requests
import os
import time
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL


class Sound(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ohaiyo(self, ctx):
        try:
            channel = ctx.author.voice.channel
            voice = get(self.client.voice_clients, guild=ctx.guild)
            if voice and voice.is_connected():
                await voice.move_to(channel)
            else:
                voice = await channel.connect()

            voice.play(discord.FFmpegPCMAudio(
                executable="C:/ProgramData/chocolatey/bin/ffmpeg.exe", source="song.mp3"), after=None)
            voice.volume = 100
            voice.is_playing()
            while voice.is_playing():
                time.sleep(1)
            await voice.disconnect()
        except AttributeError:
            await ctx.send("Haiya!! Join a voice channel first")


def setup(client):
    client.add_cog(Sound(client))
