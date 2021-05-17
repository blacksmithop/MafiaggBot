## How to use
####Clone this repo
```shell
git clone https://github.com/blacksmithop/MafiaggBot

cd MafiaggBot
```

#### Install the dependencies
```shell
python3 -m pip install -r requirements.txt
```
#### Set environment variables
`USER` - username
`PASS` - password
#### .env support
Run 
```
python3 -m pip install python-dotenv
```
Create a .env file
```
USER=username
PASS=password
```
#### Run the bot
```shell
python3 runbot.py
```
Note: When you run the bot for the first time,
it will download the deck and setup data
and store it in `bot/data/` folder.

[API docs](https://blacksmithop.github.io/mafiaggbot/)