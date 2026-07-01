# Part 1 - Collect Student Information

student_id = "STD-2026-001"

student_name = input("Enter Student Name: ")
father_name = input("Enter Father's Name: ")
age = int(input("Enter Age: "))
gender = input("Enter Gender: ")
city = input("Enter City: ")

matric_marks = float(input("Enter Matric Marks (Out of 1100): "))
fsc_marks = float(input("Enter FSc Marks (Out of 1100): "))

# Part 2 - Calculate Percentages

matric_percentage = (matric_marks / 1100) * 100
fsc_percentage = (fsc_marks / 1100) * 100
average_percentage = (matric_percentage + fsc_percentage) / 2

# Part 3 - Scholarship Eligibility

if (average_percentage >= 70):
    scholarship_status = "Eligible for Scholarship"
else:
    scholarship_status = "Not Eligible"

# Bonus Challenge

student_name_upper = student_name.upper()
name_length = len(student_name)

# Part 4 - Display Student Profile

print("         STUDENT PROFILE")

print(f"Student ID           : {student_id}")
print(f"Student Name         : {student_name_upper}")
print(f"Father's Name        : {father_name}")
print(f"Age                  : {age} Years")
print(f"Gender               : {gender}")
print(f"City                 : {city}")

print(f"Matric Marks         : {matric_marks:.0f} / 1100")
print(f"FSc Marks            : {fsc_marks:.0f} / 1100")

print(f"Matric Percentage    : {matric_percentage:.2f}%")
print(f"FSc Percentage       : {fsc_percentage:.2f}%")
print(f"Average Percentage   : {average_percentage:.2f}%")

print(f"Scholarship Status   : {scholarship_status}")

print(f"Length of Name       : {name_length}")