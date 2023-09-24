def main():
    """Get score from user"""
    score = float(input("Enter score: "))
    """Get and print result"""
    result = get_result(score)
    print(result)
"""Function to conpare result"""
def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"
main()