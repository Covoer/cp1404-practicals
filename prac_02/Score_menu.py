"""Function to get a valid score between 0 and 100"""
def get_valid_score():
    while True:
        try:
            score = float(input("Enter a valid score between 0 to 100: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


"""Function to determine the result from the score"""
def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


"""Function to show stars based on the score"""
def show_stars(score):
    if score >= 0 and score <= 100:
        print("*" * int(score))
    else:
        print("Invalid score")


# Main function
def main():
    print("Welcome to the Score Program!")

    while True:
        print("\nMain Menu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Enter your choice: ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = get_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Thank you for using the Score Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


main()