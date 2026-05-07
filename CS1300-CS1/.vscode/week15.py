#week15lecure1
#unit 1 
#beginner
test_scores = [78, 92, 85, 88, 75, 95, 82]
scores_higher = sorted(test_scores,reverse=True)
print(scores_higher)
ind = scores_higher.index(88)
print(f"88 is located at index: {ind}")

#intermediate
student_records= [("Emma", 88), ("Liam", 92), ("Olivia", 85), ("Noah", 95), ("Ava", 82)]
#sort alphabetically and by grade
records_by_name = sorted(student_records)
records_by_grade = sorted(student_records, key=lambda s: s[1])
print(records_by_name)
print(records_by_grade)
#find which position "Olivia" in is in name sorted list
record_strings= [x[0] for x in records_by_name]
print(record_strings)
ind_olivia = record_strings.index("Olivia")
print(f"Olivia can be found at index: {ind_olivia}")

#advanced
prices = [10.99, 5.99, 4.49, 2.49, 3.99, 12.49, 7.99, 6.49, 8.99, 9.99]

#unit 3
#beginner

#beginning of week 15 lecture 2
#unit 1

#beginner
import sys

empty = []
small = [1, 2, 3, 4, 5]
large = list(range(100))

print(sys.getsizeof(empty))
print(sys.getsizeof(small))
print(sys.getsizeof(large))
#empty list takes up space because it still has overhead

#intermediate
import sys
list = []
for i in range(20):
    list.append(i)
    if (i + 1) % 5 == 0:
        print(sys.getsizeof(list))
        #print(list)

#advanced

#unit 2 
#beginner



