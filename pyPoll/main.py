import os
import sys
sys.modules['itertools']
import csv

# Path to collect data from the folder
election_data_CSV = os.path.join('election_data_2.csv')

#Lists to Store Data
VoterID = []
County = []
Canidate = []

#Dictionary to aggregate data
votingResults = {"Counties"=[County], "Voters" = [VoterID], "Canidates"= [Canidate]}

with open(election_data_CSV, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add Voter ID
        VoterID.append(str(row[0]))
        # Add County
        County.append(row[1])
        # Add Canidate
        Canidate.append(row[2])

sorted_keys = sorted(votingResults)
print(votingResults.get())
print(votingResults["Counties"])
        