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

