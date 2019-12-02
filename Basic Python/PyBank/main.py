import os 
import csv
import numpy as np

csvpath = os.path.join('Resources', 'budget_data.csv')

dates = []
total = []
list_of_changes = []
initial_change = [0]
with open(csvpath, newline= '') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        dates.append(row[0])
        total.append(int(row[1]))
               

total_profit = sum(total) 
total_months = len(dates)
for i in range(1, len(total)):
    changes_profit_loss = total[i]-total[i-1]
    list_of_changes.append(int(changes_profit_loss))

average_difference = round(np.mean(list_of_changes),2)
zipped_list = initial_change + list_of_changes

months_profit_change_dict = dict(zip(dates, zipped_list))
max_value = max(zip(months_profit_change_dict.values(), months_profit_change_dict.keys()))
min_value = min(zip(months_profit_change_dict.values(), months_profit_change_dict.keys()))

print(f"Financial Analysis")
print("---------------------")
print(f"Total Months:",total_months)
print(f"Total: $",total_profit)
print(f"Average Change: $",average_difference)
print(f"Greatest Increase in Profits: $",max_value)
print(f"Greatest Decrease in Profits: $",min_value)

output_file = os.path.join('Resources', 'budget_data_final.txt')

with open(output_file, "w") as file:
    file.write(f"Financial Analysis")
    file.write("\n")
    file.write("---------------------")
    file.write("\n")
    file.write(f"Total Months: " + str(total_months))
    file.write("\n")
    file.write(f"Total: $" + str(total_profit))
    file.write("\n")
    file.write(f"Average Change: $" + str(average_difference))
    file.write("\n")
    file.write(f"Greatest Increase in Profits: $" + str(max_value))
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: $" + str(min_value))
    file.write("\n")
