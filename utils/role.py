from matcher import similar
from json import load
from pydantic import BaseModel
from typing import List


class Role(BaseModel):
    name: str = ""
    description: str = ""
    id: int = -1
    alignment: str = None
    new: bool = None
    disabled: bool = False
    holiday: str = "none"
    tags: List[str] = []




with open("./data/roles/roles.json", "r") as f:
    data = load(f)
    roles = data["roles"]

roles = [Role(**item) for item in roles]


class GetRole:
    def getRole(self, name: str):
        if name in roles:
            return roles[name]
        for role in roles:
            if similar(role.name, name) > 0.8:
                return role
        return None


if __name__ == "__main__":
    role = GetRole()
    print(role.getRole("fall"))
    print(role.getRole("tailor"))
    print(role.getRole("xudsds"))
