# Nesting a dictionary - by putting a value as list and dictionary
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Stuttgart"]
}

print(travel_log["France"][1])  # accessing item via indexing

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

# nesting a dictionary inside a dictionary

my_travel_log = {
    "France": {
        "num_times_visited": 3,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": ["Stuttgart", "Berlin"],
    "total_visits": 5
}

print(my_travel_log["Germany"][0])