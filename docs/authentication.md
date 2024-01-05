# Authentication

User authentication is done as POST request, we can simulate one in order to get the cookies.
The cookies are then used to authenticate the rest of our requests.
*Almost* every requests to the mafia gg api needs to be authenticated.


Make a POST request to `https://mafia.gg/api/user-session`

with the payload
```
{
    "login": "Mafia.gg Username",
    "password": "Mafia.gg password"
}
```

From this response save it's cookies