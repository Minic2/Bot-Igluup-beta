import discord
from discord.ext import commands
from discord.utils import get
import random
import datetime 
from urllib import parse, request
import re

bot = commands.Bot(command_prefix='-' , description= "Comando de Bot Igluup")
client = discord.Client()

@bot.command()
async def ping(ctx):
   await ctx.send('pong')

@bot.command()
async def saludar(ctx,user : discord.User):        
      await ctx.send("Saludos! " + user.mention )

@bot.command()
async def comandos(ctx):
   await ctx.send('Nuestros Comando\n'+'-saludar  - el bot saluda al user mencionado\n'+'-RMusic - te recomienda una musica al azar\n'+
   "-Avida - Adivina tu futuro")

@bot.command()
async def avida(ctx):
    id = random.randint(0,9)
    rad = ["Te vas a mudar a otro pais","Seras exitoso","Te tropezaras con un lego","Seras Calvo xdxdxd","Microsoft te contrata","Tienes cuenta paypal","Te compras un Hosting","El FBI te buscara","Compras Apple Inc.","Eres un chino mutante exiliado","Shrek te secuestrara"]
    await ctx.send(rad[id])
@bot.command()
async def gulag(ctx):
    id = random.randint(0,1)
    rad = ["Has perdido el gulag","Has ganado el gulag"]
    await ctx.send(rad[id])

@bot.command()
async def info(ctx):
    embed = discord.Embed(title =f"{ctx.guild.name}" , description="Informacion del server", timestamp=datetime.datetime.utcnow(), color= discord.Colour.dark_red())
    embed.add_field(name = "El server ha sido creado", value=f"{ctx.guild.created_at}")
    embed.add_field(name = "Server owner" , value=f"{ctx.guild.owner}")
    embed.add_field(name= "Server Region" , value=f"{ctx.guild.region}")
    embed.add_field(name= "Server ID" , value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://igluup.000webhostapp.com/img/igluu.png")
    await ctx.send(embed=embed)

@bot.command()
async def yt(ctx,*,search):
    query_string =  parse.urlencode({'search query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall("href=watch\?v=(\S{11})", html_content.read().decode())
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])
 
#Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="FLOU - alpha"))
    print('Perro estoy listo para los comandos')
# @bot.event
# async def on_message_delete(message, user : discord.User):
#     men = " el mensaje que ha enviado no esta permitido por nuestro server:("
#     await message.channel.send(user.mention + "{}".format(men))
# @bot.event
# async def on_message(message):
#     if message.content == "negro":
#         await message.delete()

bot.run('')
