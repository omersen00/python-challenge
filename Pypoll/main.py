import os
import csv
# Collect data from the resources folder
csv_file_path = os.path.join("Resources" ,"election_data.csv")
# Declare Varible
total_votes = 0 
Charles_vote = 0
Diana_vote = 0
Raymon_vote = 0
# With open as csv file
with open(csv_file_path) as elections:
    # Store data under the csvreader variable
    csvreader = csv.reader(elections,delimiter=",") 
    header = next(csvreader)     
    # Loop through each row in the csv
    for row in csvreader: 
        total_votes +=1
        # We have three candidates if the name is found, count the times it appears and store in a list
        # We can use this values in our percent vote calculation in the print statements
        if row[2] == "Charles Casper Stockham": 
            Charles_vote +=1
        elif row[2] == "Diana DeGette":
            Diana_vote +=1
        elif row[2] == "Raymon Anthony Doane": 
            Raymon_vote +=1
 # To find the winner we want to make a dictionary out of the two lists we previously created 
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [Charles_vote, Diana_vote,Diana_vote]
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)









# Print a the summary of the analysis
Charles_percent = (Charles_vote/total_votes) *100
Diana_percent = (Diana_vote/total_votes) * 100
Raymon_percent = (Diana_vote/total_votes)* 100



# Print the summary table
print(f"Election Results")
print(f"-")
print(f"Total Votes: {total_votes}")
print(f"-")
print(f"Charles Casper Stockham: {Charles_percent:.3f}% ({Charles_vote})")
print(f"Diana DeGette: {Diana_percent:.3f}% ({Diana_vote})")
print(f"Raymon Anthony Doane: {Raymon_percent:.3f}% ({Diana_vote})")
print(f"-")
print(f"Winner: {key}")
print(f"-")


# Export the results to a test file
f = open("Vote_Results.txt", "w")
f.write(f"-")
f.write(f"Total Votes: {total_votes}")
f.write(f"-")
f.write(f"Charles Casper Stockham: {Charles_percent:.3f}% ({Charles_vote})")
f.write(f"Diana DeGette: {Diana_percent:.3f}% ({Diana_vote})")
f.write(f"Raymon Anthony Doane: {Raymon_percent:.3f}% ({Diana_vote})")
f.write(f"-")
f.write(f"Winner: {key}")
f.write(f"-")



