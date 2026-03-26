import csv

with open("results.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)