import pandas as pd
from datetime import datetime, timedelta

# Load the CSV file into a DataFrame
df = pd.read_csv('Employee.csv')

# Remove rows with null values
df.dropna(inplace=True)

# Sort the DataFrame by 'Employee Name' and 'Working Date'
df.sort_values(['Employee Name', 'Working Date'], inplace=True)

# Initialize variables for consecutive days and previous checkout time
consecutive_days = 0
prev_checkout_time = None

# Iterate through the DataFrame
for index, row in df.iterrows():
    # Attempt to parse the 'Working Date' column to datetime
    try:
        working_date = pd.to_datetime(row['Working Date'], format='%Y-%m-%d')
    except ValueError:
        print(f"Invalid date format for '{row['Working Date']}' at row {index + 1}. Skipping this row.")
        continue

    # Attempt to parse check-in and check-out times
    try:
        checkin_time = datetime.strptime(row['Working Check in time'], '%H:%M:%S')
        checkout_time = datetime.strptime(row['Woking Check out time'], '%H:%M:%S')
    except ValueError:
        print(f"Invalid time format for check-in or check-out at row {index + 1}. Skipping this row.")
        continue

    # Calculate time difference between check-in and check-out
    time_diff = checkout_time - checkin_time

    # Check if the employee has worked for more than 14 hours in a single shift
    if time_diff.total_seconds() / 3600 > 14:
        print(f"Employee_Name: {row['Employee Name']} \n (Position ID: {row['Position ID']}) \n worked more than 14 hours on {working_date}")

    # Check for consecutive days and less than 10 hours between shifts
    if prev_checkout_time is not None:
        time_between_shifts = checkin_time - prev_checkout_time
        if time_between_shifts.total_seconds() / 3600 < 10 and time_between_shifts.total_seconds() / 3600 > 1:
            print(f"Employee_Name: {row['Employee Name']} \n (Position ID: {row['Position ID']}) \n has less than 10 hours between shifts on {working_date}")

    # Check if there's a next row and if the current row and the next row have the same employee name
    if index + 1 < len(df) and row['Employee Name'] == df.iloc[index + 1]['Employee Name']:
        # Check if the next date is consecutive to the current date
        next_working_date = pd.to_datetime(df.iloc[index + 1]['Working Date'], format='%Y-%m-%d')
        if (next_working_date - working_date).days == 1:
            consecutive_days += 1
            if consecutive_days > 6:
                print(f"Employee_Name: {row['Employee Name']} \n (Position ID: {row['Position ID']}) \n has worked for 7 consecutive days from {working_date - timedelta(days=6)} to {next_working_date}")
        else:
            consecutive_days = 0
    else:
        consecutive_days = 0

    prev_checkout_time = checkout_time

# Save the cleaned DataFrame back to a new CSV file which dont have null values
df.to_csv('CleanedEmployee.csv', index=False)
