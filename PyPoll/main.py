import os
import csv

#CSV file with election data
csvpath = os.path.join('Resources','election_data.csv') 

#Variables for counting vote totals, holding winner's name 
total_votes = 0
pop_vote = 0
winner =''

#Dictionaries to hold candidate/vote data 
candidates_dict = {}
vote_dict = {}

#Read in csv
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Read and store header, not include in calculations
    csv_header = next(csvreader)
    #Store values from csv in dictionary
    #key = candidate, create new key for each candidate
    #value = Ballot ID, each represents 1 vote for candidate    
    for row in csvreader:
        if row[2] in candidates_dict.keys():   
            candidates_dict[row[2]].append(row[0])
            total_votes += 1
        else:
            candidates_dict[row[2]] = [row[0]]
            total_votes += 1

#Print analysis to terminal
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')

#Loop through candidates to print name, percentage of votes, and quantity
for c in candidates_dict.keys():
    print(f'{c}: {(len(candidates_dict[c]) / total_votes*100).__round__(3)}% ({len(candidates_dict[c])}) ')
    #create a dictionary of key value pairs: (Candidates : Vote Total)
    vote_dict[c]= len(candidates_dict[c])

print('-------------------------')

#Loop through vote totals to determine winner of popular vote
for v in vote_dict.keys(): 
    if vote_dict[v] > pop_vote:
        pop_vote = vote_dict[v]
        winner = v

print(f'Winner: {winner}')
print('-------------------------')

#Write analysis to output text file in Analysis folder
output_path = os.path.join('Analysis','election_analysis.txt')

with open(output_path, 'w') as txtfile:

    txtfile.write('Election Results\n')
    txtfile.write('-------------------------\n')
    txtfile.write(f'Total Votes: {total_votes}\n')
    txtfile.write('-------------------------\n')
    for c in candidates_dict.keys():
        txtfile.write(f'{c}: {(len(candidates_dict[c]) / total_votes*100).__round__(3)}% ({len(candidates_dict[c])})\n')
    txtfile.write('-------------------------\n')
    txtfile.write(f'Winner: {winner}\n')
    txtfile.write('-------------------------\n')
