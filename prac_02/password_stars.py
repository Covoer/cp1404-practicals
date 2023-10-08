"""Define main function"""
def main():
    """Set the minimum password length"""
    min_length = 10

    while True:
        """Ask the user for a password"""
        password = get_password()

        "Check if the password meets the minimum length requirement"
        if len(password) < min_length:
            print(f"Password is too short. It must be at least {min_length} characters long.")
        else:
            print_asterisks(password)
            break


def print_asterisks(password):
    """Print asterisks based on password length"""
    print("*" * len(password))


def get_password():
    password = input("Enter a password: ")
    return password


main()