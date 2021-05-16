# Presence
(websocket)

This is used to indicate to mafia whether you are a Player/Spectator
Payload
```python
{'type': 'presence', 'isPlayer': bool}
```
A value of `isPlayer` `False` means that you're a spectator
while a value of `True` means you're a player