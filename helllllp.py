name = (input("What is your name? "))
exam_scores = [int(input("Enter your score for Exam 1: ")), int(input("Enter your score for Exam 2: ")), int(input("Enter your score for Exam 3: "))]
average_score = sum(exam_scores) / len(exam_scores)
if average_score >= 90:
    grade = "A"
elif average_score >= 87:
    grade = "A-"
elif average_score >= 83:
    grade = "B+"
elif average_score >= 80:
    grade = "B"
elif average_score >= 77:
    grade = "B-"
elif average_score >= 73:
    grade = "C+"
elif average_score >= 70:
    grade = "C"
elif average_score >= 67:
    grade = "C-"
elif average_score >= 63:
    grade = "D+"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"

if average_score >= 90:
    status = "Dean's List"
elif average_score >= 70:
    status = "Good Standing"
elif average_score >= 60:
    status = "Academic Probation"
else:
    status = "Academic Suspension Warning"
    
width = 30
print("Student Name:", name.capitalize())
print("Exam Scores:", exam_scores, "\n")
print("=" * 30)
print("STUDENT GRADE REPORT".center(width))
print("=" * 30)
print("Student: ",name.capitalize())
print("Exam 1 Score: ", exam_scores[0])
print("Exam 2 Score: ", exam_scores[1])
print("Exam 3 Score: ", exam_scores[2])
print("-" * width)
print("Average: ", f"{average_score:.2f}")
print(("Grade: " + grade))
print("Status: " + status)
print("=" * width)