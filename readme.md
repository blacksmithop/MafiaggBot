# MafiaggBot
![Website](https://img.shields.io/website?label=Docs&style=for-the-badge&up_color=%E2%9D%8C&up_message=%E2%9C%85&url=https%3A%2F%2Fblacksmithop.github.io%2FMafiaggBot%2F)

- [Clone this repo](#clone-this-repo)
- [Install the dependencies](#install-the-dependencies)
- [Set environment variables](#set-environment-variables)
- [Use .env file](#use-env-file)
- [Run the bot](#run-the-bot)

<!-- toc -->


### Clone this repo
```shell
git clone https://github.com/blacksmithop/MafiaggBot

cd MafiaggBot
```

### Install the dependencies
```shell
python3 -m pip install -r requirements.txt
```
### Set environment variables
`USER` - username
`PASS` - password
### Use .env file
Run 
```
python3 -m pip install python-dotenv
```
Create a .env file
```
USER=username
PASS=password
```
### Run the bot
```shell
python3 runbot.py
```
Note: When you run the bot for the first time,
it will download the deck and setup data
and store it in `bot/data/` folder.
