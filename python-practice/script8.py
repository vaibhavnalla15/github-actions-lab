import os
import sys

env = os.getenv("APP_ENV")
api_key = os.getenv("API_KEY")

if env != "production":
    print("Invalid env")
    sys.exit(1)

if not os.path.exists("README.md"): # Check for README.md
    print("Missing README.md")
    sys.exit(1)

if not api_key:
    print("Missing API key")
    sys.exit(1)

print("All checks passed")