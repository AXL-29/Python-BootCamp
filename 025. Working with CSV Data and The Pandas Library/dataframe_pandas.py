import pandas as pd  # using 'pd' as an alias for pandas

# Load the CSV file
data = pd.read_csv("data.csv")

# Count occurrences of each fur color
gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

# Create a dictionary with fur color counts
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

# Convert the dictionary to a DataFrame for a cleaner output (optional)
summary_df = pd.DataFrame(data_dict)

# Print the data dictionary or DataFrame
print(summary_df)
