from mafiagg.credential_manager import CredentialManager
import asyncio

auth = CredentialManager()

async def login_periodically():
    while True:
        try:
            auth.login()
        except Exception as e:
            pass

        await asyncio.sleep(600)

def start_periodic_login():
    loop = asyncio.get_running_loop()
    loop.create_task(login_periodically())

start_periodic_login()

