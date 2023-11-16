import csv
import json

data = {
    "destinationAirports": ["AUH", "BAH", "DOH", "RYU", "CAI"],
    "data": {"July 2017": {}},
}


airports = set()

with open("survey3.csv") as f:
    reader = csv.reader(f)
    next(reader)  # skip header row

    for row in reader:
        departure = row[0]
        arrival = row[1]
        airports.add(departure)
        airports.add(arrival)

print(airports)
