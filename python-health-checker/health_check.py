import os
import sys
import json
import requests

def load_config():
    with open("config.json") as f:
        return json.load(f)

def check_env(expected_env):
    actual_env = os.getenv("APP_ENV")
    if actual_env != expected_env:
        print(f"[FAIL] Env mismatch: {actual_env}")
        return False
    print("[PASS] Environment OK")
    return True

def check_files(files):
    all_ok = True
    for file in files:
        if not os.path.exists(file):
            print(f"[FAIL] Missing file: {file}")
            all_ok = False
        else:
            print(f"[PASS] Found file: {file}")
    return all_ok

def check_api(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print("[PASS] API reachable")
            return True
        else:
            print(f"[FAIL] API error: {response.status_code}")
            return False
    except Exception as e:
        print(f"[FAIL] API unreachable: {e}")
        return False

def main():
    config = load_config()

    results = [
        check_env(config["required_env"]),
        check_files(config["required_files"]),
        check_api(config["api_url"])
    ]

    if all(results):
        print("\n✅ All checks passed")
        sys.exit(0)
    else:
        print("\n❌ Health check failed")
        sys.exit(1)

if __name__ == "__main__":
    main()