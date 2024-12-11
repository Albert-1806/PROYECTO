import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def cmds(ctx):
    embed = discord.Embed(
        title="Comand list",
        color=0x001A5F
    )
    embed.add_field(name="[cmds]", value="Envía todos los comandos disponibles.", inline=True)
    embed.add_field(name="[save]", value="Guarda las imagenes enviadas.", inline=True)
    embed.add_field(name="[saludo]", value="Responde con un saludo", inline=True)
    embed.add_field(name="[bye]", value="Responde con un adiós.", inline=True)
    embed.add_field(name="[informacion]", value="Da un ejemplo de panel solar.", inline=True)
    embed.add_field(name="[ejemplo]", value="Nos brindara 1 ejemplo de panel solar.")
    embed.add_field(name="[rankig]", value="Da un top 5 de los mejores paneles.", inline=True)
    embed.add_field(name="[monocristalinos]", value="Envía informacion sobre el panel.", inline=True)
    embed.add_field(name="[polocristalinos]", value="Envía informacion sobre el panel.", inline=True)
    embed.add_field(name="[capa_fina]", value="Envía informacion sobre el panel.", inline=True)
    embed.add_field(name="[bifaciales]", value="Envía informacion sobre el panel.", inline=True)
    embed.add_field(name="[hibridos]", value="Envía informacion sobre el panel.", inline=True)

    await ctx.send(embed=embed)


@bot.command()
async def save(ctx):
    embed = discord.Embed(
        color=0x3E77B6
    )
    
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            await attachment.save(f"./img/{file_name}")
            embed.add_field(name="Imagen Guardada", value=f"Guarda la imagen en ./img/{file_name}", inline=False)

    else:
        embed.description = "No se ha podido cargar la imagen :("
    
    await ctx.send(embed=embed)

@bot.command()
async def saludo(ctx):
    embed = discord.Embed(
        description=f'¡Hola! Yo soy un bot de paneles solares y te estare brindando información.',
        color=0xC5D4EB
    )
    await ctx.send(embed=embed)

@bot.command()
async def bye(ctx):
    embed = discord.Embed(
        description=f'Estare listo para cuando vuelvas, ¡Hasta luego!.',
        color=0x6C85BD
    )
    await ctx.send(embed=embed)

@bot.command()
async def informacion(ctx):
    embed = discord.Embed(
        title="Información sobre Paneles Solares",
        description=f"Aquí tienes información sobre los paneles solares.",
        color=0x00527C
    )
    embed.add_field(name="¿Que son?", value="Son dispositivos que convierten la luz solar en electricidad mediante celdas fotovoltaicas. Estos son una fuente de energía limpia y renovable, ideales para reducir la dependencia de combustibles fósiles.", inline=False)
    
    await ctx.send(embed=embed)

@bot.command()
async def ejemplo(ctx):
    ps = ["Monocristalinos", "Policristalinos", "Híbridos", "De capa fina", "Bifaciales",
          "Concentradores solares", "Orgánicos", "De silicio amorfo", "De diseleniuro de cobre, indio y galio", "De teluro de cadmio"]  
    cps = random.choices(ps)
    
    embed = discord.Embed(
        title="Panel aleatorio : ",
        description=f"Te ha tocado : {cps}",
        color=0x003777
    )

    await ctx.send(embed=embed)

@bot.command()
async def ranking(ctx, count=5):
    embed = discord.Embed(
        title="LOS MEJORES PANELES SOLARES",
        description=f"Tenemos los {count} mejores :",
        color=0x82A1B1
    )
    embed.add_field(name="Número 1", value="Como el mejor panel a nivel internacional tenemos a los Monocristalinos", inline=False)
    embed.add_field(name="Número 2", value="En el top 2 tenemos a los Policristalinos", inline=False)
    embed.add_field(name="Número 3", value="Dentro de los 3 mejores esta el de Película Fina", inline=False)
    embed.add_field(name="Número 4", value="Aquí tenemos a los Bifaciales", inline=False)
    embed.add_field(name="Número 5", value="Por último tenemos a los Híbridos", inline=False)

    await ctx.send(embed=embed)
    
@bot.command()
async def monocristalinos(ctx):
    embed = discord.Embed(
        title="Información sobre Paneles Solares",
        description="Aquí tienes información sobre el panel solar.",
        color=0xb5bac9
    )
    embed.add_field(name="Monocristalinos", value="Eficientes y duraderos, fabricados con un solo cristal de silicio. Ideales para espacios reducidos.", inline=False)
    
    await ctx.send(embed=embed)

@bot.command()
async def policristalinos(ctx):
    embed = discord.Embed(
        title="Información sobre Paneles Solares",
        description="Aquí tienes información sobre el panel solar.",
        color=0xa3a8b7
    )
    embed.add_field(name="Policristalinos", value="Más económicos, con menor eficiencia que los monocristalinos, pero funcionales para grandes áreas.", inline=False)
    
    await ctx.send(embed=embed)

@bot.command()
async def capa_fina(ctx):
    embed = discord.Embed(
        title="Información sobre Paneles Solares",
        description="Aquí tienes información sobre el panel solar..",
        color=0x8990a2
    )
    embed.add_field(name="De capa fina", value="Flexibles y ligeros, elaborados con materiales como teluro de cadmio o silicio amorfo; menos eficientes, pero adaptables.", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def bifaciales(ctx):
    embed = discord.Embed(
        title="Información sobre Paneles Solares",
        description="Aquí tienes información sobre el panel solar.",
        color=0x788199
    )
    embed.add_field(name="Bifaciales", value="Capturan energía por ambas caras, maximizando la generación eléctrica en ubicaciones con buena reflectividad.", inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def hibridos(ctx):
    embed = discord.Embed(
        title="Información sobre Paneles Solares",
        description="Aquí tienes información sobre el panel solar.",
        color=0x666F88
    )
    embed.add_field(name="Híbridos", value="Combinan tecnologías fotovoltaicas y térmicas, produciendo electricidad y calor simultáneamente.", inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def conclusion(ctx):
    embed = discord.Embed(
        color=0x002F5C
    )
    embed.add_field(name="En conclusión", value="Los paneles solares son una opción eficiente y sostenible para generar energía limpia, reducir costos y disminuir el impacto ambiental.Aquí te dejo algunas razones: Son energía renovable, tenemos ahorro económico, tienen bajo impacto ambiental y larga duración, entre miles más.", inline=False)

    await ctx.send(embed=embed)

bot.run("TOKEN")
