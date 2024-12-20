from pydantic import BaseModel, field_validator
from typing import Optional, List

# case "third":
#             return "Third-party";
#         case "mafia":
#             return "Mafia-aligned";
#         case "town":
#             return "Town-aligned";
#         case "none":
#             return "None";
#         default:

alignmentMapping = {
    "third": "Third-party",
    "mafia": "Mafia-aligned",
    "town": "Town-aligned",
    "none": "None",
}


# Role
class Role(BaseModel):
    name: str = ""
    description: str = ""
    id: int = -1
    alignment: str = None
    new: Optional[bool] = None
    disabled: bool = False
    holiday: str = "none"
    tags: List[str] = []

    @field_validator("description")
    @classmethod
    def cleanup_description(cls, v: str) -> str:
        v = v.replace("@{item:", "[").replace("}", "]")
        return v

    @field_validator("alignment")
    @classmethod
    def title_alignment(cls, alignment: str) -> str:
        alignment = alignmentMapping.get(alignment, None)
        return alignment


# Search User
class SearchUser(BaseModel):
    id: int
    username: str
    createdAt: str


# User
class User(BaseModel):
    id: int
    username: str
    createdAt: str


# Rooms
class Room(BaseModel):
    id: str
    name: str
    hasStarted: bool
    playerCount: int
    setupSize: int
    hostUser: User
    createdAt: str


# Pagination
class Pagination(BaseModel):
    page: int
    numPages: int
    total: int


# Deck Character
class Character(BaseModel):
    playerId: int
    name: str
    avatarUrl: str
    backgroundColor: str


# Deck
class Deck(BaseModel):
    name: str
    version: int
    key: str
    builtin: bool
    deckSize: int
    uploadTimestamp: int
    sampleCharacters: List[Character]


# Deck with pagination
class DeckData(BaseModel):
    pagination: Optional[Pagination]
    decks: List[Deck]


# Setup
class Setup(BaseModel):
    name: str
    code: Optional[str]
