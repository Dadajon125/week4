
def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3
def drop_lowest(score1, score2, score3):
    lowest = min(score1, score2, score3)
    total = (score1 + score2 + score3 - lowest)
    return total / 2
def calculate_weighted(assignments, midterm, final):
    return (0.30 * assignments) + (0.30 * midterm) + (0.40 * final)
def determine_grade(average):
    if "score" >= 90:
        grade = 'A'
    elif "score" >= 80:
        grade = 'B'
    elif "score" >= 70:
        grade = 'C'
    elif "score" >= 60:
        grade = 'E'
    else: 
        return "F"
    def needs_improvement (current_avg, target_grade):
        if target_grade =='A':
           return current_avg < 90
        elif target_grade == 'B':
            return current_avg < 80
        elif target_grade == 'C':
            return current_avg < 70
        elif target_grade == 'D':
            return current_avg < 60
        
    def grade_calculator():
        score1 = int(input("Enter the 1st Assignment score"))
        score2 = int(input("Enter the 2nd Assignment score"))
        score3 = int(input("Enter the 3rd Assignment score"))
        midterm_score = int(input("Enter the midterm score"))
        final_score = int (input("Enter the final score"))
        avg_assignment_score = calculate_average(score1, score2, score3)
        avg_with_lowest_dropped = drop_lowest(score1, score2, score3)
        better_avg = max(avg_assignment_score, avg_with_lowest_dropped)

        avg_wieghted = calculate_weighted(better_avg, midterm_score, final_score)
        grade = determine_grade(avg_wieghted)

        improvement_for_a = needs_improvement(avg_wieghted,'A')







