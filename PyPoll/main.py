# Import modules os and csv
import os
import csv

# CSV file path
election_csv = os.path.join('python-challenge', 'PyPoll', 'Resources', 'election_data.csv')

# Lists to store data
candidate = []
unique_candidate = []
vote_count = []
vote_percent = []

# Assign Values
votes = 0

# Open CSV
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Loop through data
    for row in csvreader:

        votes = votes + 1

        candidate.append(row[2])

    for x in set(candidate):
        unique_candidate.append(x)

        # y is count votes per candidate
        y = candidate.count(x)
        vote_count.append(y)

        # z is percent votes per candidate
        z = round((y/votes)*100, 3)
        vote_percent.append(z)
        
    winning_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_count)]

# Print to terminal   
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(votes))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

# Print to a text file
output_path = os.path.join('python-challenge','PyPoll','Analysis','election_results.txt')

with open('output_path', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(votes) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")