#program to print contents of a directory in os module 
import os

# Get the current directory
current_directory = os.getcwd()

# Print the current directory path
print(f"Contents of: {current_directory}")

# List and print all files/folders in the current directory
for item in os.listdir(current_directory):
    print(item)
