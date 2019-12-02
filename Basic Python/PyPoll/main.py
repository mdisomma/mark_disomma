import csv
import os


file_path = os.path.join('Resources', 'election_data.csv')

total = 0
khan = 0
correy = 0
li = 0
otooley = 0

with open(file_path, newline="", encoding='utf-8') as election:
   csvreader = csv.reader(election, delimiter=",")
   header = next(csvreader)
   for row in csvreader:
           total += 1
           if row[2] == "Khan":
               khan += 1
           elif row[2] == "Correy":
               correy += 1
           elif row[2] == "Li":
               li += 1
           elif row[2] == "O'Tooley":
               otooley += 1
               
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
vote_total_candidates = [khan, correy, li, otooley]

combined_dict = dict(zip(candidates, vote_total_candidates))
key = max(combined_dict, key=combined_dict.get)

khan_percent_vote = (khan/total) *100
correy_percent_vote = (correy/total) *100
li_percent_vote = (li/total) *100
otooley_percent_vote = (otooley/total) *100

print(f"Election Results")
print(f"----------------")
print(f"Total Votes: {total}")
print(f"----------------")
print(f"Khan: {khan_percent_vote:.2f}%  ({khan})")
print(f"Correy: {correy_percent_vote:.2f}%  ({correy})")
print(f"Li: {li_percent_vote:.2f}%  ({li})")
print(f"O'Tooley: {otooley_percent_vote:.2f}%  ({otooley})")
print(f"----------------")
print(f"Winner: {key}")
print(f"----------------")

output_file = os.path.join('Resources', 'election_final.csv')

with open(output_file, "w") as file:
   file.write(f"Election Results")
   file.write("\n")
   file.write(f"Total Votes: {total}")
   file.write("\n")
   file.write(f"Khan: {khan_percent_vote:.2f}% ({khan})")
   file.write("\n")
   file.write(f"Correy: {correy_percent_vote:.2f}% ({correy})")
   file.write("\n")
   file.write(f"Li: {li_percent_vote:.2f}% ({li})")
   file.write("\n")
   file.write(f"O'Tooley: {otooley_percent_vote:.2f}% ({otooley})")
   file.write("\n")
   file.write(f"Winner: {key}")
   file.write("\n")
