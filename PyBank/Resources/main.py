# Import os, csv and statistics
import os 
import csv
import statistics

# Create a filepath for CSV File from computer
filepath = "/Users/amarrai/Desktop/python-challenge/PyBank/Resources/budget_data.csv"

# Defining Variables
Count_of_months = 0
Total_amount= 0
GreatestIncrease = 0
GreatestDecrease = 0
BestMonth = ''
WorstMonth = ''

# Create a list for the data
Change = []
Changes_MonthToMonth = []

# Read the data from the CSV file path by opening.
with open(filepath, newline='') as csvfile:

# Split the data using commas with the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
# Read and print the header
    csv_header = next(csvreader)

# Read each row of the data following the header
    for row in csvreader:

#Print (row)
        Count_of_months += 1

        Current_amount = int(row[1])
        Previous_amount = 0
        Total_amount += Current_amount
        if len(Change) >0:
            Previous_amount = Change[-1]
        if Current_amount - Previous_amount > GreatestIncrease:
            BestMonth = (row[0])
            GreatestIncrease = Current_amount - Previous_amount
        elif Current_amount - Previous_amount < GreatestDecrease:
            WorstMonth = (row[0])
            GreatestDecrease = Current_amount - Previous_amount

        Change.append(Current_amount) 

# Track monthly changes
for i in range(len(Change)-1):
    MonthlyChange = (Change[i+1] - Change[i])
    Changes_MonthToMonth.append(MonthlyChange)

    AverageChange = statistics.mean(Changes_MonthToMonth)

print("Financial Analysis")
print("___________________________________")
        
print("Total Months: " + str(Count_of_months))
print("Total: $" + str(Total_amount))
print("Average Change is: $" + str(round(AverageChange, 2)))
print("Greatest Increase in Profits: " + str(BestMonth) + "  ($" + str(GreatestIncrease) + ")")
print("Greatest Decrease in Profits: " + str(WorstMonth) + "  ($" + str(GreatestDecrease) + ")")


# Finally, write this to an output text file
f = open("/Users/amarrai/Desktop/python-challenge/PyBank/analysis,financial_analysis.txt", "w")
f.write("Financial Analysis\n")
f.write("__________________________________________\n")

f.write(f"Total Months:" + str(Count_of_months)+"\n")
f.write(f"Average Change is: $" + str(round(AverageChange, 2))+"\n")
f.write(f"Total: $" + str(Total_amount)+"\n")
f.write(f"Greatest Increase in Profits: " + str(BestMonth) + "($" + str(GreatestIncrease) + ")\n")
f.write(f"Greatest Decrease in Profits: " + str(WorstMonth) + "($" + str(GreatestDecrease) + ")")
f.close()





