# MafiaggBot

![PyPI - Version](https://img.shields.io/pypi/v/mafiagg)
![Website](https://img.shields.io/website?url=https%3A%2F%2Fblacksmithop.github.io%2FMafiaggBot%2F&up_message=%E2%9C%85&up_color=%E2%9D%8C&logo=github&label=Docs&link=https%3A%2F%2Fblacksmithop.github.io%2FMafiaggBot%2F)


## Usage

---

```shell
pip install -U mafiagg
```


```shell
pip install -U python-dotenv
```

`python-dotenv` lets you pass a `.env` file with your mafia.gg credentials

```
MAFIA_USERNAME=username
MAFIA_PASSWORD=password
```

### Example

```python
from mafiagg.client import Bot
from mafiagg.credential_manager import CredentialManager
from sys import exit


auth = CredentialManager()

bot = Bot(auth=auth, command_prefix="$")

try:
    bot.run()
except KeyboardInterrupt:
    exit(0)
```

> When you run the bot for the first time, it will download some metadata it a `./data/` folder.

---

### Features

- [x] Rooms
  - [x] List rooms
  - [x] Make private/public
  - [x] Become player/spectator
  - [x] Do afk check
    - [x] Do afk check
    - [x] Do ready check
  - [ ] Edit room options
  - [x] Rename room
  - [x] Create new room
    - [x] Only create room when game end
- [x] Decks
  - [x] Get deck by name
  - [x] Set deck by name
  - [x] Use random deck
- [x] Setups
  - [x] Get setup by name
  - [x] Set setup by code
  - [x] Set setup by name
  - [ ] Get current setup code
- [x] Roles
  - [x] Get role by name
  - [x] Cleanup role descriptions, alignment with validator
- [x] Commands
  - [x] Custom command names
  - [x] Command docs
- [x] Bot Client
- [x] Authentication
- [x] Help command
  - [ ] Formatted / multi-message help command
- [x] Host only commands
    - [ ] Host can add admins

### Tasklist

- [ ] Do not allow creation of new room unless game is over
- [ ] Lookup in game Items
- [x] Edit room options
- [ ] Implement conversion of role dictionary to setup codes
- [ ] Return character info (for decks in next message)
- [ ] Better commands (sub-commands!)
- [ ] Better doc strings using decorators
- [ ] Join other rooms on request
  - [ ] Check if bot can handle concurrent games, keep session!
  - [ ] Keep role cache based on room id
- [ ] Allow for `super().__init__` calls
- [x] Gracefully end session
    - [ ] End event loops, close websocket connection
    - [x] When exiting call DELETE on `user-session` (cookie invalidation)


## Development

Clone the repo

```shell
git clone https://github.com/blacksmithop/MafiaggBot

cd MafiaggBot
```

---

Install the dependencies

```shell
python3 -m pip install -r requirements.txt
```
