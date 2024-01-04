# MafiaggBot

## Usage

---

```shell
git clone https://github.com/blacksmithop/MafiaggBot

cd MafiaggBot
```
---

### Installation

Install dependencies 

```shell
python3 -m pip install -r requirements.txt
```

---


Create a .env file with credentials

```
MAFIA_GG_USERNAME=username
MAFIA_GG_PASSWORD=password
```

---

### Running the bot

```shell
python3 runbot.py
```

Note: When you run the bot for the first time,
it will download the deck and setup data
and store it in `bot/data/` folder.

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
- [x] Roles
    - [x] Get role by name
    - [ ] Cleanup role descriptions with validator
- [x] Commands
    - [x] Custom command names
    - [x] Command docs
- [x] Bot Client
- [X] Authentication
- [x] Help command
    - [ ] Formatted / multi-message help command
- [ ] Host only commands


### Tasklist

- [ ] Don't create new room unless game end
- [ ] Return character info (for decks in next message)
- [ ] Better commands (sub-commands!)
- [ ] Better doc strings using decorators