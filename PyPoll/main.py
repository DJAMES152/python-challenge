#importing libraries
import os 
import csv
from pathlib import Path 

#setting csv path
csv_file_path = Path("python-challenge", "PyPoll", "election_data.csv")

#setting variables 
total_vote = 0 
khan_vote = 0
correy_vote = 0
li_vote = 0
otooley_vote = 0

#opening readable csv file
with open(csv_file_path,newline="", encoding="utf-8") as campaign:

    #creating usuable csv variable
    csvreader = csv.reader(campaign,delimiter=",") 

    #skipping header row
    header = next(csvreader)     

    #go through each row of data
    for row in csvreader: 

        #counting all votes in dataset
        total_vote +=1

        #counting one vote per individual candidate accordingly using an if statement
        if row[2] == "Khan": 
            khan_vote +=1
        elif row[2] == "Correy":
            correy_vote +=1
        elif row[2] == "Li": 
            li_vote +=1
        elif row[2] == "O'Tooley":
            otooley_vote +=1
