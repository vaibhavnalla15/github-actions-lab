import os
import sys

# Get the directory where script6.py actually lives
script_dir = os.path.dirname(os.path.abspath(__file__))

# README.md is one level up from the script's folder
readme_path = os.path.join(script_dir, "..", "README.md")

if os.path.exists(readme_path):
    print("File exists")
else:
    print("Missing README.md")
    sys.exit(1)