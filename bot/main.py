# TODO - transfer, casino, etc commands
from itertools import cycle
import discord
from discord.ext import commands, tasks
# Standard modules
# TOKEN, MONGO URI are env-vars
from utils import get_environment_variable
DISCORD_BOT_TOKEN = get_environment_variable("DISCORD_BOT_TOKEN")
# intents (new discord feature to limit bots to certain bucket events)
intents = discord.Intents.default()

# NOTE- The initial version of the bot used TinyDB, but I've migrated to
# MongoDB (still considering sql tho)
# client pointer for API-reference
client = commands.Bot(command_prefix='qq ',
                      case_insensitive=True, intents=intents)
# discord.py has an inbuilt help command, which doesn't look good''
client.remove_command('help')
# status-change-cycle(The bot changes presence after a few mins.)
STATUS = cycle([
    "qq help | :(",
    "with your heart",
    "in tears",
    "with tears",
    "with your soul",
    "I'm so sad",
    "with your tears...",
    "with your feelings",
    "with sparkles"])
ls_cog = ['cogs.fun_cog',
          'cogs.ping_cog',
          'cogs.help_cog',
          'cogs.coffee_cog',
          'cogs.meme_cog',
          'cogs.utils_cog',
          'cogs.name_cog',
          'cogs.game_cog',
          'cogs.economy_cog',
          'cogs.events_cog',
          'cogs.error_cog',
          'cogs.users_cog',
          'cogs.comic_cog',
          'jishaku']


@client.event
async def on_ready():
    '''
    This prints a message when the on_ready event is detected.
    That is, when the bot logs onto discord when the script is ran.
    '''
    change_status.start()  # Triggers status change task
    print("Processing.....")
    print("|||||||||||||||")
    print("Bot has Successfully logged onto Discord...")
    print('Successfully logged in as {0.user}...'.format(client))
    # client.user gives the bots discord username tag


@tasks.loop(seconds=600)
async def change_status():
    '''
    loops through the cycle of the STATUS list and sets that as bot presence
    '''
    await client.change_presence(activity=discord.Game(next(STATUS)))
    # NOTE- There are other methods, that can be utilised instead of just
    # 'playing'

# cog-loader
if __name__ == "__main__":
    for extension in ls_cog:
        client.load_extension(extension)
        print(f'Loaded cog : {extension}')

    # Running the BOT:
    if DISCORD_BOT_TOKEN != 'foo':
        client.run(str(DISCORD_BOT_TOKEN))
    else:
        print('No token Loaded')
