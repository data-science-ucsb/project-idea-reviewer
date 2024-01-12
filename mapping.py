import pandas as pd
from thefuzz import fuzz
from thefuzz import process

ptoid = {
    "University Clothing resale thing": "pj01-universityclothing",
    "Travel Itinerary Planner": "pj02-travelplanner",
    "IntelliGrocery": "pj03-intelligrocery",
    "Course Organization and Recommendation System (Website)": "pj04-courserecs",
    "Code&Grow": "pj05-codegrow",
    "FoundIt": "pj06-foundit",
    "DSA: Dating's Scientific Algorithm": "pj07-datingalgorithm",
    "Rec Center Helper": "pj08-reccen",
    "live or die with your best friend": "pj09-liveordie",
    "SpotifAI Playlist Cover Generator": "pj10-spotifai",
    "Song/Album Rater": "pj11-songrater",
    "App blocker with Friends ": "pj12-appblocker",
    "Research Helper": "pj13-researchhelper",
    "UCSB Coral": "pj14-ucsbcoral",
}

# Loading the CSV files
file_teams = "pj.csv"
file_students = "gh.csv"

# Reading the CSV files into dataframes
df_teams = pd.read_csv(file_teams)
df_students = pd.read_csv(file_students)

# Melting the df_teams dataframe to have one student per row
df_teams_melted = df_teams.melt(
    id_vars=["Group Nr", "Project Name"],
    value_vars=[
        "student1",
        "student2",
        "student3",
        "student4",
        "student5",
        "student6",
        "student7",
        "student8",
    ],
    var_name="Student Position",
    value_name="Student Name",
)

# Cleaning the student names in both dataframes to facilitate the merge
df_teams_melted["Student Name"] = (
    df_teams_melted["Student Name"].str.strip().str.upper()
)
# remove rows with empty or nan student names
df_teams_melted = df_teams_melted[df_teams_melted["Student Name"].notna()]
df_teams_melted.to_csv("teams_melted.csv")
df_students["full_name"] = (
    df_students["first_name"].str.strip() + " " + df_students["last_name"].str.strip()
)
df_students["full_name"] = df_students["full_name"].str.upper()

# print size of df_students
print("Number of students: " + str(df_students.shape[0]))

# for each student in df_students
for index, row in df_students.iterrows():
  # find the student in df_teams_melted with the same name using fuzzy matching
  # if the student is found, add the project name to the student's row in df_students
  # if the student is not found, add the student's name to a list of unmatched students
  name = row["full_name"]
  print("Looking for: " + name)
  # use token_set_ratio to find the best match
  match = process.extractOne(name, df_teams_melted["Student Name"], scorer=fuzz.token_set_ratio)
  # if the best match is good enough, add the project name to the student's row in df_students
  if match[1] > 80:
    df_students.loc[index, "project_name"] = df_teams_melted.loc[match[2], "Project Name"]
  # if the best match is not good enough, add the student's name to a list of unmatched students
  else:
    df_students.loc[index, "project_name"] = "Not Found"
    print("Not Found: " + name)

# keep only the columns github_username and project_name
df_students = df_students[["github_username", "project_name"]]

# rename project_name to teams
df_students = df_students.rename(columns={"project_name": "teams"})

# replace the project names with the team names
df_students["teams"] = df_students["teams"].replace(ptoid)

# print the # of entries with empty github_username
print("Number of entries with empty github_username: " + str(df_students["github_username"].isna().sum()))

# remove entries with empty github_username
df_students = df_students[df_students["github_username"].notna()]

# write the results to a csv file. Don't use an index column
df_students.to_csv("teams.csv", index=False)