import discord
from discord.ext import commands
import requests
import googleapiclient.discovery
import yt_dlp as youtube_dl
from dotenv import load_dotenv
from datetime import datetime
import time
from discord import Embed
from melonapi import scrapeMelon
import json

TOKEN = '입력'
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = '입력'
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)

load_dotenv()
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')


@bot.command()
async def sent(ctx,*,player):
    '''
    [sentiment classification]
    '''
    url = "http://localhost:8000/sent"
    data = {"text": f"{player}"}
    response = requests.post(url, json=data)

    await ctx.channel.send(response.json()['sentiment'])


@bot.command()
async def chat(ctx,*,player):
    '''
    [chat bot]
    '''
    start = time.time()
    url = "http://localhost:8001/chat"
    data = {"text": f"{player}"}
    response = requests.post(url, json=data)
    end = time.time()
    print(player + response.json()['chatting'])
    

    await ctx.send(f'[{end-start}초가 걸립니다.]\n'+response.json()['chatting'])


@ bot.command()
async def play(ctx, *,player):
    output2 = ''
    print(f"args : {player}")
    output2 = player
    print(f"output2 {output2}")
    request3 = youtube.search().list(
        q = f"{output2}",
        order = 'viewCount',
        part="snippet",
        maxResults = 1
    )
    response3 = request3.execute()
    chan_id = response3['items'][0]['id']['videoId']
    ydl_opts = {'format' : 'bestaudio'}
    player = f'https://www.youtube.com/watch?v={chan_id}'
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5 -re', 'options': '-vn'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl: # 일시적 해결
        info = ydl.extract_info(player, download=not True)
        URL = info['formats'][3]['url']
    discord.opus.load_opus('libopus.0.dylib')
    voice = bot.voice_clients[0]
    voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))


@ bot.command()
async def join(ctx):
    if bot.voice_clients == []:
        channel = ctx.message.author.voice.channel
        print(f'channel : {channel}')
        await channel.connect()
        await ctx.send(f'connected to the voice channel {channel}')

@ bot.command()
async def game(ctx, *, player):
    if bot.voice_clients == []:
        channel = ctx.message.author.voice.channel
        print(f'channel : {channel}')
        await channel.connect()
        await ctx.send(f'노래 맞추기 게임을 시작 합니다. ')

    response = scrapeMelon.getList("DAY").decode()
    response = json.loads(response)
    music_list = []
    for music_info in response.keys():
        del response[music_info]['ranking']
        del response[music_info]['songId']
        del response[music_info]['albumId']
        music_list.append(response[music_info])
    # music_list = list(set(music_list)) 
    for music in music_list[:3]:
        music = music['name']
        print(music)
        request3 = youtube.search().list(
            q = f"{music}",
            order = 'viewCount',
            part="snippet",
            maxResults = 1
        )
        response3 = request3.execute()
        chan_id = response3['items'][0]['id']['videoId']
        ydl_opts = {'format' : 'bestaudio'}
        player = f'https://www.youtube.com/watch?v={chan_id}'
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5 -re', 'options': '-vn'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl: # 일시적 해결
            info = ydl.extract_info(player, download=not True)
            URL = info['formats'][3]['url']
        discord.opus.load_opus('libopus.0.dylib')
        voice = bot.voice_clients[0]
        voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        time.sleep(40)
        if player == music:
            print('정답입니다!')
            continue

async def countdown(isLong): # 카운트 다운
    leftsec = 40





@ bot.command()
async def weather(ctx):
    weathers = ''
    today = datetime.today().strftime('%Y%m%d')
    url = f'https://weather.naver.com/today/api/nation/{today}/now'
    response = requests.get(url)
    result = response.json()
    
    for area in result.keys():
        region = result[area]['regionName']
        temperature = result[area]['tmpr']
        weather = result[area]['wetrTxt']
        weathers += f'[{region}] 기온 : {temperature} | 날씨 : {weather}\n'
        print(f'[{region}] 기온 : {temperature} 날씨 : {weather}')
    await ctx.send(weathers)

@ bot.command()
async def test(ctx):
    juice=discord.Embed(color=0x3498db)
    juice.set_author(name="Please wait")
    # juice5=discord.Embed(title="⚠️ Error, are you trying to ban anyone?", description="Usage: !ban @user (reason)", color=discord.Colour.gold())
    msg = await ctx.send(embed=juice)
    # await msg.edit(embed=juice5)

@ bot.command()
async def on_ready(ctx):
    print('VC is online!')
    embed = discord.Embed(title="Screenshare", description="Cilck this link to screenshare", colour=discord.Color.blue(), url=f"https://discordapp.com/channels/{ctx.guild.id}/{ctx.author.voice.channel.id}")

    embed.add_field(name="Screenshare here", value=f"https://discordapp.com/channels/{ctx.guild.id}/{ctx.author.voice.channel.id}")
    # embed.set_thumbnail(url=doob_logo)

    await ctx.send(embed=embed)





@ bot.command()
@ commands.cooldown(1, 4, commands.BucketType.user)
async def info(ctx, *args):
    output2 = ''
    print(f"args : {args}")
    for word in args:
        output2 += str(word)
        output2 += ' '
        print(output2)
    request3 = youtube.search().list(
        q = f"{output2}",
        order = 'rating',
        part="snippet",
        maxResults = 1
    )
    response3 = request3.execute()
    print(response3)
    channame = response3['items'][0]['snippet']['title']
    chanid = response3['etag']
    dsc = response3['items'][0]['snippet']['description']
    embed2 = discord.Embed(title=f"{channame}", url=f"https://www.youtube.com/watch?v={chanid}",
                          description=f"{dsc}", color=0xFF5733)
    # response3 = request3.execute()
    # embed2.add_field(text=f"Made By Riceblades11")
    await ctx.send(embed=embed2)


@ bot.command()
@ commands.cooldown(1, 30, commands.BucketType.user)
async def search(ctx, *args):
    output = ''
    for word in args:
        output += str(word)
        output += ' '
    request = youtube.search().list(
        part="id,snippet",
        type='video',
        q=f"{output}",
        videoDuration='short',
        videoDefinition='high',
        maxResults=1,
        fields="nextPageToken,items(id(videoId),snippet(publishedAt,channelId,channelTitle,title,description))"
    )
    response = request.execute()
    print(response)
    await ctx.send(response)
    chan = response['items'][0]['snippet']['channelId']
    title = response['items'][0]['snippet']['title']
    idd = response['items'][0]['id']['videoId']
    dsc = response['items'][0]['snippet']['description']
    embed = discord.Embed(title=f"{title}", url=f"https://www.youtube.com/watch?v={idd}",
                          description=f"{dsc}", color=0xFF5733)
    # embed.set_image(
    #     url=f"https://i.ytimg.com/vi/{idd}/mqdefault.jpg")
    request2 = youtube.channels().list(
        part="snippet",
        id=f"{chan}",
    )
    response2 = request2.execute()
    pfp = response2['items'][0]['snippet']['thumbnails']['default']['url']
    name = response2['items'][0]['snippet']['localized']['title']
    embed.set_author(
        name=name, url=f"https://www.youtube.com/channel/{chan}", icon_url=pfp)
    # embed.set_footer(text="Made By Riceblades11")
    view = DropdownView(idd)
    await ctx.send(embed=embed, view=view)


class Dropdown(discord.ui.Select):
    def __init__(self, idd):
        self.idd = idd
        options = [
            discord.SelectOption(
                label='Link', description='Click for YouTube Link', emoji='🟥'),
        ]
        super().__init__(placeholder='Pick Option',
                         min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Link: https://www.youtube.com/watch?v={self.idd}', ephemeral=True)

class DropdownView(discord.ui.View):
    def __init__(self, idd):
        super().__init__()
        self.add_item(Dropdown(idd))



@ bot.command()
async def quit(ctx, player):
    channel = ctx.message.author.voice.channel
    await channel.disconnect()





bot.run(TOKEN)