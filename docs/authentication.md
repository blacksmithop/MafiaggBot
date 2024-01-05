# Authentication

User authentication is done as POST request. We can simulate one in order to get the cookies. 
They can then be used to authenticate our requests.


Make a POST request to `https://mafia.gg/api/user-session` with your login credentials

```json
{
    "login": "Mafia.gg Username",
    "password": "Mafia.gg password"
}
```

Save the cookies included with this response