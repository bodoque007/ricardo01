import discord
from discord.ext import commands
import os
import requests
import json
import random
import wikipedia
class APICommands(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("Unit01 is ready AF")
    @commands.command()
    async def Ping(self, ctx):
        await ctx.send("NEIN")
    @commands.command(aliases=["Estas", "estas",])
    async def listo(self, ctx,*,args):
        if args == 'listo?':
            await ctx.send("mas vale papá")
    @commands.command()
    async def restart(self, ctx):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                try:
                    self.client.unload_extension(f'cogs.{filename[:-3]}')
                except:
                    pass
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                try:
                    self.client.load_extension(f'cogs.{filename[:-3]}')
                except:
                    pass
        await ctx.send(f'Recargadisimo mono.')

    @commands.command()
    async def weather(self,ctx, *, data):
        OWKey = 'deea336dba07fe2d7a5c0c4f69662a96'
        f = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={data}&appid={OWKey}&units=metric&lang=es')
        if f.status_code == 200:
            dou_response = json.loads(f.content)
            try:
                weather = dou_response["weather"][0]["description"]
                temp = dou_response["main"]["temp"]
                wind = dou_response["wind"]["speed"]
                rick = (f'Clima: {weather}\nTemperatura: {temp}°C\nVientos: {wind}KM/H')
                embed = discord.Embed(
                    colour=discord.Color.blue(),
                    title=f"Weather in "+data+":",
                    description=rick)

                await ctx.send(embed=embed)
            except:
                await ctx.end("Shut the fuck up")
    @commands.command()
    async def mars(self,ctx,date):
        api_key = '44hd35BpK02KsbwRNjwtZ988egjtheC2zhWvU7tB'
        r = requests.get(f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={date}&api_key={api_key}')
        if r.status_code == 200:
            mars_response = json.loads(r.content)
            try:
                pic = mars_response["photos"][0]["img_src"]
                author = mars_response["photos"][0]["rover"]["name"]
                camera = mars_response["photos"][0]["camera"]["full_name"]
                picture = pic
                embed = discord.Embed(colour=discord.Colour.red(),title="Image found",description=f'Photo taken by {author}.\nCamera used: {camera}')
                embed.set_image(url=f'{pic}')
                await ctx.send(embed=embed)
            except:
                await ctx.send("Photo not found")
    @commands.command(aliases=["gif", "Gif", "GIF"])
    async def tenor(self, ctx, *, search):
        channel = ctx.channel
        random_number = random.randrange(0, 50)
        api_key = 'ZXECEQAWAPM1'
        img_url = ''
        r = requests.get(f'https://api.tenor.com/v1/search?q={search}&key={api_key}&limit=10')
        if r.status_code == 200:
            gif_url = json.loads(r.content)
        try:
            random_number = random.randrange(0, len(gif_url['results']))
            await ctx.send(
                f'{ctx.message.author.mention}, tu gif de {search}.{gif_url["results"][random_number]["url"]}')
        except:
            await ctx.send("No encontre nada de eso :(")
    @commands.command()
    async def lyrics(self,ctx,*, data):
        x=data.split(", ")
        r = requests.get(f'https://api.lyrics.ovh/v1/{x[0]}/{x[1]}')
        if r.status_code == 200:
            l_response = json.loads(r.content)
            try:
                lyric = l_response["lyrics"]
                embed = discord.Embed(
                    colour=discord.Color.dark_red(),
                    title=x[1].upper(),
                    description=lyric)
                await ctx.send(embed=embed)
            except:
                await ctx.send(f'Lyrics not found.')
    @commands.command()
    async def dict(self,ctx,*, word):
        headers = {
            'Authorization': "TOKEN e4adbb5a7c7d3cd8890b9e1871a6d9e2b81b6bf7"
        }
        r = requests.get(f'https://owlbot.info/api/v4/dictionary/{word}', headers=headers)
        if r.status_code == 200:
            dict_response = json.loads(r.content)
            try:
                meaning = dict_response["definitions"][0]["definition"]
                example = dict_response["definitions"][0]["example"]
                meaning= (f'Meaning of {word}:\n{meaning}\n Example: {example}')
                embed = discord.Embed(
                    colour=discord.Color.dark_red(),
                    title=f'Found {word} on database:',
                    description=meaning)
                await ctx.send(embed=embed)
            except:
                await ctx.send(f'bad word.')
    @commands.command()
    async def BB(self,ctx):
        r = requests.get(f'https://breaking-bad-quotes.herokuapp.com/v1/quotes')
        if r.status_code == 200:
            bb_response = json.loads(r.content)
            try:
                quote = bb_response[0]["quote"]
                author = bb_response[0]["author"]
                await ctx.send(f'{quote}\nSaid by: {author}')
            except:
                await ctx.send("nno se bro")
    @commands.command()
    async def derivative(self,ctx,*,calc):
        r = requests.get(f'https://newton.now.sh/derive/{calc}')
        if r.status_code ==200:
            der_response = json.loads(r.content)
            try:
                answer = der_response["result"]
                await ctx.send(f'Derivative of {calc} is:\n {answer}')
            except:
                await ctx.send(f"Couldn't do calculation")
    @commands.command()
    async def URSS(self,ctx):
            await ctx.channel.send(file=discord.File("./URSS.jpg"))

def setup(client):
    client.add_cog(APICommands(client))