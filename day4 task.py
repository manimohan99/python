"""File I/O & error handling | AI-assisted debugging (safely) 

4h learning  +  4h team support 

Python topics 

open(), read(), write(), context managers (with) 

CSV reading and writing with the csv module 

try / except / finally, raising exceptions 

Custom exception classes. """

# File I/O & error handling | AI-assisted debugging (safely) 
file_path="example.txt"
try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)