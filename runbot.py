from utils.client import Client
from sys import exit

bot = Client()

try:
    bot.run()
except KeyboardInterrupt:
    exit(0)
