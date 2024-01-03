from websockets import connect
from requests import Session
from json import loads, dumps
from utils.auth import Cookie
from utils.bot import Bot
import asyncio


class Mafia:
    def __init__(self):
        cookie = Cookie()
        self.cookie = cookie.getCookieData()
        cookie = cookie
        # self.user = User()
        self.id = cookie.user.id
        self.bot = Bot(user=self.cookie, _id=id) # self.user.response["id"]
        self.ws = None
        self.room = None
        self.engine, self.auth = None, None

    def load(self):
        options = {"name": "Bot Lobby", "unlisted": True}
        with Session() as s:
            resp = loads(
                s.post(
                    "https://mafia.gg/api/rooms/",
                    cookies=self.cookie,
                    json=options,
                ).content
            )
        self.room = resp["id"]
        room = f"Created room at https://mafia.gg/game/{self.room}"
        print(room)
        self.get_ws()

    def get_ws(self):
        with Session() as s:
            resp = loads(
                s.get(
                    f"https://mafia.gg/api/rooms/{self.room}", cookies=self.cookie
                ).content
            )
            self.engine, self.auth = resp["engineUrl"], resp["auth"]

    async def ws_send(self, engine, auth):
        print("Establishing connection")
        self.ws = await connect(engine, ssl=True)
        output = dumps(
            {
                "type": "clientHandshake",
                "userId": self.id,
                "roomId": self.room,
                "auth": auth,
            }
        )
        await self.ws.send(output)
        info = loads(await self.ws.recv())
        self.bot.roles = info["events"][2]["roles"]
        await self.ws.send(dumps({"type": "presence", "isPlayer": False}))

    def run(self):
        self.load()
        asyncio.get_event_loop().run_until_complete(
            self.ws_send(self.engine, self.auth)
        )
        print("Bot has started listening to commands")
        asyncio.get_event_loop().run_until_complete(self._run())

    def __del__(self):
        print("Bot stopped, shutting down")

    async def _run(self):
        while True:
            info = loads(await self.ws.recv())
            resp = self.bot.parse(info)
            if resp is not None:
                if type(resp) is list:
                    for i in resp:
                        await self.ws.send(dumps(i))
                elif resp["type"] == "newGame":
                    self.load()
                    self.get_ws()
                    chat = {
                        "type": "chat",
                        "message": f"I moved to https://mafia.gg/game/{self.room}",
                    }
                    await self.ws.send(dumps(chat))
                    await self.ws.send(dumps({"type": "newGame", "roomId": self.room}))
                    await self.ws_send(self.engine, self.auth)
                    print("New game, clearing the cache(user)")
                    self.bot.reset_cache()
                else:
                    await self.ws.send(dumps(resp))
