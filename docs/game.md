# Game
(websocket)
### Start a game
Payload
```python
{"type": "startGame"}
```

### Start a new game
Payload
```python
{'type': 'newGame', 'roomId': int(roomId)}
```

### Send a message
Payload
```python
{'type': 'chat', 'message': str}
```

Response
```python
{message: str,
     from: {model: 'user'/'player',
     userid: int,
     playerid: int}
}
```