#beginning of week 14 lecture 1
#unit 1

#beginner

#intermediate

#advanced

#unit 2

#beginner

#intermediate

#advanced

#beginning of week 14 lecture 2
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
student_name = "Jason"
exam1= 94
exam2 = 90
exam3 = 88

#unit 2
#beginner
def final_grade(grade, bonus):
    """Add bonus to grade for final grade"""
    