# lab2_kumuganwa-lgtm

This project has two programs:

- `grade-evaluator.py` reads a CSV of grades, checks it, and prints the final grade, GPA, pass/fail status, and which assignment(s) can be resubmitted.
- `organizer.sh` archives the current `grades.csv` with a timestamp and logs it.

## Files

| File | Purpose |
|---|---|
| `grades.csv` | Assignment data (columns: assignment, group, score, weight) |
| `grade-evaluator.py` | Python grade calculator |
| `organizer.sh` | Bash archiving script |
| `organizer.log` | Created by `organizer.sh`; one line per archive |
| `archive/` | Created by `organizer.sh`; holds old CSV files |

## Requirements

- Python 3 (no external libraries needed)
- Bash (Linux, macOS, or Git Bash/WSL on Windows)

## 1. Running the grade evaluator

```bash
python grade-evaluator.py
```

(Use `python3` instead of `python` if that is what your system uses.)

The program asks for a file name. Type the name and press Enter:

```
Enter the name of the CSV file to process (e.g., grades.csv): grades.csv
```

### CSV format

The file must have this header and one row per assignment:

```
assignment,group,score,weight
Quiz,Formative,85,20
Group Exercise,Formative,40,20
Functions and Debugging Lab,Formative,45,20
Midterm Project - Simple Calculator,Summative,70,20
Final Project - Text-Based Game,Summative,60,20
```

Rules the program checks:

- Every score must be between 0 and 100.
- All weights must add up to 100, Formative weights to 60, and Summative weights to 40.
- The group must be written exactly as `Formative` or `Summative`.

### Example output

```
Formative: 56.67%
Summative: 65.00%
Total grade: 60.00%
GPA: 3.00
Final status: PASSED

Assignment(s) eligible for resubmission:
 - Group Exercise (score: 40, weight: 20)
 - Functions and Debugging Lab (score: 45, weight: 20)
```

To pass, a student needs at least 50% in both Formative and Summative. Resubmission is offered only for failed Formative assignments (below 50) that have the highest weight; if several tie, all are listed.

### Error messages

| Problem | Message |
|---|---|
| File name does not exist | `Error: The file 'x.csv' was not found.` |
| Score outside 0-100 | `Error: 'Quiz' has a score of 105. Scores must be between 0 and 100.` |
| Weights wrong | `Error: Total weight is 90, but it must be 100.` |

## 2. Running the organizer

```bash
bash organizer.sh
```

This will:

1. Create the `archive/` folder if it does not exist.
2. Move `grades.csv` into `archive/` as `grades_<timestamp>.csv` (for example `grades_20251105-170000.csv`).
3. Create a new empty `grades.csv`.
4. Add a line to `organizer.log` with the timestamp and the old and new file names.

Run it from the folder that contains `grades.csv`. If the file is missing, the script prints an error and stops.

**Note:** Because the script moves `grades.csv`, keep a copy of your data first (for example `cp grades.csv grades_backup.csv`). To run the evaluator on an archived file, type its path when prompted, such as `archive/grades_20251105-170000.csv`.
