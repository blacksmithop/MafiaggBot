from utils.helper import similar
from json import load
from utils.models.models import Role
from typing import Optional

with open("./data/roles/roles.json", "r") as f:
    data = load(f)
    roles = data["roles"]

roles = [Role(**item) for item in roles]


class GetRole:
    def getRole(self, name: str):
        name = name.title()
        response = None
        if name in roles:
            response = roles[name]
        for role in roles:
            score = similar(role.name, name)
            if score > 0.6:
                response = role
        description = self.formatRoleData(name=name, response=response)
        return description

    def formatRoleData(self, name: str, response: Optional[Role]):
        if response == None:
            text = f"❌ Could not find a role by the name: {name}"
        else:
            text = f"✅ Role: {response.name} | Alignment: {response.alignment} | Description: {response.description}"
        return text


if __name__ == "__main__":
    role = GetRole()
    print(role.getRole("fall"))
    print(role.getRole("tailor"))
    print(role.getRole("xudsds"))
