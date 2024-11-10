# ------------------------------------------------------------------------------------------ #
# Title: Assignment03
# Desc: This assignment demonstrates using lists and files to work with data
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# Adam Savage,20241103,Modified file
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
csv_data: str = ''  # Holds combined string data separated by a comma.
file_obj = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
student_data: list = []
students: list = []
row_list: list = []  # to show all data rows in csv_data when writing to file
csv_data_list: list = []  # to show all data rows in csv_data when writing to file

file_obj = open(FILE_NAME, 'r')

# Extract the data from the file
for row in file_obj.readlines():
    # Transform the data from the file
    student_data = row.split(',')
    student_data = [student_data[0], student_data[1], student_data[2].strip()]
    # Load it into our collection (list of lists)
    students.append(student_data)
file_obj.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        student_first_name = input("Enter the student's first name: ")
        student_last_name = input("Enter the student's last name: ")
        course_name = input("Please enter the name of the course: ")
        csv_data += f"{student_first_name},{student_last_name},{course_name}\n"
        continue

    # Present the current data
    elif menu_choice == "2":
        print("\nThe current data is:")
        print(csv_data)
        continue

    # # this commented block is the original "elif" for menu choice 3
    # # Save the data to a file
    # elif menu_choice == "3":
    #     file_obj = open(FILE_NAME, "a")
    #     file_obj.write(csv_data)
    #     file_obj.close()
    #     print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
    #     continue

    # NEW Save the data to a file
    elif menu_choice == "3":
        file_obj = open(FILE_NAME, "a")
        file_obj.write(csv_data)
        file_obj.close()
        # to show all registrations to write when there are multiple in csv_data, convert it to a list then loop through the list to print each registrant
        csv_data_list = csv_data.rstrip().split("\n")  # "rstrip()" removes the trailing "\n" to prevent an empty last item in the list when "split()" separates the string by "\n"
        for row in csv_data_list:  # this for loop prints each registrant to write
            row_list = row.split(",")  # "split()" creates a list from each row/string, separated by ","
            print(f"You have registered {row_list[0]} {row_list[1]} for {row_list[2]}.")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
