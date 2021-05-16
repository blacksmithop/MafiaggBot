# Authentication

| Method      | Description                          |
| ----------- | ------------------------------------ |
| `GET`       | :material-check:     Fetch resource  |
| `POST`       | :material-check-all: Submit data |

To authenticate with [mafia](https://mafia.gg/) you need to pass
the user token with your POST request

### Getting the cookie
Make a POST request to `https://mafia.gg/api/user-session`
with this payload
```json
{ "login" : username, "password": password }
```

Response
```python
{
    id: str, 
    username: str,
    email: str(email), 
    hostBannedUsernames: list,
    isPatreonLinked: bool,
    activePatreon: bool,
    needsVerification: bool, 
    createdAt: str(timestamp)
}
```

Store this `cookie`

#### Example (Get cookie)
=== "Python"
```python
from requests import Session

with Session() as s:
    cookie = s.post(URL, json={'login': username, 'password': password})
if cookie.status_code == 401:
    raise WrongPassword("You provided incorrect password")
cookie = cookie.cookies.get_dict()
```


