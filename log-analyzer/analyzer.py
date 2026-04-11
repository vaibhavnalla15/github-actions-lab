import sys  
from pathlib import Path

LOG_FILE = "logs/app.log"
REPORT_FILE = "./report.txt"

def analyze_logs():
    error_count = 0
    warning_count = 0
    info_count = 0

    if not Path(LOG_FILE).exists():
        print("Log file missing")
        sys.exit(1)
    
    with open(LOG_FILE) as f:
        for line in f:
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1
            elif "INFO" in line:
                info_count += 1

    return error_count, warning_count, info_count

def generate_report(errors, warnings, infos):
    with open(REPORT_FILE, "w") as f:
        f.write(f"Error: {errors}\n")
        f.write(f"Warning: {warnings}\n")
        f.write(f"Info: {infos}\n")

def main(): 
    errors, warnings, infos = analyze_logs()

    print(f"Errors: {errors}")
    print(f"Warnings: {warnings}")  
    print(f"Infos: {infos}")

    generate_report(errors, warnings, infos)    

    # FAIL CONDITION
    if errors > 1:
        print("Too many erros! Failing CI...")
        sys.exit(1)

if __name__ == "__main__":
    main()  