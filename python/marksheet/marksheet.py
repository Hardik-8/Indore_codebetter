# -------- Student Details --------
university = "AKS University"

name = input("Enter Name : ")
course = input("Enter Course : ")
roll = input("Enter Roll No : ")
branch = input("Enter Branch : ")
fname = input("Enter Father's Name : ")
sem = input("Enter Semester : ")

# -------- Subjects --------
sub1 = "Physics"
sub2 = "Chemistry"
sub3 = "Maths"

# -------- Marks Input --------
P = int(input("Enter Physics Marks : "))
C = int(input("Enter Chemistry Marks : "))
M = int(input("Enter Maths Marks : "))

# -------- Validation --------
if P > 100 or C > 100 or M > 100:
    print("❌ Marks cannot be greater than 100")
    exit()

# -------- Total & Percentage --------
total = P + C + M
percentage = (total / 300) * 100

# -------- Result Logic --------
fail_count = 0
failed_subjects = []

if P < 33:
    fail_count += 1
    failed_subjects.append("Physics")
if C < 33:
    fail_count += 1
    failed_subjects.append("Chemistry")
if M < 33:
    fail_count += 1
    failed_subjects.append("Maths")

if fail_count == 0:
    result = "PASS"
    if percentage >= 60:
        division = "First Division"
    elif percentage >= 45:
        division = "Second Division"
    else:
        division = "Third Division"
else:
    result = "FAIL"
    division = "----"

# -------- Marksheet Print --------
print("\n\t==============================================================")
print("\t\t\t\t", university)
print("\t==============================================================\n")

print("\tName :", name, "\t\tCourse :", course)
print("\tRoll :", roll, "\t\tBranch :", branch)
print("\tFName:", fname, "\t\tSemester:", sem)

print("\n\t--------------------------------------------------------------")
print("\t Subject\tMin Marks\tMarks Obtain\tTotal")
print("\t--------------------------------------------------------------")
print("\t Physics\t33\t\t", P, "\t\t100")
print("\t Chemistry\t33\t\t", C, "\t\t100")
print("\t Maths\t\t33\t\t", M, "\t\t100")
print("\t--------------------------------------------------------------")

print("\t Total Marks :", total, "/300")
print("\t Percentage  :", round(percentage, 2), "%")
print("\t Result      :", result)
print("\t Division    :", division)

if fail_count > 0:
    print("\t Failed In   :", ", ".join(failed_subjects))

print("\n\t Date : 04/02/2026\t\tController of Examination")
print("\t==============================================================")
