def get_student_score():
    """
    Prompts the user to enter a valid score (0-100) and returns it as a float.

    Returns:
        float: The student's validated score.
    """
    while True:
        try:
            student_score = float(input("Enter your score: "))
            if 0 <= student_score <= 100:
                return student_score
            print("Error: Score must be between 0 and 100.")
        except ValueError:
            print("Error: Please enter a valid number.")

def calculate_grade(student_score):
    """
    Determines the letter grade based on the given score.

    Args:
        student_score (float): The student's score.

    Returns:
        str: The corresponding letter grade ('A', 'B', 'C', 'D', or 'F').
    """
    if student_score >= 90:
        return "A"
    if student_score >= 80:
        return "B"
    if student_score >= 70:
        return "C"
    if student_score >= 60:
        return "D"
    return "F"  # No need for else

# Main execution flow
if __name__ == "__main__":
    final_score = get_student_score()
    final_grade = calculate_grade(final_score)
    print(f"Your Grade is: {final_grade}")
