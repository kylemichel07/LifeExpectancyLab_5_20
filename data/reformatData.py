import json


f1 = open("data/life_expectancy_clean.csv", "r")
lines = f1.readlines()

#iterate through the list of lines, then split each line into its own list, then go through that list and create a dictionary with year being the key and life expectancy the value
dictionary = {}

header = lines[0].strip().split(",")
year_start_index = 4
years = header[year_start_index:]

for line in lines[1:]:
    row = line.strip().split(",")
    country = row[0]
    year_values = row[year_start_index:]

    year_dict = {
        year: float(value)
        for year, value in zip(years, year_values)
        if value.strip()
    }

    dictionary[country] = year_dict
    

print(dictionary["Canada"]['1960'])


# Create the dictionary here

f1.close()

#Save the json object to a file
f2 = open("life_expectancy.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()
