import os
import sys

# Define the relative path to the file
file_path ="/README.md"

# Check if the file exists 
if os.path.exists(file_path):
    print(f"Success: {file_path} is present.")
else:
    print(f"Error: {file_path} not found.")
    sys.exit(1)