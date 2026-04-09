import os
import sys

api_key = os.getenv("API_KEY")

if not api_key:
    print("API key missing")
    sys.exit(1)

print("API key found")