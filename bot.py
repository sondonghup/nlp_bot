import discord
from discord.ext import commands
import requests
import googleapiclient.discovery
import yt_dlp as youtube_dl
from dotenv import load_dotenv
import time
from melonapi import scrapeMelon
import json
import os

from funcs.food_func import food_list
from funcs.weather_func import get_region_daily_weather, get_region_week_weather, get_all_region_weather

TOKEN = os.environ['discord_token']
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = os.environ['youtube_api_key']
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)

load_dotenv()
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

class youtube_quiz:
    def __init__(self, quizUIFrame, voice, owner) -> None:
        self._quizUIFrame = quizUIFrame
        self._voice = voice
        self._owner = owner
        
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
    print(response3)
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
    await ctx.send(f'{player}')

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

@ bot.command()
async def food(ctx, *, player):
    if player == '':
        await ctx.send('지역을 입력해 주세요')
    else :
        response = food_list(player)
        restaurant_list = ''
        response = sorted(response['restaurants'], key= lambda x: x['distance'])
        for restaurant in response:
            name = restaurant['name']
            distance = restaurant['distance']
            review_avg = restaurant['review_avg']
            restaurant_list += f'[{name}] 평점 : {review_avg} 거리 : '+'{0:.1f}'.format(distance)+'km\n'
        await ctx.send(restaurant_list)

@ bot.command()
async def weather(ctx, *, player):
    if player == '':
        await ctx.send('전국 날씨는 $weather 전국, 지방 날씨는 $weather 주소 로 입력해주세요.')
    elif player == '전국':
        all_region_weather = get_all_region_weather()
        weathers = ''
        for area in all_region_weather.keys():
            region = all_region_weather[area]['regionName']
            temperature = all_region_weather[area]['tmpr']
            weather = all_region_weather[area]['wetrTxt']
            weathers += f'[{region}] 기온 : {temperature} | 날씨 : {weather}\n'
        await ctx.send(weathers)

    else:
        region_daily_weather = get_region_daily_weather(player)
        await ctx.send(region_daily_weather)

@ bot.command()
async def weekweather(ctx, player):
    region_week_weather = get_region_week_weather(player)
    await ctx.send(region_week_weather)

@bot.command()
async def summary(ctx,*,player):
    '''
    [summarization]
    '''
    url = "http://localhost:8002/summarize"
    data = {"text": f"{player}"}
    response = requests.post(url, json=data)
    await ctx.channel.send('[요약 입니다.]\n' + response.json()['summarizing'])

@ bot.command()
async def quit(ctx, player):
    channel = ctx.message.author.voice.channel
    await channel.disconnect()

bot.run(TOKEN)