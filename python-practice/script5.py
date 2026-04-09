import os
import sys

env = os.getenv("APP_ENV")

if env != "production":
    print("Invalid Environment")
    sys.exit(1)
else:
    print("Correct Environment")