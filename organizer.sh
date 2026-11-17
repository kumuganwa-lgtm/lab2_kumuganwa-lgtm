#!/bin/bash

# organizer.sh - archives grades.csv with a timestamp and logs what happened.

# 1. Stop with a clear message if grades.csv is missing
if [ ! -f grades.csv ]; then
    echo "Error: grades.csv was not found in this folder."
    echo "Run this script from the folder that contains grades.csv."
    exit 1
fi

# 2. Create the archive folder if it doesn't exist
if [ ! -d archive ]; then
    mkdir archive
fi

# 3. Make a timestamp like 20251105-170000
timestamp=$(date +%Y%m%d-%H%M%S)
new_name="grades_$timestamp.csv"

# 4. Move grades.csv into archive/ with the new name
mv grades.csv "archive/$new_name"

# 5. Create a new, empty grades.csv ready for the next batch
touch grades.csv

# 6. Add a line to the log (>> adds to the end instead of overwriting)
echo "$timestamp: grades.csv -> archive/$new_name" >> organizer.log

echo "Archived grades.csv as archive/$new_name"
