"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject_details(data)


def get_data():
    """Read data from a file and return it as a list of lists."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        data.append(parts)
    input_file.close()
    return data


def display_subject_details(data):
    """Display subject details based on the collected data."""
    for subject_data in data:
        subject, lecturer, num_students = subject_data
        print(f"{subject} is taught by {lecturer} and has {num_students} students")

main()