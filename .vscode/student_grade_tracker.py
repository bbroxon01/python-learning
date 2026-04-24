"""
Student Grade Tracker
CS 1300 — Lecture 5 Mini-Project
A modular, well-tested program that collects exam scores,
calculates a letter grade and academic standing, and
displays a formatted report.

Functions:
is_valid_score — Helper: validate a single score
get_exam_scores — Collect n exam scores with validation
get_validated_scores — Helper: retry loop for score entry
calculate_average — Compute mean of a scores list
determine_letter_grade — Map average to letter grade
determine_standing — Map average to academic standing
print_divider — Helper: print a decorative line
display_report — Print the formatted grade report
test_grade_tracker — Run all unit tests"""

""" student = get_student_name()
    scores = get_exam_scores()
    average = calculate_average()
    letter_grade = determine_letter_grade()
    standing = determine_standing()"""
"""main()"""

"""get exam scores"""
"""def get_exam_scores():
    exam_score = input("Enter an exam score: ".isdigit)
    if not exam_score == "" or 0 <= exam_score <= 100:
        exam_scores
        return exam_score"""
score = []
def main():
    """Student Grade Tracker Orchestrator"""
    menu()
        #get_student_name()
    get_exam_scores()
    #calculate_average()
    #display_report()
    #test_grade_tracker()
    
def menu():
    print("Welcome!")
    return get_student_name()
    
"""Get student name — Prompt for and return student name"""
def get_student_name():
    return input("Enter your name: ".istitle)
"""Get exam scores"""    
def get_exam_scores():
    return int(input("Enter a score: "))
    get_validated_scores()
    
def get_validated_scores(scores):
    if not is_valid_score():
        scores.remove(score)
        message = print("One score invalid\nDo you want to enter another score")
        if message == "no":
            return scores
        else:
            score
    else:
            if not False:
                return scores
    def is_valid_score():
        scores = []
        if not 0 <= score <= 100:
            return score
        else:
            scores.append(score)
            return scores
#def calculate_average(get_exam_scores, total= (100)):
"""Get scores"""
"""Validate Score/s"""
    #if is_valid_score():
     #   get_exam_scores()
    #percentage = (score / total) * 100
    #return round(percentage, 1)
#def is_valid_score(score):
    #return 0 <= score < 100

# TESTING THE FUNCTION
"""def test_calculate_grade():"""
"""Test the calculate_grade function"""
"""print("Testing calculate_grade():")
    
    # Test 1: Normal case
    result = calculate_grade(85, 100)
    expected = 85.0
    print(f"Test 1 - Normal: ", end="")
    if result == expected:
        print("PASS")
    else:
        print(f"FAIL (got {result}, expected {expected})")

    # Test 2: Perfect score
    result = calculate_grade(100, 100)
    expected = 100.0
    print(f"Test 2 - Perfect: ", end="")
    if result == expected:
        print("PASS")
    else:
        print(f"FAIL (got {result}, expected {expected})")
    
    # Test 3: Zero score
    result = calculate_grade(0, 100)
    expected = 0.0
    print(f"Test 3 - Zero: ", end="")
    if result == expected:
        print("PASS")
    else:
        print("FAIL")

    # Test 4: Different total
    result = calculate_grade(18, 20)
    expected = 90.0
    print(f"Test 4 - Different total: ", end="")
    if result == expected:
        print("PASS")
    else:
        print("FAIL")

    # Test 5: Edge case - division by zero
    result = calculate_grade(50, 0)
    expected = 0
    print(f"Test 5 - Zero total: ", end="")
    if result == expected:
        print("PASS")
    else:
        print("FAIL")

test_calculate_grade()"""

# DEBUGGING EXAMPLE

#def buggy_average(numbers):
#    """Calculate average - HAS A BUG!"""
#    total = sum(numbers)
#    return total / len(numbers) # What if empty list?

#def test_buggy_average():
#    print("\nTesting buggy_average():")
#    try:
#        result = buggy_average([])
#        print(f"Empty list: {result}")
#    except ZeroDivisionError:
#        print("BUG FOUND: Crashes on empty list!")

#    def fixed_average(numbers):
#        if len(numbers) == 0:
#            return 0
#        return sum(numbers) / len(numbers)

#    print(f"Fixed version with empty list: {fixed_average([])}")

#test_buggy_average()
