#Importing Libraries
import os
import csv

#path to collect data from the budget data excel sheet
budget_csv = os.path.join('Resources','budget_data.csv')

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")