#beginning of week 14 lecture 1
#unit 1
#beginner
rgb_color = (255, 128, 0)

print(f"Red channel: {rgb_color[0]}")
print(f"Green channel: {rgb_color[1]}")
print(f"Blue channel: {rgb_color[2]}")

palette = []
palette.append((rgb_color[0], rgb_color[1], rgb_color[2]))
print(palette)

#intermediate
#creat student tuples
student_record1 = ("Steve", 88, 25)
student_record2 = ("Derrick", 92, 23)
student_record3 = ("Jason", 79, 22)
#store in classroom list
classroom = []
classroom.append(student_record1)
classroom.append(student_record2)
classroom.append(student_record3)
#print second student name using double subscripting
derrick_name = classroom[1][0]
print(derrick_name)
#unpack first student information
classroom = (student_record1, student_record2, student_record3)
steve, derrick, jason = classroom
#print formatted message
print(f"First student's information: {steve}")

#advanced
#creat original student info tuple
student_info = ("Jason", [94, 90, 88])
final_grade = f"{sum(student_info[1]) / len(student_info[1]):.2f}"
updated_student_info = (student_info[0], student_info[1], final_grade)
#add fourth exam score
updated_student_info[1].append(95)
#calculate new average
final_grade = f"{sum(updated_student_info[1]) / len(updated_student_info[1]):.2f}"
updated_student_info = (updated_student_info[0], updated_student_info[1], final_grade)

print(f"Original student info: {student_info}")
print(f"Updated student info: {updated_student_info}")

#unit 2
#beginner
grades = [88, 92, 79]
date = (2024, 6, 1)
def final_grade(grades, bonus=5):
    """Add bonus to grade for final grade"""
    for grade in grades:
        grade += bonus
    return grade, date
print(final_grade(grades))
#list was used for grades because it is mutable and can be modified, while tuple was used for date because it is immutable and should not be changed.

#intermediate
def find_range():

#advanced

  
#Unit 3
#beginner
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for g in grid:
    print(g, end="\n")
    
for row in grid:
    for value in row:
        print(value, end= ' ')
    print()
print(f"{grid[0]}")
#print whole row with one index
#print specific location with two indexes

#intermediate

#advanced
