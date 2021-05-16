# Rooms

### Get all rooms

Making a GET request to `https://mafia.gg/api/rooms` 
returns a list of running rooms

Response
```python
[
{id: int,
 name: str,
 hasStarted: bool,
 playerCount: int,
 setupSize: int,
 hostUser: {id: int, username: str,
         activepatreon: bool,
         createdAt: str(timestamp)}
        , createdAt: str(timestamp)}, ....
]
```

### Get room by ID
Making a GET request to `https://mafia.gg/api/rooms/roomID`
retuns data about that room

Payload - `cookie`

Options
```python
{
    'name': str,
    'unlisted': bool
}
```
Response
```python
{engineUrl: str, auth: str}
``` 
`engineUrl` is websocket url you will be communicating with
`auth` is used to authenticate the room with mafia

#### Example (Create a room)
Creating a room and getting it's ID

=== "Python"
```python
from requests import Session
from json import loads

with Session() as s:
    resp = loads(s.post('https://mafia.gg/api/rooms/',
                        cookies=cookie,
                        json=options).content)
roomId = resp['id']
```

Authenticating room with mafia

=== "Python"
```python
with Session() as s:
    resp = loads(s.get(f"https://mafia.gg/api/rooms/{roomId}",
    cookies=self.user.cookie).content)
    engine, auth = resp['engineUrl'], resp['auth']
```

### Creating a new room
To create a room from the data we have, we need to make a websocket 
connection to the url we retrieved `engine`

Payload
```python
{
    'type': 'clientHandshake',
     'userId': str(userId),
    'roomId': int(roomId), 'auth': str
}
```

#### Example (connection)
=== "Python"
```python
from websockets import connect
ws = await connect(engine, ssl=True)
await ws.dump(json_payload)
response = loads(await self.ws.recv())
```
