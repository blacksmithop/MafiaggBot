from urllib.parse import quote_plus

username = quote_plus("user")
password = quote_plus("password")
uri = "mongodb://%s:%s@localhost" % (username, password)
