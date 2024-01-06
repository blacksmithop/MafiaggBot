from utils.client import Bot
from utils.credential_manager import CredentialManager
from sys import exit


auth = CredentialManager()

bot = Bot(auth=auth, command_prefix="$")

try:
    bot.run()
except KeyboardInterrupt:
    exit(0)
