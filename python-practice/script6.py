import os
import sys

if not os.path.exists("README.md"):
    print("Missing README.md")
    sys.exit(1)

print("File exists")