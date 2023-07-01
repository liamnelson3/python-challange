# %%
import os
import csv

# %%
os.chdir(r"c:\Users\lanel\OneDrive\Desktop\Data Analytics info\University of Oregon\UO-Data-Analysis-Bootcamp-Public\Module 3\Challange Files\python-challenge\PyBank")

current_directory = os.getcwd()

csv_path = os.path.join(current_directory, 'Resources', 'budget_data.csv')
print(csv_path)

# %%
with open(csv_path, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = list(csv.DictReader(csvfile, delimiter=','))

    #following code inspired by https://learnpython.com/blog/read-csv-into-list-python/
    # reads each column of the csv file to a list using List Comprehension
    dates = [str(row['Date']) for row in csvreader]
    profits = [float(row['Profit/Losses']) for row in csvreader]

# %%
#get Total Months
months_total = len(dates)

# %%
#net total amount of Profit/Losses
net_profits = sum(profits)

# %%
#find the differences between each item in profits and put each result into a list
#see Images folder for a visual explination on how zip(profits[:-1], profits[1:]) works
#code from https://stackoverflow.com/questions/2400840/python-finding-differences-between-elements-of-a-list
profits_dif = [j-i for i, j in zip(profits[:-1], profits[1:])]

# %%
#assign remaining variables based on profits_dif
biggest_profit = max(profits_dif)
biggest_loss = min(profits_dif)
average_profit = sum(profits_dif)/len(profits_dif)

# %%
#get months of biggest profit and biggest lost in profits by finding items in dates with matching index
Max_index = profits_dif.index(max(profits_dif))
Min_index = profits_dif.index(min(profits_dif))
#profits_dif has 1 less item then dates, so +1 is used to ensure proper sync
Max_date = dates[Max_index+1]
Min_date = dates[Min_index+1]

# %%
os.chdir(r"c:\Users\lanel\OneDrive\Desktop\Data Analytics info\University of Oregon\UO-Data-Analysis-Bootcamp-Public\Module 3\Challange Files\python-challenge\PyBank\Analysis")

with open('Financial Analysis.txt', 'w') as writefile:
    writefile.write(f"Financial Analysis\n")
    writefile.write(f"-------------------------\n")
    writefile.write(f"Total Months: {months_total}\n")
    writefile.write(f"Total: ${net_profits}\n")
    writefile.write(f"Average Change: ${average_profit}\n")
    writefile.write(f"Greatest Increase in Profits: {Max_date} (${biggest_profit})\n")
    writefile.write(f"Greatest Decrease in Profits: {Min_date} (${biggest_loss})\n")


