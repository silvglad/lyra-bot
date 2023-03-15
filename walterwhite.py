from array import array
import discord
import aiohttp
import datetime
import warnings
from discord import Member
from discord.ext    import commands
from discord.ext.commands   import Bot, has_permissions, MissingPermissions
import random
import time
import aioconsole
import asyncio
import sys
import multiprocessing
import os
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot('!', intents=intents, activity=discord.Game(name='Silvia guarra'))
array_ratios = ["ratio", "r palabra","RATlO"] 
gallotrap = ['gallotrap', 'gallo trap']
tigrerasta = ["tigrerasta", "tigrasta"]
bena = ["benamomento", "bena"]
emojis = ['👍',':tigrerasta:941000059795939339', 'a:bena:948200095415955506', '🤙']
pregunta= ['quien te pregunto', 'pregunto', 'preguntado']
sustancias = ['crotolamo', 'uxiono', 'obo', 'trujo','acudo', 'aboreo', 'permatrago', 'orbo', 'primo', 'oplo', 'cupo', 'nifo', 'padalustro', 'tiro', 'crotofroto', 'timulo']
respuestas = ['este','esta','esto']
padreada = ['padreada', 'jodienda', 'jodieron', 'jodeme']
dromedario = ["joroba", "mamifero", "giba", "artiodactilo", "pezuñas", "peninsula arabiga", "camelus", "dromedarius", "camelus dromedarius"]
focas = ["https://giphy.com/gifs/seal-adM1FEGALvsLS", "https://giphy.com/gifs/seals-lookatthelights-bRdTqVJ9of7Ko", "https://giphy.com/gifs/baby-seals-1VI11KXvGKZ8c", "https://giphy.com/gifs/bustle-seal-3oEduYLamPNtprNZ9m", "https://giphy.com/gifs/yawn-seal-babyseal-WE2AngvoLwc4zQRzVk", "https://giphy.com/gifs/OceanaOrg-WoQwRtTIR0kqFQVTWJ", "https://giphy.com/gifs/pbsnature-seal-seals-fur-gHJUEf5m1eiCjEEEai", "https://giphy.com/gifs/pbsnature-animals-nature-seal-2UIrMgtTszskzIdiYL", "https://giphy.com/gifs/channel9-david-attenborough-davidattenborough-sevenworldsoneplanet-Tf8uMxnsOBNSiHOmiI", "https://tenor.com/view/seal-smile-gif-21574380", "https://tenor.com/view/seal-white-seal-cute-adorable-seal-adorable-gif-17879744", "https://tenor.com/view/seal-seals-seal-kiss-kiss-gif-25888634", "https://tenor.com/view/seal-spin-spinning-spinning-seal-animal-spin-gif-17879679", "https://tenor.com/view/fat-full-food-seal-sassy-gif-7890730", "https://tenor.com/view/seal-silly-seal-ponsuke-seal-tongue-gif-25839635"]
frasesCelebres = ["No es un musical es... Una mierda", "El jamón al vacío no se puede mover", "Las canciones hablan", "-¿Quién coño es Diego? \n -Mi polla con peluca","Sabe como a habitación vieja", "-¿Qué color es ese? \n -Color normal", "Eres mazoca", "Quién es este gilipollas, no puedo más", "Tío no puedo con la cara de GILIPOLLAS que tiene", "Racismo o parkour, tú decides", "Voy a coger una bomba, y la próxima vez que vomite alguien, la reviento", "-NEREA RÁPIDO SUBE AL GEISER \n -QUÉ COJONES ES UN GEISER? \n \*Nerea ha muerto*", "Bena, matate", "-Ostia no hemos apagado las luces, somos poco discretos \n -Es de dia", "-Vamos a girar un pelín \n -¿Cuánto? \n -Unos 180 grados", "Dios es un poco basura", "Hace frío, voy a ponerme el porro folar", "Un nabo! Para mi casa", "Imaginaos que quiero consultar en una base de datos todos los usuarios cuyo sexo sea... Zurdo", "La ETA era la impedancia característica en el vacío", "No, la .3 por el culo te la hinco", "Todos los calvos tienen dientes", "Bena, yo saltaría por la ventana", "es leucemico porque es alérgico al gluten", "Me enfrenté a un payaso una vez y estuvo gracioso", "Se me oye gemir en todo el edificio", "Nerea dió su vida por el beti", "Primero muevo, luego pienso", "No sé sacar líquidos de aquí, ¿cómo va esto?", "¿Quién está tocándome la polla con un cristal?", "Tengo problemas manejando mis extremidades", "Me acaban de echar por decir Franco o ha empezado la partida?", "No me quiero poner político pero... \n Me voy a comer a Bulgaria", "Vamos a mear", "Odio la fauna local", "No es fea es exótica", "Me voy a la espación estacial", "Estoy un poco república democrática del congo", "-Te ofrecemos una oportunidad de negocio amigo, tus créditos o tu vida \n -Tu puta madre, que te parece eso", "Me van a dar el Indio este de mierda y cocaína", "Odio la puta gente", "Será que vale mucho para el vendedor comprado", "¿Me puede salir una puta?", "Es como al becario, no le pagas", "Las peores personas que he conocido en mi vida se llaman", "Entre todos somos dos", "¡¿Pero por qué sigo manchado?! Me tengo que morir", "No te puedo hacer un chequeo médico, soy hemofílico", "Mientras no metas las cosas en cadáveres, todo bien", "¿Puedo hacer una puta?", "Suelta el puto", "Ya vale de putos", "Yo necesito comida que pueda comer", "Necesito hambre", "Estoy hasta la polla \*Disparo*", "Voy tren 👍", "Ostia que estoy en la misma celda que Pedro Sánchez", "Necesitamos un buen plan. Para empezar, voy a pegar a un polígrafo", "Polvo de taco", "Quien de aqui no es analfabeto? \n \*silencio sepulcral*", "Ojalá yo cagar todo el día", "Estoy estresado porque tengo ganas de cagar", "EH, QUE TE PUEDES COMER LA MIERDA", "Ahora que soy fumador no se si estoy estresado por que quiero cagar o por que quiero fumar", "Espera, creo que lo que necesito es fumar, no cagar", "Lleva 5 segundos vivo y ya es retrasado", "Me voy a suicidar solo para no ser asmático", "Checkea esto \n \*Se pone a cagar*", "Te han vuelto a salir huevos", "¿Qué pasa si le disparo en la bola?","Aitor, bájale el tamaño a la interfaz que la tienes enorme", "Aitor al revés es autor", "Desde aquí parece que tengo polla", "Vale, hay dos personas con nabo, escóndanse!", "A mi me gusta mucho el tema de juntar mierda y que se haga grande", "Tengo que regar a Bena", "Una cosa muy rara que me pasa a veces, es que salgo a la calle", "Ah, es verdad, que me corro cuando me curo", "Está bien pero muerto", "El lunes me parece buena hora", "Poca broma, la polla es una buena forma de orientarse"]
candidatos = []

esperandoEste = False
tts = False
ruleta = False
roma = False

@bot.event
async def on_ready():
    numero=random.randint(0, len(frasesCelebres)-1)
    channel = bot.get_channel(483257593536446506)
    await channel.send(frasesCelebres[numero])
    print (frasesCelebres[numero])

async def background_task():
	while True:
		bop = await aioconsole.ainput()
		channel = bot.get_channel(483257593536446506)
		await channel.send(bop)

async def aprendizajeFrases():
    while True:
        await asyncio.sleep(1250)
        os.system("python Ordenar.py")
        rand = random.randint(1984, 19841984)
        await asyncio.sleep(rand)
        num=random.randint(0, len(frasesCelebres)-1)
        channel = bot.get_channel(483257593536446506)
        await channel.send(frasesCelebres[num])
        print (frasesCelebres[num])

async def kick(ctx, member: discord.Member, *, reason="Te ha tocado, parguela"):
    await member.kick(reason=reason)
    await ctx.send(f'A {member} le ha tocado')

@bot.event
async def on_message(message):

    if message.author.bot:
        return

    num = random.randint(1,1985)
    msg = message.content
    user = message.author.display_name
    usuario = message.author.name
    print(user+":",msg)
    r1 = random.randint(0, len(emojis)-1)
    idUsuario=message.author.id
    global esperandoEste
    global tts
    global ruleta
    global roma

    msg=msg.lower()
    
    if (num == 1984):
        mensaje = "Callate, "+user
        await message.channel.send(mensaje)
        await message.channel.send("Estoy cansado de esto.")
        sys.exit("Ya estoy hasta las pelotas")

    if (num >= 1980):
        await asyncio.sleep(random.randint(1,15))
        mensaje = "Vete a la mierda, "+user
        await message.channel.send(mensaje)

    if (any(word in msg for word in dromedario)):
        roma = True

    if ("yo flipo" in msg):
        numero = random.randint(1, 10) 
        for i in range(numero):
            await message.channel.send('Yo flipo')

    if msg == "tts" and tts == False:
        tts = True
        await message.channel.send('TTS activado')
    elif msg == "tts" and tts == True:
        tts = False
        await message.channel.send('TTS desactivado')
        return

    if (any(word in msg for word in padreada)):
        await message.channel.send("Y no poco")
        await message.channel.send(file=discord.File('Imagenes/mejodieron.png'))
        return

    if (any(word in msg for word in respuestas) and esperandoEste == True):
        esperandoEste = False
        time.sleep(1.5)
        await message.channel.send('https://tenor.com/view/walter-white-walter-crying-walter-dying-gif-20964719')
        #await message.channel.send(file=discord.File('walter-white-falling.gif'))
        return

    if ("fiesta" in msg):
        mensaje=user+", cuál fiesta?"
        await message.channel.send(mensaje, tts=tts)
        esperandoEste = True
        return

    if any(word in msg for word in sustancias):
        for i in range(len(sustancias)-1):
            if sustancias[i] in msg:
                sustancia = sustancias[i]
        mensaje=user+", qué es "+sustancia+"?"
        await message.channel.send(mensaje, tts=tts)
        esperandoEste = True
        return

    if any(word in msg for word in pregunta):
        await message.add_reaction(':peepoclown:904688078453620767')
        await message.channel.send("Yo le pregunté", tts=tts)
        return

    if any(word in msg for word in array_ratios):
        await message.add_reaction(emojis[r1])
        

    if any(word in msg for word in tigrerasta):
        await message.add_reaction(':tigrerasta:941000059795939339')
        

    if any(word in msg for word in gallotrap):
        await message.add_reaction('🤙')
        

    if any(word in msg for word in bena):
        await message.add_reaction('a:bena:948200095415955506')
        

    if ("abogado" in msg):
        frase = "¿Crees que soy boludo, "+user+"?"
        await message.channel.send(frase, tts=tts)
        await asyncio.sleep(random.randint(1,5))
        await message.channel.send('Quieres que diga "¿Qué abogado?" Y tú dirás "El que tengo aquí colgado"', tts=tts)
        await asyncio.sleep(random.randint(1,5))
        await message.channel.send( "Vete a la mierda", tts=tts)
        time.sleep(random.randint(1,5))
        await message.add_reaction(':xD:861261199396175892')
        await message.channel.send( "https://tenor.com/view/3d-saul-saul-goodman-adamghik-gif-23876766")
        return

    if ("señor" in msg and "white" in msg):
        mensaje="Que quieres, "+user+"?"
        await message.channel.send(mensaje, tts=tts)
        return

    if ("gora eta" in msg):
        mensaje="Gora eta militarra. Viva o exercito guerrilheiro do povo galego ceive. Viva Marx viva Engels viva Lenin viva Stalin viva Mao. Parasitos youtubers gulag."
        await message.channel.send(mensaje, tts=tts)
        return

    if ("foca" in msg):
        numero = random.randint(0, len(focas)-1)
        await message.channel.send(focas[numero])

    if idUsuario == 325587406105477120 and roma == True:
        await message.channel.send('Vete a la mierda, Roma')

    with open('Datos/Frases.txt', 'r') as f:
        lineas = f.readlines()

    #Para que recoja los mensajes completos
    with open('Datos/Frases.txt', 'a') as f:
        if(msg not in lineas):
            f.write('\n')
            f.write(msg)

    #if (msg == "!ruleta"):
        #await message.channel.send('Tienen 60 segundos para apuntarse diciendo "yo", empezando ya')
        #ruleta = True
        #await asyncio.sleep(60)
        #expulsion = random.randint(0, len(candidatos)-1)
        #await message.guild.kick(candidatos[expulsion],*)

    if ((msg == "yo") and (ruleta)):
        global candidatos
        candidatos.append(idUsuario)
        await message.channel.send("Prepárate " + user)

    if(msg == "!ruleta"):
        await message.channel.send("Tienen 60 segundos para apuntarse diciendo yo, empezando ya")
        candidatos = []
        ruleta = True
        await asyncio.sleep(60)        
        expulsion = random.randint(0, len(candidatos)-1)
        expulsao = message.guild.get_member(candidatos[expulsion])
        await message.channel.send("Que te jodan, " + expulsao.display_name)
        await message.guild.kick(message.guild.get_member(candidatos[expulsion]), reason=None)
        ruleta = False

    if(msg == "!genocida"):
        await message.channel.send("Espero no echar a Dixeo")
        todos = list(message.guild.members)
        await asyncio.sleep(5)        
        expulsion = random.randint(0, len(todos)-1)
        expulsao = message.guild.get_member(todos[expulsion].id)
        print(expulsao)
        await message.channel.send("Que te jodan, " + expulsao.display_name)
        await message.guild.kick(message.guild.get_member(expulsao.id), reason=None)

#-------------------------------------------------------------------------------------------#

bot.loop.create_task(background_task())
bot.loop.create_task(aprendizajeFrases())
bot.run(os.environ['DISCORD_TOKEN_WALTER'])
