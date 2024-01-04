# MafiaggBot

![Website](https://img.shields.io/website?label=Docs&style=for-the-badge&up_color=%E2%9D%8C&up_message=%E2%9C%85&url=https%3A%2F%2Fblacksmithop.github.io%2FMafiaggBot%2F)

## Instructions

---

### Clone repo

```shell
git clone https://github.com/blacksmithop/MafiaggBot

cd MafiaggBot
```

---

### Install dependencies

```shell
python3 -m pip install -r requirements.txt
```

---

### Set environment variables

Create a .env file with credentials

```
MAFIA_GG_USERNAME=username
MAFIA_GG_PASSWORD=password
```

---

## Usage

```shell
python3 runbot.py
```

Note: When you run the bot for the first time,
it will download the deck and setup data
and store it in `bot/data/` folder.

### Changelog

- [x] Reworked Decks
- [x] Reworked Roles
- [ ] Rework bot logic
- [x] Only read cookie once, refresh if needed
- [x] Cleanup descriptions with validator
- [ ] Lock certain commmands as host only
- [ ] Don't create new commands unless game end
- [ ] Return character info (for decks in next message)
- [ ] Better commands (sub-commands!)
- [ ] Better doc strings using decorators
- [x] Move functional commands to bot base
- [ ] Run `registerBotCommands` automatically