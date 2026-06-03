"""File I/O & error handling | AI-assisted debugging (safely) 

4h learning  +  4h team support 

Python topics 

open(), read(), write(), context managers (with) 

CSV reading and writing with the csv module 

try / except / finally, raising exceptions 

Custom exception classes. """

# File I/O & error handling | AI-assisted debugging (safely) 
# file_path = "analysys.txt"
# try:
#     with open(r"C:\Users\SRS\Documents\analysys.txt", 'r') as file:
#         content = file.read()
#     print(content)   # properly indented inside try
# except FileNotFoundError:
#     print("File not found!")
# 
# # at the same time how to write in a file and update it
# file_path = r"C:\Users\SRS\Documents\analysys.txt"
# 
# try:
#     with open(file_path, 'w') as file:
#         file.write("This is a new line of text.")
#     print("File written successfully!")
# except FileNotFoundError:
#     print("The folder path does not exist.")
# except PermissionError:
#     print("You don't have permission to write to this location.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")


#CSV reading and writing with the csv module #try / except / finally, raising exceptions 
import csv
csv_file_path = r"C:\Users\SRS\Desktop\Python_21_Days_Practice\pythonweek1\data.csv"
try:
    with open(csv_file_path,"r")as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("The specified CSV file was not found.")
except PermissionError:
    print("Permission denied: unable to open the CSV file.")

