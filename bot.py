import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix='!')

# Словарь для хранения пар "код сервера: язык"
server_languages = {}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='set_language', aliases=['установить_язык'])
async def set_language(ctx, language):
    # Проверка наличия указанного языка
    if language.lower() in ['en', 'ru']:
        server_languages[ctx.guild.id] = language.lower()
        await ctx.send(f'Язык для сервера {ctx.guild.name} установлен на {language.upper()}')
    else:
        await ctx.send('Доступные языки: EN, RU')

@bot.command(name='hello', aliases=['привет'])
async def hello(ctx):
    # Получение языка для сервера
    language = server_languages.get(ctx.guild.id, 'en')

    # Локализация текста
    if language == 'ru':
        message = 'Привет, мир!'
    else:
        message = 'Hello, world!'

    await ctx.send(message)

# Запуск бота
bot.run('YOUR_BOT_TOKEN')
