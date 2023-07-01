# %%
import os
import csv

# %%
os.chdir(r"c:\Users\lanel\OneDrive\Desktop\Data Analytics info\University of Oregon\UO-Data-Analysis-Bootcamp-Public\Module 3\Challange Files\python-challenge\PyPoll")

current_directory = os.getcwd()

csv_path = os.path.join(current_directory, 'Resources', 'election_data.csv')
print(csv_path)

# %%
with open(csv_path, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = list(csv.DictReader(csvfile, delimiter=','))

    #following code inspired by https://learnpython.com/blog/read-csv-into-list-python/
    # reads each column of the csv file to a list using List Comprehension
    ballot = [int(row['Ballot ID']) for row in csvreader]
    county = [str(row['County']) for row in csvreader]
    name = [str(row['Candidate']) for row in csvreader]

#create zipped list (result is a list of tuples)
voting_zipped = list(zip(ballot, county, name))

# %%
#get total amount of voters
voter_amount = len(voting_zipped)
voter_amount

# %%
#get amount of votes each canidate recieved
charles_total = [i for i in name if i == 'Charles Casper Stockham']
diana_total = [i for i in name if i == 'Diana DeGette']
raymon_total = [i for i in name if i == 'Raymon Anthony Doane']

# %%
#get percentages
charles_percentage = (len(charles_total)/voter_amount) * 100
diana_percentage = (len(diana_total)/voter_amount) * 100
raymon_percentage = (len(raymon_total)/voter_amount) * 100


# %%
#assign canidate with highest percentage of votes to variable
voter_list = [charles_percentage, diana_percentage, raymon_percentage]
voter_dict = {'Charles Casper Stockham':charles_percentage, 'Diana DeGette':diana_percentage, 'Raymon Anthony Doane':raymon_percentage}
#code from https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/
highest_percentage = [i for i in voter_dict if voter_dict[i] == max(voter_list)]
winner = highest_percentage[0]
winner

# %%
os.chdir(r"c:\Users\lanel\OneDrive\Desktop\Data Analytics info\University of Oregon\UO-Data-Analysis-Bootcamp-Public\Module 3\Challange Files\python-challenge\PyPoll\Analysis")

with open('Election Results.txt', 'w') as writefile:
    writefile.write(f"Financial Analysis\n")
    writefile.write(f"-------------------------\n")
    writefile.write(f"Total Votes: {voter_amount}\n")
    writefile.write(f"-------------------------\n")
    writefile.write(f"Charles Casper Stockham: {charles_percentage}%\n")
    writefile.write(f"Diana DeGette: {diana_percentage}%\n")
    writefile.write(f"Raymon Anthony Doane: {raymon_percentage}%\n")
    writefile.write(f"-------------------------\n")
    writefile.write(f"Winner: {winner}\n")
    writefile.write(f"-------------------------\n")


