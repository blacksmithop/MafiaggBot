from utils.client import Client
from utils.credential_manager import CredentialManager
from sys import exit


auth = CredentialManager()

bot = Client(auth=auth)

# try:
#     bot.run()
# except KeyboardInterrupt:
#     exit(0)
