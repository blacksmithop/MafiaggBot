from typing import List


# check if bot command
def is_bot_command(data):
    name, cmd = data
    return name[:2] != "__" and hasattr(cmd, "isCommand")


# convert setup code to roles dict
def convert_setup(roles: str) -> dict:
    try:
        return dict(map(lambda x: str.split(x, "a"), str.split(roles, "b")))
    except ValueError:
        pass


# calculate number of roles
def get_role_name_and_count(args: List):
    if len(args) == 2:
        try:
            role_name, role_count = args[0], int(args[1])
        except ValueError:
            role_name, role_count = args, 1
    else:
        try:
            role_name, role_count = args[:-1], int(args[-1])
        except ValueError:
            role_name, role_count = args, 1
    return role_name, role_count
