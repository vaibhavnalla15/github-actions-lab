import os
import sys

if os.path.exists("README.md"):
    print("File exists")
else:
    print("Missing README.md")
    sys.exit(1)