# An Application Programming Interface (API) is a set of commands, functions, protocols, and objects.
# that programmers can use to create software or interact with an external system.

# An API endpoint is a specific URL when you request data from an API.

# API Parameters let you customize what data the API returns.
    # They are usually added to the URL after a "?", and separated by "&".
    # Example: https://api.sunrise-sunset.org/json?lat=14.5995&lng=120.9842&formatted=0

    # lat - Latitude
    # lng - Longitude
    # formatted=0 - returns time in 24-hrs (ISO) format

# An API request is a message sent from one application (the client) 
# to another application (the server) asking for data or an action.

# API Request Flow
# 1. Your program sends a request
# 2. The server receives it
# 3. The server processes the request
# 4. The server sends back a response (usually JSON)

# What's Inside an API Request?
    # Endpoint(URL) - where the request is sent.

# Method (HTTP Verb)
# Tells the server what you want to do.

# Method            Purpose
# GET               Get data
# POST              Send/create data
# PUT               Update data
# DELETE            Remove data

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)