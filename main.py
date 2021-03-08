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

# INVITE LINK
@bot.command(name='invitacion')
async def invitacion(ctx, *argument):
    invitelink = await ctx.channel.create_invite(max_age=86400,unique=True)
    await ctx.author.send('Aquí está el link de invitación al servidor que pediste. Debes usarlo en las siguientes 24 horas antes de que expire. ')
    await ctx.author.send(invitelink)

#CANAL DE ROLES
@bot.command()
async def texto(ctx):
  with open('/home/runner/mayol/roles/head.txt') as f:
    head = f.read()
    await ctx.channel.send(head)


@bot.command()
async def rolespron(ctx):
  with open('/home/runner/mayol/roles/roles.txt') as f:
    addpron = f.read()
    pronouns = await ctx.channel.send(addpron)
    reactions = ['🥝', '🍓', '🍉']
    for i in reactions:
      await pronouns.add_reaction(i)

@bot.command()
async def delroles(ctx):
  with open('/home/runner/mayol/roles/roles1.txt') as f:
    remroles = f.read()
    pronouns = await ctx.channel.send(remroles)
    reactions = ['1️⃣', '2️⃣', '3️⃣']
    for i in reactions:
      await pronouns.add_reaction(i)

@bot.command()
async def ayuda(ctx):
  await ctx.channel.send('Estos son los comandos que puedes usar en el servidor:\n\n**!drive**: Link de la carpeta de Drive.\n**!invitacion**: Envía un DM con un link de invitación al server que caduca en 24 horas.')

@bot.event
async def on_raw_reaction_add(payload):
  user = payload.member

  if user == bot.user:
    return

  el = discord.utils.get(user.guild.roles, name="él")
  ella = discord.utils.get(user.guild.roles, name="ella")
  elle = discord.utils.get(user.guild.roles, name="elle")

  if payload.channel_id == 816881384776794143:
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

@bot.command()
async def resumen(ctx):
  await ctx.channel.send('!texto: manda texto inicial para canal de roles\n!rolespron: manda texto con reacciones para agregar roles\n!delroles: manda texto con reacciones para eliminar roles\n**enviar los tres anteriores en orden**\n\n!invitacion: envía dm con link de invitación al server\n!drive: envía mensaje con link del drive\n\nFALTA: nombres exactos de los roles como estén en tu server, link del drive')

keep_alive()

bot.run(DISCORD_TOKEN)