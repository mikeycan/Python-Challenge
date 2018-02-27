import os
import csv
#import us_state_abbrev

employee_data_csv = os.path.join("employee_data1.csv")

# Lists to store data
EmpID = []
FirstName = []
LastName = []
DOB = []
SSN = []
State = []

us_state_abbrev = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
    'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
    'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
    'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN',
    'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
    'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
    'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
    'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX',
    'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV',
    'Wisconsin': 'WI', 'Wyoming': 'WY',
}

with open(employee_data_csv, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add Employee ID
        EmpID.append(row[0])
        # Split Name into First Name and add
        new_names = row[1].split(" ")
        FirstName.append(new_names[0])
        # Split Name into Last Name and add
        LastName.append(new_names[1])
        # Add DOB in mm/dd/yyyy format
        bdate = row[2].split("-") # splitting dob by '-'
        new_db = bdate[1] + "/" + bdate[2] + "/" + bdate[0] # formatting dob
        dob.append(new_db) # appending formatted dob
        # Add SSN and hiding first 5
        hide_ssn = row[4].split("-")
        SSN.append("***-**-"+ str(hide_ssn[3]))
        #Add State Abb
        State.append(us_state_abbrev[row[4]])
        
# Zip lists together
cleanedEMP_csv = zip(EmpID, FirstName, LastName, DOB, SSN,State)
print(cleanedEMP_csv)
# Set variable for output file
output_file = os.path.join("combined_employee_data.csv")
#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    # Write the header row
    writer.writerow(["Employee ID", "First Name", "Last Name", "Date of Birth",
                     "Social Security Number", "State"])
    # Write in zipped rows
    writer.writerows(cleanedEMP_csv)
