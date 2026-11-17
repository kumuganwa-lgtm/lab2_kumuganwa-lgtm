import csv
import sys
import os

def load_csv_data():
   
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")

    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    assignments = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):

    for item in data:
        if item['score'] < 0 or item['score'] > 100:
            print(f"Error: '{item['assignment']}' has a score of {item['score']:g}.")
            print("Scores must be between 0 and 100.")
            return


    total_weight = 0
    formative_weight = 0
    summative_weight = 0

    for item in data:
        total_weight = total_weight + item['weight']
        if item['group'] == 'Formative':
            formative_weight = formative_weight + item['weight']
        elif item['group'] == 'Summative':
            summative_weight = summative_weight + item['weight']

    if total_weight != 100:
        print(f"Error: Total weight is {total_weight:g}, but it must be 100.")
        return
    if formative_weight != 60:
        print(f"Error: Formative weight is {formative_weight:g}, but it must be 60.")
        return
    if summative_weight != 40:
        print(f"Error: Summative weight is {summative_weight:g}, but it must be 40.")
        return

    
    formative_points = 0
    summative_points = 0

    for item in data:
        points = item['score'] * item['weight'] / 100
        if item['group'] == 'Formative':
            formative_points = formative_points + points
        elif item['group'] == 'Summative':
            summative_points = summative_points + points

    total_grade = formative_points + summative_points
    gpa = (total_grade / 100) * 5.0


    formative_percent = formative_points / formative_weight * 100
    summative_percent = summative_points / summative_weight * 100

    if formative_percent >= 50 and summative_percent >= 50:
        status = "PASSED"
    else:
        status = "FAILED"


    failed_formative = []
    highest_weight = 0

    for item in data:
        if item['group'] == 'Formative' and item['score'] < 50:
            failed_formative.append(item)
            if item['weight'] > highest_weight:
                highest_weight = item['weight']

  
    print(f"Formative: {formative_percent:.2f}%")
    print(f"Summative: {summative_percent:.2f}%")
    print(f"Total grade: {total_grade:.2f}%")
    print(f"GPA: {gpa:.2f}")
    print(f"Final status: {status}")

    if len(failed_formative) == 0:
        print("No failed formative assignments, so no resubmission is needed.")
    else:
        print("\nAssignment(s) eligible for resubmission:")
        for item in failed_formative:
            if item['weight'] == highest_weight:
                print(f" - {item['assignment']} (score: {item['score']:g}, weight: {item['weight']:g})")

if __name__ == "__main__":
   
    course_data = load_csv_data()


    evaluate_grades(course_data)
