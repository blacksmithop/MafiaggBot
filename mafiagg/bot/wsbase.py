from websockets import connect
from requests import Session
from json import loads, dumps
import asyncio


class WebsocketBase:
    def establish_connection(self):
        options = {"name": "Bot Lobby", "unlisted": True}  # Create a private lobby
        with Session() as s:
            resp = s.post(
                "https://mafia.gg/api/rooms/",
                cookies=self.cookie,
                json=options,
            ).json()
        self.room = resp["id"]
        print(f"Created room at https://mafia.gg/game/{self.room}")
        self.get_websocket()

    def get_websocket(self):
        with Session() as s:
            resp = s.get(
                f"https://mafia.gg/api/rooms/{self.room}", cookies=self.cookie
            ).json()
            self.engine, self.auth = resp["engineUrl"], resp["auth"]

    async def send_to_websocket(self, engine, auth):
        print("Establishing connection")
        self.ws = await connect(engine, ssl=True)
        output = dumps(
            {
                "type": "clientHandshake",
                "userId": self.botUser.id,
                "roomId": self.room,
                "auth": auth,
            }
        )
        await self.ws.send(output)
        await self.ws.send(dumps({"type": "presence", "isPlayer": False}))

    def run(self):
        self.establish_connection()
        asyncio.get_event_loop().run_until_complete(
            self.send_to_websocket(self.engine, self.auth)
        )
        print("Bot has started listening to commands")
        asyncio.get_event_loop().run_until_complete(self.sendAndReceive())

    def __del__(self):
        print("Bot stopped, shutting down")

    async def sendAndReceive(self):
        while True:
            info = loads(await self.ws.recv())
            resp = self.parse(info)
            if resp is not None:
                if type(resp) is list:
                    for i in resp:
                        await self.ws.send(dumps(i))
                elif resp["type"] == "newGame":
                    self.establish_connection()
                    self.get_websocket()
                    chat = {
                        "type": "chat",
                        "message": f"I moved to https://mafia.gg/game/{self.room}",
                    }
                    await self.ws.send(dumps(chat))
                    await self.ws.send(dumps({"type": "newGame", "roomId": self.room}))
                    await self.send_to_websocket(self.engine, self.auth)
                    print("New game, clearing the cache(user)")
                    self.reset_cache()
                else:
                    await self.ws.send(dumps(resp))
