import csv
import sys
import os


def load_csv_data():
    filename = input(
        "Enter the name of the CSV file to process (e.g., grades.csv): ")

    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    assignments = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
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

    print("\n--- Processing Grades ---")
    # check whether the CSV file contains any assignment data.

    if not data:
        print("Error: The CSV file contains no grade records.")
        sys.exit(1)

    # Check if all scores are percentage based (0-100)
    for row in data:
        assignment_name = row["assignment"]
        score = row["score"]

        if score < 0 or score > 100:
            print(
                f"Error: '{assignment_name}' has an invalid score ({score}). "
                "Scores must be between 0 and 100."
            )
            sys.exit(1)

    # Validate total weights (Total=100, Summative=40, Formative=60)

    # Calculate the total weight for each assignment group
    formative_weight = sum(
        assignment["weight"]
        for assignment in data
        if assignment["group"] == "Formative"
    )

    summative_weight = sum(
        assignment["weight"]
        for assignment in data
        if assignment["group"] == "Summative"
    )

    # Calculate the overall weight
    total_weight = formative_weight + summative_weight

    # Validate that all weights meet the requirements
    if round(total_weight, 2) != 100:
        print(f"Error: Total weight is {total_weight}, but must equal 100.")
        sys.exit(1)

    if round(formative_weight, 2) != 60:
        print(
            f"Error: Formative weight is {formative_weight}, but must equal 60")
        sys.exit(1)

    if round(summative_weight, 2) != 40:
        print(
            f"Error: Summative weight is {summative_weight}, but it must equal 40.")
        sys.exit(1)

    print("All assignment weights are valid.")

    # Calculate the Final Grade and GPA
    formative_points = sum(
        assignment["score"] * assignment["weight"] / 100
        for assignment in data
        if assignment["group"] == "Formative"
    )

    summative_points = sum(
        assignment["score"] * assignment["weight"] / 100
        for assignment in data
        if assignment["group"] == "Summative"
    )

    formative_pct = (formative_points / formative_weight) * 100
    summative_pct = (summative_points / summative_weight) * 100

    total_grade = formative_points + summative_points
    gpa = (total_grade / 100) * 5

    # Determine Pass/Fail status (>= 50% in BOTH categories)
    if formative_pct >= 50 and summative_pct >= 50:
        status = "PASSED"
    else:
        status = "FAILED"

    # Check for failed formative assignments (< 50%)
    # and determine which one(s) have the highest weight for resubmission.

    failed_formative = []
    for assignment in data:
        if (
                assignment["group"] == "Formative" and assignment["score"] < 50):
            failed_formative.append(
                {
                    "assignment": assignment["assignment"],
                    "weight": assignment["weight"]
                }
            )

    resubmission_options = []

    if failed_formative:
        highest_weight = max(
            assignment["weight"]
            for assignment in failed_formative
        )

        for assignment in failed_formative:
            if assignment["weight"] == highest_weight:
                resubmission_options.append(
                    assignment["assignment"]
                )

    # Print the final decision (PASSED / FAILED) and resubmission options
    print("\n========= ALU TRANSCRIPT ===========")

    print(f"Formative Score (60%): "
          f"{formative_points:.2f} points ({formative_pct:.2f}%)")
    print(f"Summative Score (40%): "
          f"{summative_points:.2f} points ({summative_pct:2f}%)")
    print(f"Final Grade: {total_grade:.2f}")
    print(f"GPA: {gpa:.2f}")
    print(f"Status: {status}")

    if status == "FAILED":
        print("\nResubmission Options:")

        if resubmission_options:
            for assignment in resubmission_options:
                print(f"- {assignment}")
        else:
            print("None")


if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()

    # 2. Process the features
    evaluate_grades(course_data)
