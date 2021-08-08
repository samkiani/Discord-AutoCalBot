import discord
from discord.ext import commands
from persiantools.jdatetime import JalaliDate , JalaliDateTime
import datetime
from asyncio import sleep

class CONFIG:
    TOKEN = 'ODE1Njk2MzgzOTQ4NDg4NzQ2.YDwKdA.A_BiZpeVlK8cgfcHskO788bW3KQ' #str
    GUILD_ID = 857613550168309810 #int
    CHANNEL_ID = 857613550168309814 #int

client = discord.Client()


@client.event
async def on_ready():
    guild = client.get_guild(CONFIG.GUILD_ID)
    channel = guild.get_channel(CONFIG.CHANNEL_ID)
    await channel.connect()
    new_nick = str(JalaliDate.today())
    await guild.get_member(client.user.id).edit(nick = new_nick)
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching , name = 'Calendar ►►► Developed by ErfanNJZ'))
    print(JalaliDateTime.today().replace(microsecond = 0) ,'\n\nBot Online Shod XD\nDeveloped by ErfanNJZ')


client.run(CONFIG.TOKEN)