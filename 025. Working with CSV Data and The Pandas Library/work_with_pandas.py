import pandas

data = pandas.read_csv("weather_data.csv")
temperatures = data["temp"]

print(temperatures)