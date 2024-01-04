from inspect import getmembers, ismethod
from utils.helper import isBotCommand, commandNotFound, register_command


class BotBase:
        
    def registerBotCommands(self):
        allCommands = getmembers(self, predicate=ismethod)
        commands = [command for command in allCommands if isBotCommand(command)]
        commandMapping = {
            v._commandName:v for _,v in commands
        }
        self.commands = commandMapping
        
    def getCommand(self, commandName: str):
        command = self.commands.get(commandName, None)
        return command

    def parseCommand(self, msg: str) -> list:
        ctx = msg.split(" ")
        if len(ctx) == 2:
            cmd, args = ctx
            cmd = self.getCommand(cmd)
            if cmd == None:
                cmd = self.getCommand(msg)
                args = None

        elif len(ctx) >= 3:
            cmd, args = ctx[0], ctx[1:]
            args = " ".join(args)
            cmd = self.getCommand(cmd)
            if cmd == None:
                cmd, args = ctx[:2], ctx[2:]
                cmd = " ".join(cmd)
                args = " ".join(args)
                cmd = self.getCommand(cmd)
                if cmd == None:
                    cmd, args = None, None
        else:
            cmd, args = msg, None
            cmd = self.getCommand(cmd)
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
        func = self.getCommand(commandName=args)
        if not func:
            self.response["message"] = f"⛔ No command named [{args}]"
        else:
            self.response["message"] = f"✅ Command [{func._commandName}] : {func.__doc__}"
        return self.response
    
    def reset_cache(self):
        self.cache.data = dict()