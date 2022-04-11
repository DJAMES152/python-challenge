#Importing Libraries
import os
import csv
from turtle import clear

#path to collect data from the budget data excel sheet
budget_csv = os.path.join('Resources','budget_data.csv')

#define the function and have it print the total
# def print_data(total):

    #defining variables


    # total_months = (months)
    # print_data(total_months)
    # total_profit = nettotal
    # print(sum(total_profit[1]))

#  # def get_no_of_elements(months):
# months = str(total[0])
# def get_no_of_elements(total):
#     count = 0
# for months in months:
#         count += 1
# return  count

# print_data(total_months))

# Open and read csv
filename = open(budget_csv)
file = csv.DictReader(filename)
months = []
nettotal = []
sum = 0

for col in file:
    months.append(col['Date'])
    nettotal.append(col['Profit/Losses'])  

    totalmonths = len(months)
    totalprofit = nettotal

    for i in range(0, len(totalprofit)):
        sum = sum + totalprofit[i]
    print(str(sum))
print("Total Months: ", totalmonths)
print("Total Profit: ", totalprofit)
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")

    count = 1

    for row in csv_reader:
        
       count += 1

    # months = []
    # nettotal = []

    # for col in csv_reader:
    #     months.append(col['Date'])
    #     nettotal.append(col['Profit/Losses'])  
       # print_data(row)

#Removing header row
print("month:", months)
