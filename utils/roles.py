from utils.helper import similar
from json import load
from utils.models.models import Role
from typing import Optional
from collections import OrderedDict


with open("./data/roles/roles.json", "r") as f:
    data = load(f)
    roles = data["roles"]

rawRoles = [Role(**item) for item in roles]
roles = sorted(rawRoles, key=lambda x: x.name)


class GetRole:
    def getRole(self, name: str):
        matches = {}
        name = name.title()
        response = None
        for role in roles:
            score = similar(role.name, name)
            if score > 0.7:
                matches[score] = role
        if matches != {}:
            matches = OrderedDict(sorted(matches.items()))
            response = next(reversed(matches.items()))[1]
        description = self.formatRoleData(name=name, response=response)
        return description, response

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
