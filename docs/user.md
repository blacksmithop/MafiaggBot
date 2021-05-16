# User

### Get user by ID

To get a user by their ID, make a GET request to
`https://mafia.gg/api/users/userID`

Response
```python
{id: int, username: str,
 activepatreon: bool,
 createdAt: str(timestamp)}
```

### See your user data
Make a GET request to `https://mafia.gg/api/user`

Response - Same as `https://mafia.gg/api/user-session`