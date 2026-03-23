import csv

data = [
    ["name", "age", "city"],
    ["Harshit", 23, "Udaipur"],
    ["Neha", 21, "Ajmer"]
]

with open("newfile.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerows(data)