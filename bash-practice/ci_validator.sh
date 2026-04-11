#!/usr/bin/env bash

# -------------------------------
# CONFIG (EDIT BASED ON PROJECT)
# -------------------------------
REQUIRED_ENV="production"
REQUIRED_FILES=("../README.md" "ci_validator.sh")
REQUIRED_COMMANDS=("python3" "pip")

# -------------------------------
# INIT
# -------------------------------
ERRORS=()

echo "Starting CI Validation..."

# -------------------------------
# CHECK ENVIRONMENT
# -------------------------------
if [ "$APP_ENV" != "$REQUIRED_ENV" ]; then
    echo "[FAIL] APP_ENV is $APP_ENV (expected: $REQUIRED_ENV)"
    ERRORS+=("Invalid Environment")
else
    echo "[PASS] Environment is correct"
fi

# -------------------------------
# CHECK FILES
# -------------------------------
for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$file" ]; then
        echo "[FAIL] Required file not found: $file"
        ERRORS+=("Missing File: $file")
    else
        echo "[PASS] Found required file: $file"
    fi
done

# -------------------------------
# CHECK COMMANDS
# -------------------------------
for cmd in "${REQUIRED_COMMANDS[@]}"; do
    if ! command -v "$cmd" &> /dev/null; then
        echo "[FAIL] Command not found: $cmd"
        ERRORS+=("Missing command: $cmd")
    else
        echo "[PASS] Command available: $cmd"
    fi  
done

# -------------------------------
# CHECK SECRET
# -------------------------------
if [ -z "$API_KEY" ]; then
    echo "[FIAL] API_KEY is Missing"
    ERRORS+=("Missing API_KEY")
else
    echo "[PASS] API_KEY is present"
fi

# -------------------------------
# FINAL RESULT
# -------------------------------
echo "-------------------------------"

if [ ${#ERRORS[@]} -ne 0 ]; then
  echo "❌ Validation Failed"
  printf '%s\n' "${ERRORS[@]}"
  exit 1
else
  echo "✅ All checks passed"
  exit 0
fi