import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
import random
import asyncio
from keep_alive import keep_alive 

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))

#CANAL DE ROLES
@bot.command()
async def texto(ctx):
  # channel = bot.get_channel() #id?
  with open('/home/runner/mayol/roles/head.txt') as f:
    head = f.read()
    await ctx.channel.send(head)

# INVITE LINK

@bot.command(name='invitacion')
async def invitacion(ctx, *argument):
    invitelink = await ctx.channel.create_invite(max_age=86400,unique=True)
    await ctx.author.send('¡Aquí está el link de invitación al servidor que pediste! Debes usarlo en las siguientes 24 horas antes de que expire. ')
    await ctx.author.send(invitelink)

@bot.command()
async def rolespron(ctx):
  # channel = bot.get_channel()
  with open('/home/runner/mayol/roles/roles.txt') as f:
    addpron = f.read()
    pronouns = await ctx.channel.send(addpron)
    reactions = ['🥝', '🍓', '🍉']
    for i in reactions:
      await pronouns.add_reaction(i)

@bot.command()
async def delroles(ctx):
  # channel = bot.get_channel(801276868027482164)
  with open('/home/runner/mayol/roles/roles1.txt') as f:
    remroles = f.read()
    pronouns = await ctx.channel.send(remroles)
    reactions = ['1️⃣', '2️⃣', '3️⃣']
    for i in reactions:
      await pronouns.add_reaction(i)

@bot.event
async def on_raw_reaction_add(payload):
  user = payload.member

  if user == bot.user:
    return

  el = discord.utils.get(user.guild.roles, name="él")
  ella = discord.utils.get(user.guild.roles, name="ella")
  elle = discord.utils.get(user.guild.roles, name="elle/ele")

  if payload.channel_id == 801276868027482164:
    if payload.emoji.name =='🥝':
      await user.add_roles(el)
    elif payload.emoji.name =='🍓':
      await user.add_roles(ella)
    elif payload.emoji.name =='🍉':
      await user.add_roles(elle)
    elif payload.emoji.name =='1️⃣':
      await user.remove_roles(el)
    elif payload.emoji.name =='2️⃣':
      await user.remove_roles(ella)
    elif payload.emoji.name =='3️⃣':
      await user.remove_roles(elle)

#DRIVE
@bot.command()
async def drive(ctx):
  with open('/home/runner/mayol/ayuda/drive.txt') as f:
    drive = f.read()
    await ctx.channel.send(drive)

keep_alive()

bot.run(DISCORD_TOKEN)