def extract_name_from_email(email):
    """
    Extract a name from the email. Assumes the name is the part before "@" and
    separates parts of the name using ".".
    """
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = ' '.join(parts).title()
    return name


def main():
    """
    Program to store and display user emails and names.
    """
    email_to_name = {}
    email = input("Email: ")

    while email != "":
        # Extract a potential name from the email
        proposed_name = extract_name_from_email(email)

        # Check if the extracted name is correct
        confirmation = input(f"Is your name {proposed_name}? (Y/n) ").lower()
        if confirmation == 'n' or confirmation == 'no':
            correct_name = input("Name: ")
            email_to_name[email] = correct_name
        else:
            email_to_name[email] = proposed_name

        email = input("Email: ")

    # Display the stored emails and names
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
