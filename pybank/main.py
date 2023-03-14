import os
import csv
total_months = []
total_profit = []
monthly_profit_change = []
budget_data = os.path.join("Resources", "budget_data.csv")
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)  
    # Loop through the rows in the stored file contents
    for row in csv_reader: 
        # Append the total months and total profit to their corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    # In order to get the monthly change in profits
    for i in range(len(total_profit)-1):
        # Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        



# Get max and min of the the montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)




# Match max and min to the proper month using month list and index from max and min


#We use the plus 1 at the end since month associated with change is the + 1 month or next month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 






print("Financial Analysis")
print("-")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

f = open("Budget_data_results.txt", "w")
f.write("Financial Analysis")
f.write("-")
f.write(f"Total Months: {len(total_months)}")
f.write(f"Total: ${sum(total_profit)}")
f.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
f.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
f.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")





