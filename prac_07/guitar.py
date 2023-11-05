import csv

filename = 'guitars.csv'


class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def __lt__(self, other):
        """Less than, used for sorting Guitars by year."""
        return self.year < other.year

    def get_age(self):
        current_year = 2023  # Updated to reflect the current year
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50


def load_guitars(filename):
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # skip empty rows
                name, year, cost = row
                guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def print_guitars(guitars):
    for guitar in guitars:
        print(guitar)


# Load guitars from file
guitars = load_guitars(filename)

# Display unsorted guitars
print("Unsorted Guitars:")
print_guitars(guitars)

# Sort guitars by year (oldest to newest)
guitars.sort()

# Display sorted guitars
print("\nSorted Guitars:")
print_guitars(guitars)
# Example usage:
guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(guitar)  # Output: Gibson L-5 CES (1922) : $16,035.40
print(guitar.get_age())  # Output: 100
print(guitar.is_vintage())  # Output: True
