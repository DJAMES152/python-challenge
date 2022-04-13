#Importing Libraries
import os
import csv

#path to collect data from the budget data excel sheet
budget_csv = os.path.join('Resources','budget_data.csv')

#setting variables and empty lists
months = []
netprofit = []
mon_profit_change = []

#opening csv and reader
with open(budget_csv) as budget:
    csv_reader = csv.reader(budget, delimiter=",")

    #setting up to read header row first
    csv_header = next(csv_reader)

    #cycle through rows in csv file
    for row in csv_reader:
        
        #appending months and profits lists
        months.append(row[0])
        netprofit.append(int(row[1]))
    
    #monthly profit change formula
    for i in range(len(netprofit)-1):
        
        #taking difference between two seperate months calculated into the profit change of both
        mon_profit_change.append(netprofit[i+1]-netprofit[i])

#creating variables for maximum and minimum monthly profit changes
max_increase = max(mon_profit_change)
max_decrease = min(mon_profit_change)

#giving variable to maximium and minimum index list to grab data from
month_increase = mon_profit_change.index(max(mon_profit_change)) +1
month_decrease = mon_profit_change.index(min(mon_profit_change)) +1

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(netprofit)}")
print(f"Average Change: {round(sum(mon_profit_change)/len(mon_profit_change), 2)}")
print(f"Greatest Increase in Profits: {months[month_increase]} (${(str(max_increase))})")
print(f"Greatest Decrease in Profits: {months[month_decrease]} (${(str(max_decrease))})")