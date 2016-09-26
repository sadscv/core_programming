import csv

with open('data.csv', 'r') as f:
    csv_file = csv.reader(f, delimiter=",")
    for line in csv_file:
        print(line)