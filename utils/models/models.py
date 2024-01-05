from pydantic import BaseModel, field_validator
from typing import Optional, List


# Role
class Role(BaseModel):
    name: str = ""
    description: str = ""
    id: int = -1
    alignment: str = None
    new: bool = None
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
    def title_alignment(cls, v: str) -> str:
        return v.title()


# User
class User(BaseModel):
    id: int
    username: str
    activePatreon: bool
    createdAt: str
    hostBannedUsernames: List[str] = []
    isPatreonLinked: bool = False
    needsVerification: bool = False
    createdAt: str = ""


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