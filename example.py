import discord
import logging
import random
import io
import aiohttp
import os
import youtube_dl
import asyncio
from discord.ext import commands

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot('?', intents=intents, activity=discord.Game(name='Ys'))
candidatos = []
ruleta = False

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    user = await bot.fetch_user("325587406105477120")
    await user.send("mwah") 


@bot.event
async def on_message(message):
    global ruleta
    if message.author == bot.user:
        return
        
    if random.random() < 0.001:
      message.channel.send("https://cdn.discordapp.com/attachments/482309896776450048/1080601371092467863/IMG_8025.png")
    if random.random() < 0.002:
      message.channel.send("https://cdn.discordapp.com/attachments/482309896776450048/1080601380533850173/IMG_8026.png")
      
    if message.author.id == 465581283465232406:
      if random.random() < 0.005:
        rand = random.random()
        if rand < 0.33:
          await message.channel.send('chapa la boca (tq)')
        if rand > 0.33 and rand < 0.66:
          await message.channel.send('no te soporto (tq)')
        if rand > 0.66:
          await message.channel.send("https://tenor.com/view/me-when-dragon-quest-slime-meme-haha-gif-19829441")
          
    if message.author.id == 626175514851409950:
      if random.random() < 0.005:
        await message.channel.send('maricon con acento en la o')
        
    if message.author.id == 325587406105477120:
      emoji = discord.utils.get(bot.emojis, name='aaaaaaaaaaaaaaa')
      emoji2 = discord.utils.get(bot.emojis, name='lauralooks')
      if random.random() < 0.005:
        await message.add_reaction(str(emoji))
      if random.random() < 0.005:
        await message.add_reaction(str(emoji2))
      if random.random() < 0.01:
        await message.add_reaction("✅")
      if random.random() < 0.02:
        await message.add_reaction("🏳️‍🌈")
      if random.random() < 0.01:
        await message.add_reaction("🤓")
      if random.random() < 0.01:
        await message.add_reaction("☝️")
    
    if message.author.id == 478507439814082561:
      if random.random() < 0.005:
        await message.channel.send('pero y la de trabajar te la sabes?')
        
    if message.author.id == 265145474951020544:
      if random.random() < 0.005:
        await message.channel.send('cómo van esos romantic oomfies dekoperros?')
        
    if message.author.id == 413459503028240389:
      if random.random() < 0.005:
        await message.channel.send('gay + gay = gay^2')



        
    if message.content.lower() == 'cope':
      async with aiohttp.ClientSession() as session:
          async with session.get('https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/ezgif-2-bf9235ae95.gif?v=1658245352648') as resp:
              if resp.status != 200:
                  return await message.channel.send('Could not download file...')
              data = io.BytesIO(await resp.read())
              await message.channel.send(file=discord.File(data, 'cool.gif'))

    if 'ys' in message.content.lower().split():
      if random.random() < 0.30:
          await message.channel.send('PICO DA FICÇÃO')
    if 'trails' in message.content.lower().split():
      if random.random() < 0.30:
          await message.channel.send('estelle is bestelle')
             
    if 'mayufiesta' in message.content.lower().split():
      emoji = discord.utils.get(bot.emojis, name='mayufiesta')
      await message.channel.send(str(emoji))

      
    if 'chao' in message.content.lower().split() or 'chaos' in message.content.lower().split():
      chaos=('https://tenor.com/view/oomfie-twitter-mya-birdy-moots-gif-21653749', 
             'https://tenor.com/view/oomfie-twitter-mya-birdy-moots-gif-21654146',
            'https://tenor.com/view/oomfie-twitter-mya-birdy-moots-gif-21654131',
            'https://tenor.com/view/oomfie-twitter-mya-birdy-moots-gif-21654710',
            'https://tenor.com/view/chao-sonic-suicide-pact-ecco2k-gif-26110792',
            'https://tenor.com/view/chao-chao-garden-sonic-sonic-chao-cepe-chao-gif-26092692',
            'https://tenor.com/view/sonic-chao-chao-sonic-sonic-sonic-the-hedgehog-shadow-chao-gif-23946468',
            "https://tenor.com/view/chao-sonic-sa2-sonic-adventure2-chaos-gif-25303563",
            "https://tenor.com/view/sonic-chao-amy-rose-sonic-adventure-cute-petting-sonic-chao-gif-20180724",
            "https://tenor.com/view/chao-chao-garden-sonic-sonic-chao-jerma-gif-26172357",
            "https://tenor.com/view/chao-sonic-doll-sonic-adventure-happy-chao-sonic-doll-adventure-gif-20180493",
            "https://tenor.com/view/chao-happy-chao-sonic-happy-dance-dancing-gif-25729360",
            "https://tenor.com/view/chao-sonic-tails-cute-food-gif-19963890",
            "https://tenor.com/view/chao-garden-chao-sonic-we-dont-care-meme-ratio-playing-gif-26069397",
            "https://tenor.com/view/sonic-chao-chao-sonic-chao-gif-24626313")
      await message.channel.send(random.choice(chaos))
      
    if 'poggers' in message.content.lower().split():
      await message.channel.send("https://pbs.twimg.com/media/EXbhWXLWsAAErj_.jpg")

    """
    if ((message.content == "yo") and (ruleta)):
        global candidatos
        candidatos.append(message.author.id)
        await message.channel.send("Prepárate " + message.author.display_name)

    if(message.content == "!ruleta"):
        await message.channel.send("Tienen 60 segundos para apuntarse diciendo yo, empezando ya")
        candidatos = []
        ruleta = True
        await asyncio.sleep(60)        
        expulsion = random.randint(0, len(candidatos)-1)
        expulsao = message.guild.get_member(candidatos[expulsion])
        await message.channel.send("Que te jodan, " + expulsao.display_name)
        await message.guild.kick(message.guild.get_member(candidatos[expulsion]), reason=None)
        ruleta = False

    if(message.content == "!genocida"):
        await message.channel.send("Espero no echar a Dixeo")
        todos = list(message.guild.members)
        await asyncio.sleep(5)        
        expulsion = random.randint(0, len(todos)-1)
        expulsao = message.guild.get_member(todos[expulsion].id)
        print(expulsao)
        await message.channel.send("Que te jodan, " + expulsao.display_name)
        await message.guild.kick(message.guild.get_member(expulsao.id), reason=None)
   """
        
    await bot.process_commands(message)
    
@bot.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)
    
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename
      
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    
'''
@bot.command()
async def play(ctx):
    try :
        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            filename = await YTDLSource.from_url('https://www.youtube.com/watch?v=WKvUE7LB3Js', loop=bot.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
        await ctx.send('**Now playing:** {}'.format(filename))
    except:
        await ctx.send("The bot is not connected to a voice channel.")
'''
    
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    
@bot.command()
async def playyt(ctx, url):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        em8 = discord.Embed(title = "Music is currently playing", description = 'Please wait for the current playing music to end or use ?leave',color = ctx.author.color)
        await ctx.send(embed = em8)
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels)
    await voiceChannel.connect()
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    temp_song = "https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/Neutral%20Garden.mp3?v=1674950631866"
    voice.play(discord.FFmpegPCMAudio(temp_song))
    em6 = discord.Embed(title = "Downloading Youtube Music", description = f'{url}\n\nPlease wait for Lyra.',color = ctx.author.color)
    await ctx.send(embed = em6, delete_after = 2)
    await ctx.message.delete()

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '196',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.stop()
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    em1 = discord.Embed(title = "Now Listening", description = f'{url}\n\nPlease use ?leave first to change music.',color = ctx.author.color)

    videoID = url.split("watch?v=")[1].split("&")[0]

    em1.set_thumbnail(url = f'https://img.youtube.com/vi/{videoID}/default.jpg'.format(videoID = videoID))
    await ctx.send(embed = em1)
    
@bot.command()
async def stop(ctx):
    await ctx.voice_client.stop()
    
@bot.command()
async def pause(ctx):
    await ctx.voice_client.pause()
    
@bot.command()
async def resume(ctx):
    await ctx.voice_client.resume()
    
@bot.command()
async def surprise(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    song = 'https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/song.mp3?v=1674781173433'
    voice.play(discord.FFmpegPCMAudio(song))
    
@bot.command()
async def chao(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    temp_song = "https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/Neutral%20Garden.mp3?v=1674950631866"
    voice.play(discord.FFmpegPCMAudio(temp_song))
    
@bot.command()
async def yippie(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    temp_song = "https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/Sena%20Yippee%20(No%20music%20or%20Sound%20Effects).mp3?v=1676243559569"
    voice.play(discord.FFmpegPCMAudio(temp_song))
    
@bot.command()
async def maricones(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    temp_song = "https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/SnapSave.io%20-%20Dreams%20Of%20An%20Absolution%20(LB%20vs%20JS%20Remix)%20(128%20kbps).mp3?v=1677094279296"
    voice.play(discord.FFmpegPCMAudio(temp_song))
    
@bot.command()
async def musicade(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    temp_song = "https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/SnapSave.io%20-%20Dreams%20of%20An%20Absolution%20-Theme%20of%20Silver%20The%20Hedgehog-%20(128%20kbps).mp3?v=1677094360206"
    voice.play(discord.FFmpegPCMAudio(temp_song))
    
@bot.command()
async def ys(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    temp_song = "https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/SnapSave.io%20-%20Ys%20VIII%20-Lacrimosa%20of%20DANA-%20OST%20-%20Sunshine%20Coastline%20(128%20kbps).mp3?v=1677094339931"
    voice.play(discord.FFmpegPCMAudio(temp_song))
    
@bot.command()
async def trails(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    temp_song = "https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/SnapSave.io%20-%20Sen%20no%20Kiseki%20Super%20Arrange%20Version%20-%20The%20Decisive%20Collision%20(128%20kbps).mp3?v=1677094851678"
    voice.play(discord.FFmpegPCMAudio(temp_song))

@bot.command()
async def sranktrauma(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    temp_song = "https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/SnapSave.io%20-%20Sonic%20Frontiers%20-%20Cyber%20Space%201-2_%20Flowing%20(128%20kbps).mp3?v=1677094824050"
    voice.play(discord.FFmpegPCMAudio(temp_song))

@bot.command()
async def teamosupersonic(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    temp_song = "https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/SnapSave.io%20-%20Sonic%20Frontiers%20OST%20-%20Find%20Your%20Flame%20(128%20kbps).mp3?v=1677094866443"
    voice.play(discord.FFmpegPCMAudio(temp_song))
    
async def auxsong(ctx, song):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio(song))
    
@bot.command()
async def enfundatuvenganza(ctx):
    await auxsong(ctx, 
    "https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/y2mate.com_-_Unfounded_Revenge_Smashing_Song_of_Praise_Super_Smash_Bros_Ultimate_Soundtrack.mp3?v=1677095252922"
                 )
    
@bot.command()
async def carnavalfiesta(ctx):
    await auxsong(ctx, 
    "https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/Carnival_Night_Zone_Act_1_-_Sonic_the_Hedgehog_3_OST.mp3?v=1677095975799"
                )
    
@bot.command()
async def bajadeltechoniña(ctx):
    await auxsong(ctx, 
                  "https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/y2mate.com_-_Rooftop_Run_Day_Sonic_Unleashed_OST.mp3?v=1677096003354"
                 )
    
@bot.command()
async def ladrondemadres(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/y2mate.com_-_Mind_of_a_Thief_MOTHER_3_OST.mp3?v=1677095990457"
                 )
    
@bot.command()
async def derrotameesta(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/Undefeatable_-_Sonic_Frontiers_OST_High_Quality.mp3?v=1677096358965"                  
                 )
    
@bot.command()
async def GLADIOOON(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/y2mate.com_-_Pokemon_Sun_Moon_Gladion_Battle_Music_Highest_Quality.mp3?v=1677096344516"                  
                 )
    
@bot.command()
async def sexmusic(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/You_Will_Know_Our_Names_-_Xenoblade_Chronicles__Definitive_Edition_Music.mp3?v=1677096345917"                  
                 
                 )  

@bot.command()
async def posibilidades(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/y2mate.com_-_Endless_Possibility_Sonic_Unleashed_OST.mp3?v=1677096623417"                 
                 )  
@bot.command()
async def viveyaprende(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/Live_and_Learn_by_Crush_40_Main_Theme_of_SA2.mp3?v=1677096624916"                 
                 )  
    
@bot.command()
async def sumundito(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/y2mate.com_-_His_World_Theme_of_Sonic_The_Hedgehog.mp3?v=1677096627678"                 
                 )  
    
@bot.command()
async def plsimastar(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/y2mate.com_-_Reach_for_the_Stars_Opening_Theme_Sonic_Colors_OST.mp3?v=1677096628367"                 
                 )  
    
@bot.command()
async def itsnouse(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/Sound_Effect_Silver_-_Its_No_Use.mp3?v=1677096628586"                 
                 )  

@bot.command()
async def caballerodelviento(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/y2mate.com_-_Knight_of_the_Wind_Sonic_and_the_Black_Knight_OST.mp3?v=1677096631705"                 
                 
                 )  
    
@bot.command()
async def estoyhecho(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/What_Im_Made_Of....mp3?v=1677096632143"                 
                 )  

@bot.command()
async def geis(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/SnapSave.io%20-%20CROSSING%20RAGE!%20(Ys%20SEVEN)%20(128%20kbps).mp3?v=1677097074332"                 
                 )  
@bot.command()
async def chosdeko(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/y2mate.com_-_Team_Chaotix_Sonic_Heroes_OST.mp3?v=1677097079904"                 
                 )  
@bot.command()
async def azulcomoelmar(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/SnapSave.io%20-%20Inevitable%20Struggle%20(128%20kbps).mp3?v=1677097083962"                 
                 )  
@bot.command()
async def silver(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/SnapSave.io%20-%20Sora%20no%20Kiseki%20FC%20%26%20SC%20Super%20Arrange%20Version%20-%20Silver%20Will%20(128%20kbps).mp3?v=1677097090271"                 
                 )  
@bot.command()
async def jueguenys(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/SnapSave.io%20-%20Ys%20Origin%20Super%20Arrange%20Version%20-%20Over%20Drive%20(128%20kbps).mp3?v=1677097159061"                 
                 
                 )  
    
@bot.command()
async def tropicure(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/SnapSave.io%20-%20%5B1080p%5DTropical-Rouge%20Precure%20Opening%201%20(128%20kbps).mp3?v=1677097494493"                 
                 )  
@bot.command()
async def miasma(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/T_H_E_M_I_A_S_M_A_Tales_of_the_Abyss.mp3?v=1677097499223"                 
                 )  
    
@bot.command()
async def kratosteamo(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/SnapSave.io%20-%20Tales%20of%20Symphonia%20-%20Kratos'%20theme%20(128%20kbps).mp3?v=1677097858223"                 )  
    
@bot.command()
async def findelpensamiento(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/Tales_of_Symphonia_Soundtrack__End_of_a_Thought.mp3?v=1677097996926"                 
                 )  

@bot.command()
async def espiritufusfus(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/Tales_of_Symphonia_Music-_Fighting_of_the_Spirits.mp3?v=1677098244676"                 
                 )  
    
@bot.command()
async def kanarazu(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/PS2_Tales_of_the_Abyss_OP.mp3?v=1677098248757"                 
                 )  
    
@bot.command()
async def tuturara(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/1-21_Paulownian_Mall.mp3?v=1677100363951"                 )  
    
@bot.command()
async def myangeloffate(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/SnapSave.io%20-%20Bravely%20Default%20-%20Flying%20Fairy%20OST%20-%2027%20Love's%20Vagrant%20(128%20kbps).mp3?v=1677269254269"                 
                 )  
@bot.command()
async def teamometaknight(ctx):
    await auxsong(ctx, 
"https://cdn.glitch.global/4481df25-2b21-46d9-8f45-e8f30e142960/SnapSave.io%20-%20Friends%20and%20Sun%20-%20Kirby%20Super%20Star%20Ultra%20(128%20kbps).mp3?v=1677269256020"                 
                 )  
@bot.command()
async def say(ctx, *, text):
  if ctx.message.author.id == 303617564607643648:
    await ctx.message.delete()
    await ctx.send(text)
  else:
    await ctx.send("casi pero no")

'''
@bot.command(name="poyo")
@commands.cooldown(1, 86400, commands.BucketType.guild)
async def poyo(ctx):

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)
'''

bot.run('OTk4NTkzMjc2NTgyMDM1NTE2.GZ20hH.1m1tACUHF0zc4rzd_MErDTOxKNolBBx2-spr7Y')