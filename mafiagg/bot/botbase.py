from inspect import getmembers, ismethod
from mafiagg.helper.decorators import register_command
from mafiagg.helper.tools import is_bot_command
from mafiagg.bot.wsbase import WebsocketBase
from typing import Dict, List


class BotBase(WebsocketBase):
    def register_bot_commands(self):
        allCommands = getmembers(self, predicate=ismethod)
        commands = [command for command in allCommands if is_bot_command(command)]
        commandMapping = {v._commandName: v for _, v in commands}
        self.commands = commandMapping

    def get_command(self, commandName: str):
        return self.commands.get(commandName, None)

    def send(self, message: str) -> Dict:
        return {"type": "chat", "message": message}

    def parse_command(self, msg: str) -> List:
        ctx = msg.split(" ")
        if len(ctx) == 2:
            cmd, args = ctx
            cmd = self.get_command(cmd)
            if cmd == None:
                cmd = self.get_command(msg)
                args = None

        elif len(ctx) >= 3:
            cmd, args = ctx[0], ctx[1:]
            args = " ".join(args)
            cmd = self.get_command(cmd)
            if cmd == None:
                cmd, args = ctx[:2], ctx[2:]
                cmd = " ".join(cmd)
                args = " ".join(args)
                cmd = self.get_command(cmd)
                if cmd == None:
                    cmd, args = None, None
        else:
            cmd, args = msg, None
            cmd = self.get_command(cmd)
        return [cmd, args]

    @register_command("help")
    def help(self, args=None) -> dict:
        """Shows the help command"""
        if args is None:
            functions = self.commands.keys()
            func = [f"[{i}]" for i in functions]
            self.response[
                "message"
            ] = f"Commands are {', '.join(func)} GitHub: https://github.com/blacksmithop/mafiaggbot"
            return self.response
        func = self.get_command(commandName=args)
        if not func:
            self.response["message"] = f"⛔ No command named [{args}]"
        else:
            self.response[
                "message"
            ] = f"✅ Command <{func._commandName}> - {func.__doc__}".format(
                prefix=self.command_prefix, cmd=func._commandName
            )
        return self.response

    def reset_cache(self):
        self.cache.data = dict()
