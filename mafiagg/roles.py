from mafiagg.helper.decorators import get_similar_score
from json import load
from mafiagg.models.models import Role
from typing import Optional
from collections import OrderedDict
from os import path
from pathlib import Path
from requests import Session
from json import dump


class GetRole:
    def __init__(self) -> None:
        self.get_roles()

    URL = "https://raw.githubusercontent.com/blacksmithop/MafiaggBot/main/data/roles/roles.json"
    ROLES_DIR = "./data/roles"

    def get_roles(self):
        file_path = f"{self.ROLES_DIR}/roles.json"
        if path.isfile(file_path):
            print("Loaded roles")
            with open(file_path, "r", encoding="utf8") as f:
                roles = load(f)["roles"]
                self.roles = [Role(**item) for item in roles]

        else:
            self.download_roles()

    def download_roles(self):
        self.create_roles_dir()
        self.store_roles()

    def store_roles(self):
        with Session() as sess:
            data = sess.get(self.URL).json()
        roles = [Role(**item) for item in data["roles"]]
        sorted_roles = sorted(roles, key=lambda x: x.name)
        roles = [dict(role) for role in sorted_roles]
        data["roles"] = roles

        with open(f"{self.ROLES_DIR}/roles.json", "w") as f:
            dump(data, f, indent=4, sort_keys=True, default=str)
            print("Saved role data to file")

    def create_roles_dir(self) -> None:
        Path(self.ROLES_DIR).mkdir(parents=True, exist_ok=True)

    def get_role(self, name: str):
        matches = {}
        name = name.title()
        response = None
        for role in self.roles:
            score = get_similar_score(role.name, name)
            if score > 0.7:
                matches[score] = role
        if matches != {}:
            matches = OrderedDict(sorted(matches.items()))
            response = next(reversed(matches.items()))[1]
        description = self.format_role(name=name, response=response)
        return description, response

    def format_role(self, name: str, response: Optional[Role]):
        if response == None:
            text = f"❌ Could not find a role by the name: {name}"
        else:
            text = f"✅ Role: {response.name} | Alignment: {response.alignment} | Description: {response.description} | Tags: {', '.join(response.tags)}"
        return text


if __name__ == "__main__":
    role = GetRole()
    print(role.get_role("fall"))
    print(role.get_role("tailor"))
    print(role.get_role("xudsds"))
