import pandas

data = pandas.read_csv("weather_data.csv")

# get the column value:
day = data.day
print(day)

day = data["day"]
print(day)

# get the row value:
monday = data[data.day == "Monday"]
mon_temp_F = (monday.temp * 9/5) + 32

print(mon_temp_F)

max_temp = data[data.temp == data.temp.max()]
print(max_temp)

# create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

new_data_frame = pandas.DataFrame(data_dict)
new_data_frame.to_csv("new_data.csv")
print(new_data_frame)

