#!/usr/bin/python
from time import strftime, localtime
import asyncio
import re
import datetime
import discord
from discord.ext import commands

''' Path to the log directory '''
logdir = ''
''' Your bot API token '''
token = '<YOUR-TOKEN>'
''' Path to the URL where your pisg stats will be published '''
statsUrl = ''
''' Command prefix '''
commandPrefix = '!'

''' --- DO NOT CHANGE BELOW --- '''

bot = commands.Bot(command_prefix=commandPrefix)

@bot.event
async def on_ready():
    welcome = "Logged in as {0.name} - {0.id}\n".format(bot.user)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="statistics games"))
    print(welcome)

async def format_message_mbot(message):
    # Log in mbot format for pisg compatibility
    timestamp = strftime("%a %b %d %H:%M:%S %Y", localtime())
    log = "{1} <{0.author}> {0.content}".format(message, timestamp)
    if message.attachments:
	# Translates images to an url
        img = message.attachments[0]['url']
        log += " {}".format(img)

    return log

def write(log, _file):
    print(log, file=open(_file, "a", encoding="utf-8"))

async def log_discord(message, _file):
    log = await format_message_mbot(message)
    write(log, logdir + _file)

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
		
	if message.content.startswith(commandPrefix + "stats"):
		await message.channel.send(statsUrl)
	
	# Filter our special characters for channel names
	chan_plain = re.search(r'([a-zA-Z-]+)', message.channel.name)	
	await log_discord(message, "discordlog" + "_" + chan_plain.group())

if __name__ == "__main__":
    bot.run(token)
