# Lab 1 – Grade Evaluator

The Grade Evaluator project consists of two parts:

---

## Part 1: Python Script – `grade-evaluator.py`

This script reads assignment records from a CSV file and calculates the student's academic performance.

The script performs the following tasks:

- Validates that all assignment scores are between **0 and 100**
- Verifies that assignment weights total **100%**
- Ensures **Formative** assignments total **60%**
- Ensures **Summative** assignments total **40%**
- Calculates the weighted Final Grade
- Calculates the GPA using:

```text
GPA = (Final Grade / 100) × 5.0
```

- Determines whether the student has **PASSED** or **FAILED**
- Identifies the failed formative assignment(s) with the highest weight for resubmission
- Handles missing or empty CSV files 

---

## Part 2: Shell Script – `organizer.sh`

This script automates the archiving of the course data.

It performs the following tasks:

- Creates an `archive/` folder if it does not already exist
- Renames `grades.csv` using the current date and time
- Moves the renamed file into the `archive/` folder
- Creates a new empty `grades.csv` ready for the next batch of grades
- Records every archive operation in `organizer.log`

---

## How to Run

### Python Script

Run the Python application:

```bash
python3 grade-evaluator.py
```

When prompted, enter:

```text
grades.csv
```

The program will display:

- Formative score
- Summative score
- Final Grade
- GPA
- Pass/Fail status
- Resubmission options (if applicable)

---

### Shell Script

Make the script executable:

```bash
chmod +x organizer.sh
```

Run the script:

```bash
./organizer.sh
```

The script will:

- Archive the current `grades.csv`
- Create a new empty `grades.csv`
- Record the archive details in `organizer.log`