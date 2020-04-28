import discord
from discord.ext import commands, tasks
from discord.utils import get
import os
import random
import json
import requests
import asyncio
from discord import FFmpegPCMAudio
from os import system
import youtube_dl
#OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']

#!PUT YOUR TOKEN HERE
TOKEN = "TOKEN"

client = commands.Bot(command_prefix=["Ricardo ","ricky ","Ricky ","ricardo ","RICKY "])
@client.event
async def on_ready():
    print("Unit01 is ready AF")
    await client.change_presence(status=discord.Status.online ,activity=discord.Game("Rainbow Six Siege"))
@client.event
async def on_member_join(member):
    print(f'{member} has joined the Test Zone. Welcome.')
@client.event
async def on_member_removed(member):
    print(f'{member} has left the Test Zone. Have a nice day {member}')
@client.command(alias="DOU")
async def dou(ctx):
    await ctx.send("DOOOOOOU AMIGO")
@client.command()
async def eu(ctx):
    await ctx.send("Que pasa boludo?")
@client.command()
async def gordo(ctx, *, args):
    if args == "teton":
        await ctx.send("chupala")
@client.command(aliases= ["8ball", "menem", "question", "question,"])
async def pregunta(ctx, *, question):
    responses = [
        "Extremely possible",
        "It's inminent",
        "It's very likely",
        "Unlikely",
        "Won't happen",
        "Are u nuts?",
        "No fucking way",
        "It's very possible",
        "Yes",
        "Perhaps",
        "Ni en pedo amigo jajaj",
        "I don't think so",

    ]
    await ctx.send(f'Question/Pregunta: {question}\nAnswer/Respuesta: {random.choice(responses)}')
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=6):
    await ctx.channel.purge(limit=amount)
@client.command()
async def ping(ctx):
    await ctx.send(f'Your ping is {round(client.latency*1000)}ms')
@client.command()
async def kick(ctx, member: discord.Member, *, reason = None):
    await member.kick(reason=reason)
@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} was banned. Go home pete.')
@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator=member.split("#")
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
#@tasks.loop(seconds=90)
#async def changing_status():
 #   await client.change_presence(activity=discord.Game(next(status)))
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("No te entendí capo.")

@client.command(aliases=["metete","adentro"])
async def join(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
        await ctx.send("Buenasss")
    else:
        await ctx.send("ni ganas,")
@client.command(aliases=["get"])
async def leave(ctx, *, args):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected or args == " the fuck out":
        await ctx.send("Ricardo Unidad01 fuera. Recuerden:VSCode es para trolos")
        print("Ricardo leaves channel")
        await voice.disconnect()
    else:
        print("Unidad01 fuera.")
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to puto el que lee!')
@client.command()
async def peruano(ctx):
    await ctx.send(f'{ctx.message.author.mention} peruano')
@client.command(manage_messages=True)
async def repeti(ctx, times: int, *, content):
    for i in range(times):
        await ctx.send(content)
@client.command(alias = ["issnow"])
async def ISSnow(ctx):
    f = requests.get(f'http://api.open-notify.org/iss-now.json')
    if f.status_code == 200:
        iss_response = json.loads(f.content)
        try:

            iss_latitude = iss_response["iss_position"]["latitude"]
            iss_longitude = iss_response["iss_position"]["longitude"]
            response= (f'ISS current position is on:\n Latitude: {iss_latitude}\n Longitude: {iss_longitude}')
            embed = discord.Embed(
                colour=discord.Color.dark_teal(),
                title=f"Positon of ISS",
                description=response)
            await ctx.send(embed=embed)
        except:
            await ctx.send("No se capo jaja")
@client.command(alias = ["isspassengers"])
async def ISSpassengers(ctx):
    f = requests.get(f'http://api.open-notify.org/astros.json')
    if f.status_code == 200:
        pas_reponse =json.loads(f.content)
        try:
            num= pas_reponse["number"]
            passenger1 = pas_reponse["people"][0]["name"]
            passenger2 = pas_reponse["people"][1]["name"]
            passenger3 = pas_reponse["people"][2]["name"]
            response = (f'Currently there are {num} passengers on board. They are: \n{passenger1},\n{passenger2},\n and {passenger3}.')
            embed = discord.Embed(
                colour=discord.Color.dark_purple(),
                title=f"Iss Passengers:",
                description=response)
            await ctx.send(embed=embed)
        except:
            await ctx.send("Ni idea maquina, disculpa.")
@client.command()
async def playE(ctx):
    await ctx.send("Okkk")
    guild = ctx.guild
    voice_client: discord.voice_client = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio("./songs/aa.mp3")
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)
@client.command(alias="stfu")
async def stop(ctx):
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    if voice_client.is_playing():
        voice_client.stop()

client.run(TOKEN)