import csv

with open("datasets/customers-100.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["First Name"], row["City"])