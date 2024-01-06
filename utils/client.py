from websockets import connect
from requests import Session
from json import loads, dumps
from utils.mafiabot import Bot
from utils.credential_manager import CredentialManager
import asyncio


class Client:
    def __init__(self, auth: CredentialManager):
        self.auth = CredentialManager
        self.bot = Bot(auth=auth)
        self.ws = None
        self.room = None
        self.engine, self.auth = None, None

    def establishConnection(self):
        options = {"name": "Bot Lobby", "unlisted": True}  # Create a private lobby
        with Session() as s:
            resp = s.post(
                "https://mafia.gg/api/rooms/",
                cookies=self.bot.cookie,
                json=options,
            ).json()
        self.room = resp["id"]
        print(f"Created room at https://mafia.gg/game/{self.room}")
        self.getWebsocket()

    def getWebsocket(self):
        with Session() as s:
            resp = s.get(
                f"https://mafia.gg/api/rooms/{self.room}", cookies=self.bot.cookie
            ).json()
            self.engine, self.auth = resp["engineUrl"], resp["auth"]

    async def sendToWebsocket(self, engine, auth):
        print("Establishing connection")
        self.ws = await connect(engine, ssl=True)
        output = dumps(
            {
                "type": "clientHandshake",
                "userId": self.bot.id,
                "roomId": self.room,
                "auth": auth,
            }
        )
        await self.ws.send(output)
        await self.ws.send(dumps({"type": "presence", "isPlayer": False}))

    def run(self):
        self.establishConnection()
        asyncio.get_event_loop().run_until_complete(
            self.sendToWebsocket(self.engine, self.auth)
        )
        print("Bot has started listening to commands")
        asyncio.get_event_loop().run_until_complete(self.sendAndReceive())

    async def sendAndReceive(self):
        while True:
            info = loads(await self.ws.recv())
            resp = self.bot.parse(info)
            if resp is not None:
                if type(resp) is list:
                    for i in resp:
                        await self.ws.send(dumps(i))
                elif resp["type"] == "newGame":
                    self.establishConnection()
                    self.getWebsocket()
                    chat = {
                        "type": "chat",
                        "message": f"I moved to https://mafia.gg/game/{self.room}",
                    }
                    await self.ws.send(dumps(chat))
                    await self.ws.send(dumps({"type": "newGame", "roomId": self.room}))
                    await self.sendToWebsocket(self.engine, self.auth)
                    print("New game, clearing the cache(user)")
                    self.bot.reset_cache()
                else:
                    await self.ws.send(dumps(resp))
