import sys
import random
import pandas as pd
from io import StringIO

# Get the CSV file path from the command line
csv_path = sys.argv[1]

# Read the CSV file
with open(csv_path, "r") as f:
    csv_data = f.read()

# Convert the original CSV data to DataFrame
df_original = pd.read_csv(StringIO(csv_data))

# Define the new CSV format
columns_new = [
    "Enrl Cd",
    "Perm #",
    "Grade",
    "Final Units",
    "Student Last",
    "Student First Middle",
    "Quarter",
    "Course ID",
    "Section",
    "Meeting Time(s) / Location(s)",
    "Email",
    "ClassLevel",
    "Major1",
    "Major2",
    "Date/Time",
    "Pronoun",
]

# Creating a new DataFrame with the desired format
df_new = pd.DataFrame(columns=columns_new)

# Adding the relevant data from the original DataFrame to the new DataFrame
df_new["Student Last"] = df_original["Last name"]
df_new["Student First Middle"] = df_original["First name"]
df_new["Email"] = df_original["School Email"]

# set each Perm # to a random unique positive integer
perm = []
for i in range(len(df_original)):
    perm.append(random.randint(1, 100000))
df_new["Perm #"] = perm

# set each Enrl Cd to 12
df_new["Enrl Cd"] = 12

# Export to student_data.csv
df_new.to_csv("student_data.csv", index=False)

# open the student_data.csv file and insert ",,,,,,,,,,,,,,," at the second line
with open("student_data.csv", "r") as f:
    lines = f.readlines()
    lines.insert(1, ",,,,,,,,,,,,,,,\n")
with open("student_data.csv", "w") as f:
    f.writelines(lines)
