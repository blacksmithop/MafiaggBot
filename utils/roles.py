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
        response = None
        if name in roles:
            response = roles[name]
        for role in roles:
            if similar(role.name, name) > 0.8:
                response = role
        description = self.formatRoleData(name=name, response=response)
        return description
    
    def formatRoleData(self, name: str, response: Optional[Role]):
        if response == None:
            text = f"❌ Could not find a role by the name: {name}" 
        text = f"✅ Role: {response.name} | Alignment: {response.alignment.title()} | Description: {response.description}"
        return text
    
    
if __name__ == "__main__":
    role = GetRole()
    print(role.getRole("fall"))
    print(role.getRole("tailor"))
    print(role.getRole("xudsds"))
