# BlueJay_Intrnship
Bluejay internship assignment for the internship of data analysis 

# Employee Data Processing Script

**Overview**
This Python script is designed to process employee data stored in a CSV file named 'Employee.csv'. The script performs various data cleaning and validation tasks on the employee data, such as checking for invalid date and time formats, identifying employees who worked more than 14 hours in a single shift, and tracking consecutive working days with less than 10 hours between shifts. The cleaned data is then saved to a new CSV file named 'OutputEmployeeData.csv'.

**Prerequisites**
Before running the script, you'll need the following:

Python 3.x installed on your system.

The pandas library for data manipulation. You can install it using pip:

shell
Copy code
```
pip install pandas
```
The datetime library for date and time handling. It is part of Python's standard library and does not require a separate installation.

How to Use
#Prepare Your Data

Ensure that you have a CSV file named 'Employee.csv' containing employee data in the same directory as the script. The data should include columns like 'Employee Name,' 'Working Date,' 'Working Check in time,' and 'Working Check out time.'

#Run the Script

Execute the script by running the Python file in your terminal or preferred Python development environment:

shell
Copy code
```
python script.py
```
The script will read 'Employee.csv,' process the data, and print any validation messages or issues it encounters during processing.

#View Cleaned Data

The cleaned employee data will be saved to a new CSV file named 'OutputEmployeeData.csv' in the same directory as the script. You can open this file to review the cleaned data.

#Data Processing Details
The script uses the pandas library to load and manipulate the data in a DataFrame.
It checks for null values and removes rows with missing data.
Date and time formats are validated, and invalid entries are skipped.
It calculates the time difference between check-in and check-out times to identify shifts exceeding 14 hours.
Consecutive working days with less than 10 hours between shifts are tracked.
The cleaned data is saved to 'OutputEmployeeData.csv' without the index column.
Issues and Contributions
If you encounter any issues or have suggestions for improvements, please feel free to open an issue or create a pull request in this GitHub repository.

You can customize this README to include additional information or specific usage instructions if needed. This provides users with a clear understanding of what the script does and how to use it effectively.
Some basic Git commands are:
```
git status
git add
git commit
```




