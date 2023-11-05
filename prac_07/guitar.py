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


def read_guitars(filename):
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:  # Ensure there are enough parts
                name, year, cost = parts
                guitars.append(Guitar(name, int(year), float(cost)))  # Convert year and cost to the correct types
    return guitars


def save_guitars(filename, guitars):
    with open(filename, 'w', newline='') as file:
        for guitar in guitars:
            file.write("{},{},{}\n".format(guitar.name, guitar.year, guitar.cost))


def main():
    filename = 'guitars.csv'
    guitars = read_guitars(filename)

    # Display the unsorted list of guitars
    print("These are my guitars:")
    for guitar in guitars:
        print(guitar)

    # Sort and display the guitars by year
    guitars.sort()
    print("\nGuitars sorted by year:")
    for guitar in guitars:
        print(guitar)

    # Add new guitars
    add_more = input("Do you want to add more guitars? (Y/n) ").lower()
    while add_more != 'n':
        name = input("Name: ")
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        add_more = input("Add another? (Y/n) ").lower()

    # Save guitars to file
    save_guitars(filename, guitars)

    # Verify by reading the file again
    print("\nGuitars saved to file:")
    guitars = read_guitars(filename)
    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    main()
