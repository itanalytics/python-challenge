import os
import csv

#csvpath = os.path.join('..','Resources','budget_data.csv')
csvpath = 'C://Users/ivanv/Desktop/Bootcamp/python-challenge/PyBank/Resources/budget_data.csv'

#Variables to hold statistics and calculations
months = 0
net_total = 0
tot_change = 0
top_inc = 0
top_dec = 0
inc_date =''
dec_date= ''
previous_pl = 0
#Create dictionary to hold values from CSV & to perform calculations on
pl_changes = {}

#Read in csv file 
with open (csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Read and store header, not include in calculations
    csv_header = next(csvreader)
    #Store values from csv in dictionary
    #key = date, value = list of ints[P/L Amount , Change in P/L]    
    for row in csvreader:
        
        pl_changes[row[0]]=[int(row[1]),int(row[1])-previous_pl]
        previous_pl = int(row[1])
        
    
    #Perform calculations on values stored in dictionary    
for x in pl_changes.keys():
    #Sum of total P/L amounts
    net_total += pl_changes[x][0]
    #Sum of total P/L changes
    tot_change += pl_changes[x][1]
    #Record greatest increase & decrease, with corresponding dates
    if pl_changes[x][1] > top_inc:
        top_inc = pl_changes[x][1]
        inc_date = x
        
    elif pl_changes[x][1] < top_dec:
        top_dec = pl_changes[x][1]
        dec_date = x

    
#Calculate total months    
months = len(pl_changes)
#Calculate average change, accounting for first month
first_month = list(pl_changes.keys())[0]
avg_change = (tot_change - pl_changes[first_month][1]) / (months -1)   

#Print analysis summary to Terminal
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {months}')
print(f'Total: ${net_total}')
print(f'Average Change: {avg_change.__round__(2)}')
print(f'Greatest Increase in Profits: {inc_date} (${top_inc})')
print(f'Greatest Decrease in Profits: {dec_date} (${top_dec})')


#Print analysis to output text file in Analysis folder
#output_path = os.path.join('..','Analysis','budget_analysis.txt')
output_path = r'C:\Users\ivanv\Desktop\Bootcamp\python-challenge\PyBank\Analysis\budget_analysis.txt'

with open(output_path, 'w') as txtfile:

    txtfile.write('Financial Analysis\n')
    txtfile.write('----------------------------\n')
    txtfile.write(f'Total Months: {months}\n')
    txtfile.write(f'Total: ${net_total}\n')
    txtfile.write(f'Average Change: {avg_change.__round__(2)}')
    txtfile.write(f'Greatest Increase in Profits: {inc_date} (${top_inc})\n')
    txtfile.write(f'Greatest Decrease in Profits: {dec_date} (${top_dec})\n')