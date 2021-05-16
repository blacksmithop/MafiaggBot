# Deck

### Get a list of all decks
Make a GET request to `https://mafia.gg/api/decks?filter&page=num`
`num` indicates the page to display

Response
```python
{pagination: {page: int, numPages: int, total: int},
     decks: [{name: str, version: int,
     key: DECKID, builtin: bool,
     deckSize: int, uploadTimestamp: int(timestamp),
     sampleCharacters: [{playerId: int, name: str,
     avatarUrl: str, backgroundColor: str(hex)}, ...]}]}
```
Check `numPages` for total number of pages

### Get deck by ID
Make a GET request to `https://mafia.gg/api/decks/deckId`

Response
```python
{
     name: str, version: int,
     key: DECKID, builtin: bool,
     deckSize: int, uploadTimestamp: int(timestamp),
     sampleCharacters:
         [{playerId: int, name: str,
        avatarUrl: str, backgroundColor: str(hex)}, ...]
}
```