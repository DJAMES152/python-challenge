#importing libraries
import os 
import csv
from pathlib import Path 

#setting csv path
csv_file_path = Path("Resources", "election_data.csv")

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

#creating a dictionary of possible candidates
candidate = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_vote, correy_vote,li_vote,otooley_vote]

#correlating the candidate and votes lists together and returning the winner using the max function in the campaign dictionary
campaign_dictionary = dict(zip(candidate,votes))
key = max(campaign_dictionary, key=campaign_dictionary.get)

#creating formulas in order to create results for each candidate
khan_percent = (khan_vote/total_vote) * 100
correy_percent = (correy_vote/total_vote) * 100
li_percent = (li_vote/total_vote) * 100
otooley_percent = (otooley_vote/total_vote) * 100

#printing final results of election
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_vote}")
print(f"-------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_vote})")
print(f"Correy: {correy_percent:.3f}% ({correy_vote})")
print(f"Li: {li_percent:.3f}% ({li_vote})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_vote})")
print(f"-------------------------")
print(f"Winner: {key}")
print(f"-------------------------")

#creating path to election results text file
final_data = Path("Analysis", "election_results.txt")

#opening writable csv file
with open(final_data,"w") as results:

#creating election results text file to be read in layman's terms
    results.write(f"Election Results")
    results.write("\n")
    results.write(f"-------------------------")
    results.write("\n")
    results.write(f"Total Votes: {total_vote}")
    results.write("\n")
    results.write(f"-------------------------")
    results.write("\n")
    results.write(f"Khan: {khan_percent:.3f}% ({khan_vote})")
    results.write("\n")
    results.write(f"Correy: {correy_percent:.3f}% ({correy_vote})")
    results.write("\n")
    results.write(f"Li: {li_percent:.3f}% ({li_vote})")
    results.write("\n")
    results.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_vote})")
    results.write("\n")
    results.write(f"-------------------------")
    results.write("\n")
    results.write(f"Winner: {key}")
    results.write("\n")
    results.write(f"-------------------------")

