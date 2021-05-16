# Ping
(websocket)

Is used to ping the mafia websocket

Payload
```python
{"type": "ping"}
```
Response
```python
{timestamp: int(timestamp), sid: int}
```