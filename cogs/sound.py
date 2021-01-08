import discord
from discord.ext import commands
from discord.utils import get
import requests
import os
import time
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import asyncio


class Sound(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        return voice    
            
    @commands.command()
    async def dc(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)
        await voice.disconnect()


    @commands.command()
    async def ohaiyo(self, ctx):
        try:
            # callback
            voice = await ctx.invoke(self.join)

            # for HEROKU deploy
            voice.play(discord.FFmpegPCMAudio("song.mp3"), after=None)

            # for local debug
            # voice.play(discord.FFmpegPCMAudio(
            #     executable="C:/ProgramData/chocolatey/bin/ffmpeg.exe", source="song.mp3"), after=None)
            voice.volume = 100
            voice.is_playing()
            while voice.is_playing():
                time.sleep(1)
            else:
                await voice.disconnect()

        except AttributeError:
            await ctx.send("Haiya!! Join a voice channel first")

    # _songlist = asyncio.Queue()

    @commands.command(aliases=['p'])
    async def play(self, ctx, url:str):
        try:
            voice = await ctx.invoke(self.join)

            ydl_opts = {'format': 'bestaudio'}
            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                path = info['formats'][0]['url']
                title = info.get('title', None)

            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            voice.play(discord.FFmpegPCMAudio(path, **FFMPEG_OPTIONS), after=None)

            await ctx.send(f"Now Playing **{title}**")

            voice.volume = 100
            voice.is_playing()
            while voice.is_playing():
                time.sleep(1)
            else:                    
                await voice.disconnect()
                
        except AttributeError:
            await ctx.send("Haiya!! Join a voice channel first")

    @commands.command()
    async def stop(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_playing:
            await voice.stop()

def setup(client):
    client.add_cog(Sound(client))
