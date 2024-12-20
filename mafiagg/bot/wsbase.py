from websockets import connect
from websockets.exceptions import ConnectionClosedOK
from requests import Session
from json import loads, dumps
import asyncio


class WebsocketBase:
    def establish_connection(self):
        options = {"name": "Bot Lobby", "unlisted": True}  # Create a private lobby
        try:
            with Session() as s:
                resp = s.post(
                    "https://mafia.gg/api/rooms/",
                    cookies=self.cookie,
                    json=options,
                ).json()
            self.room = resp["id"]
            print(f"Created room at https://mafia.gg/game/{self.room}")
            self.get_websocket()
        except Exception as e:
            print(f"Error establishing connection: {e}")

    def get_websocket(self):
        try:
            with Session() as s:
                resp = s.get(
                    f"https://mafia.gg/api/rooms/{self.room}", cookies=self.cookie
                ).json()
                self.engine, self.auth = resp["engineUrl"], resp["auth"]
        except Exception as e:
            print(f"Error getting websocket information: {e}")

    async def send_to_websocket(self, engine, auth):
        try:
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
        except Exception as e:
            print(f"Error in sending to websocket: {e}")

    async def listen_and_respond(self):
        while True:
            try:
                info = loads(await self.ws.recv())
            except ConnectionClosedOK:
                print("Websocket connection closed")
                exit(0)
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

    def run(self):
        self.establish_connection()
        asyncio.get_event_loop().run_until_complete(
            self.send_to_websocket(self.engine, self.auth)
        )
        print("Bot has started listening to commands")
        asyncio.get_event_loop().run_until_complete(self.listen_and_respond())
