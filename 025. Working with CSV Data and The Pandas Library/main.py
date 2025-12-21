import csv


list_data = []

# with open("weather_data.csv", "r") as data_file:
#     for data in data_file:
#         stripped_data = (data.strip())
#         list_data.append(stripped_data)

with open("weather_data.csv", "r") as file_data:
    data = csv.reader(file_data)
    next(data)

    temperatures = []
    for row in data:
        temp = int(row[1])
        temperatures.append(temp)

print(temperatures)
