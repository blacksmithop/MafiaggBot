# MafiaggBot

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
  - [x] Rename room
  - [x] Create new room
    - [ ] Only create room when game end
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
  - [ ] Cleanup role descriptions with validator
- [x] Commands
  - [x] Custom command names
  - [x] Command docs
- [x] Bot Client
- [x] Authentication
- [x] Help command
  - [ ] Formatted / multi-message help command
- [ ] Host only commands

### Tasklist

- [ ] Don't create new room unless game end
- [ ] Understand role object -> setup code creation
- [ ] Return character info (for decks in next message)
- [ ] Better commands (sub-commands!)
- [ ] Better doc strings using decorators
- [ ] When exiting bot site calls DELETE on `user-session` (cookie invalidation?)
- [ ] Join other rooms on request
- [ ] Allow for `super().__init__` calls

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
