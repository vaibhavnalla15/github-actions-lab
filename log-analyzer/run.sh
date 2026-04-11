#!/usr/bin/env bash

echo "🚀 Starting Log Analysis Pipeline..."

# Run Python analyzer
python3 analyzer.py

# Capture exit status
STATUS=$?

echo "📄 Report Output:"
cat report.txt

# Decide based on result
if [ $STATUS -ne 0 ]; then
  echo "❌ Pipeline failed due to high errors"
  exit 1
else
  echo "✅ Pipeline passed"
fi