import sys

num = -2 

if num < 0:
    print("Negative numer detected")
    sys.exit(1)  # ❌ FAIL CI
else:
    print("All Good")
