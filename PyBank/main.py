import os
import csv

# Path to collect data from Resources folder
budget_data = os.path.join("Resources", "budget_data.csv")

Total_Months = 0
Total_Profit = 0
Total_Change = 0
Change_Months = 0

GincValue = 0
GincDate = ""
    
GdecValue = 0
GdecDate = ""
    


with open(budget_data, "r") as budget_file:
    budget_reader = csv.reader(budget_file, delimiter=",")
    header = next(budget_reader)

    
    # Total Months, Total, & Avg Change
    January_Row = next(budget_reader)
    Total_Months += 1
    Total_Profit += int(January_Row[1])
    Previous_Profit = int(January_Row[1])
    
    for row in budget_reader:
        Total_Months += 1
        Total_Profit += int(row[1])

        
        Change = int(row[1]) - Previous_Profit
        Total_Change += Change
        Change_Months += 1
        
        Previous_Profit = int(row[1])
    
    
        if Change > GincValue:
            GincValue = Change
            GincDate = row[0]
        
        if Change < GdecValue:
            GdecValue = Change
            GdecDate = row[0]
        
    

    
output = f"""
Financial Analysis
----------------------------
Total Months: {Total_Months}
Total: ${Total_Profit}
Average Change: ${Total_Change / Change_Months:.2f}
Greatest Increase in Profits: {GincDate} (${GincValue})
Greatest Decrease in Profits: {GdecDate} (${GdecValue})
"""

print(output)

with open("Analysis/pybank_output.txt", "w") as PyBank_Output:
    PyBank_Output.write(output)