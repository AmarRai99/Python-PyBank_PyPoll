# Import the modules 

import os
import csv
import statistics

# Give the relative path for CSV file

csvpath = ("/Users/amarrai/Desktop/python-challenge/PyPoll/Resources/election_data.csv")

# Define Variables, list of Data, Dictionary and the winners place. 
Comparing_Percentages = []
TotalVotes = 0 
Compare_Library = {}
Percentages = {}
Candidate_Votes = {}
Winner = "Winning Candidate:"

# Read the data from CSV file. Open the CSV file.
# Use Delimiter

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    # Find Total number of votes
    # Add the candidates and their votes to the dictionary.
    # Different candidates need to be added to list.
    # If the candidates do not differ, add a vote.
    for row in csvreader:
         TotalVotes = TotalVotes + 1
         if row[2] not in Candidate_Votes:
            Candidate_Votes[row[2]] = 1
         else:
            Candidate_Votes[row[2]] += 1

# Percentage of votes by Candidate: Divide Votes by candiates by total number of votes
for Candidate in Candidate_Votes:
    Percentage_Vote = Candidate_Votes[Candidate] / TotalVotes

# Percetage formatting and add cadidates percentage to library.
# Use 'append' to add the percentages in a list.
    Percentage_Change_For_Votes = "{:.3%}".format(Percentage_Vote)
    Percentages[Candidate] = Percentage_Change_For_Votes
    Comparing_Percentages.append(Percentage_Change_For_Votes)
    Compare_Library[Percentage_Change_For_Votes] = Candidate

# Calculate Winner
    Winner = Compare_Library[max(Comparing_Percentages)]

# Print Results and use a loop for each candidates results.
print(" ")
print("Election Results")
print("-------------------------------------")
print(f"TotalVotes:  {TotalVotes}")
print("-------------------------------------")

for Candidate in Candidate_Votes:
    print(f"{Candidate}: {Percentages[Candidate]} ({Candidate_Votes[Candidate]})")
print("-----------------------------------")
print(f"Winner: {Winner}")
print("-----------------------------------")

# Write the results as a text file with the titles.
f = open("/Users/amarrai/Desktop/python-challenge/PyPoll/analysis/Election_Analysis.txt", 'w')

f.write("Election Results\n")
f.write("------------------------------------\n")
f.write(f"Total Votes: {TotalVotes}\n")
f.write("------------------------------------\n")
for Candidate in Candidate_Votes:
    f.write(f"{Candidate}: {Percentages[Candidate]} ({Candidate_Votes[Candidate]})\n")
f.write("------------------------------------\n")
f.write(f"Winner: {Winner}\n")
f.write("------------------------------------\n")
f.close()



