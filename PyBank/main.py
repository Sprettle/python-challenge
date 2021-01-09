# Import modules os and csv
import os
import csv

# CSV file path
budget_csv = os.path.join('python-challenge', 'PyBank', 'Resources', 'budget_data.csv')

# Lists to store data
date = []
profit = []
monthly_changes = []

# Assign Values
months = 0
initial_profit = 0
total_profit = 0
change_profits = 0

# Open the CSV 
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Loop through data
    for row in csvreader:    
      
      months = months + 1

      date.append(row[0])
      profit.append(row[1])

      # Calculate the total profit
      total_profit = total_profit + int(row[1])

      #Calculate the average change in profits 
      month_profit = int(row[1])
      monthly_profits = month_profit - initial_profit

      #Store monthly changes in a list
      monthly_changes.append(monthly_profits)

      change_profits = change_profits + monthly_profits
      initial_profit = month_profit

      #Calculate the average change in profits
      average_change_profits = (change_profits/months)
      
      #Find the max and min change in profits
      increase_profits = max(monthly_changes)
      decrease_profits = min(monthly_changes)

      increase_date = date[monthly_changes.index(increase_profits)]
      decrease_date = date[monthly_changes.index(decrease_profits)]
      
   # Print to terminal 
    print("Financial Analysis")
    print("------------------------------")
    print("Total Months: " + str(months))
    print("Total: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(decrease_profits) + ")")
   
# Print to a text file
output_path = os.path.join('python-challenge','PyBank','Analysis','Financial Analysis.txt')

with open('output_path', 'w') as text:
    text.write("Financial Analysis"+ "\n")
    text.write("--------------------------\n")
    text.write("Total Months: " + str(months) + "\n")
    text.write("Total: " + "$" + str(total_profit) +"\n")
    text.write("Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(increase_profits) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(decrease_profits) + ")\n")
  