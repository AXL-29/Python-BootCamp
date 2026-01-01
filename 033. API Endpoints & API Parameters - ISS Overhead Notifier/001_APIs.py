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

# HTTP Status Codes (What the Server is Telling You)
# HTTP status codes are numbers returned by the server to tell you the result of your API request.

# 1XX: Hold On
# 2XX: Here You Go
# 3XX: Go Away
# 4XX: You Screwed Up
# 5XX: I Screwed Up

# Common Status Code You'll See
# Code      Meaning             What it Means for You
# 200       OK                  Request successeded
# 201       Created             Data was succesfully created
# 400       Bad Request         You sent wrong parameters
# 401       Unauthorized        Missing/invalid API key
# 403       Forbidden           Access denied
# 404       Not Found           Endpoint doesn't exist
# 500       Server Error        Problem on server side

# Exceptions (When Python Says "Something Broke")
# An exception is an error that occurs while your program is running

# Common API-related Exceptions:
# Exception             Cause
# ConnectionError       No internet / API down
# Timeout               API too slow
# HTTPError             Non-200 status code
# KeyError              Missing key in JSON
# ValueError            Invalid data format

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

iss_position = (latitude, longitude)

print(iss_position)