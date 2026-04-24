def get_scores(num_tests):
 """Get test scores from user"""
 scores = []
 for i in range(num_tests):
    score = int(input(f"Test {i+1}: "))
    scores.append(score)
    return scores

def calculate_average(scores):
 """Calculate average of scores"""
 return sum(scores) / len(scores)

