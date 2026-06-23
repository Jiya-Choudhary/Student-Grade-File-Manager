# STUDENT GRADE FILE MANAGER
import csv
def calculate_grade(score_string):
    score = float(score_string)

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
with open("students.csv", mode="r") as input_file, open(
    "students_with_grades.csv", mode="w", newline=""
) as output_file:

    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    header = next(reader)
    header.append("Grade")
    writer.writerow(header)

    for row in reader:
        if not row or row[0].strip() == "":
            continue
        score_value = row[1]
        grade = calculate_grade(score_value)
        row.append(grade)
        writer.writerow(row)

print("Grades have been calculated successfully!")
