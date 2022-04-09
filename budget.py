# importing required modules
import os
import csv

print(os.getdir)
# Setting path to csv file for required Data
budget_data = os.path.join("budget_data.csv" )

#Setting Variables for the empty lists
Months = []
Profit = []
profit_change_per_month = []
Greatest Increase = []
Greatest Decrease = []

#Opening statistics csv file through new variable
with open(budget_data,newline="") as budgetcsv
    
    # Creating variable for 
    read_budget = csv.reader(budgetcsv, delimiter=",")

    header = next(read_budget)

    for row in read_budget:

        # Logging total months and profit into their own respectible lists
        all_months.append(row[0])
        all_profit.append(int(row[1]))

    # Length of Profit list
    for i in range(len(all_profit)-1)   

        # Appended profit change data formula
        profit_change_per_month.append(all_profit[i+1]-all_profit[i])

# Gathering minimum/maximum of monthly profit change data
max_profit_increase = max(profit_change_per_month)
max_profit_decrease = min(profit_change_per_month)

# Combining Min/Max monthly profit change data with proper months
max_month_increase = profit_change_per_month(max(profit_change_per_month)) + 1
max_month_decrease = profit_change_per_month(min(profit_change_per_month)) + 1

#Printing Final Results

print ("Final Budget Data")
print (f"Total Months: {len(Months)}")
print (f"Total Profit: ${sum(Profit)})")
print (f"Average Profit Change: {round(sum(profit_change_per_month)/len(profit_change_per_month), 2)})
print (f"Greatest Profit Increase: {Months[max_month_increase]} (${(str(max_profit_increase))})")
print (f"Greatest Profit Decrease: {Months[max_month_decrease]} (${(str(max_profit_decrease))})")



