import discord
from discord.ext import commands
from persiantools.jdatetime import JalaliDate , JalaliDateTime
import datetime
from asyncio import sleep

class CONFIG:
    TOKEN ='OTI2ODI0ODM2MTQyMDg0MTE4.YdBS5A.1x5_pMblFctapdFRRgMyN_eACw0' #str
    GUILD_ID = 926824836142084118 #int
    CHANNEL_ID = 926828389145382922 #int

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