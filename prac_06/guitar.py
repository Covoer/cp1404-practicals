class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        # Assuming the current year as 2022. In real-world applications,
        # you'd fetch the current year dynamically.
        current_year = 2022
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50


# Example usage:
guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(guitar)  # Output: Gibson L-5 CES (1922) : $16,035.40
print(guitar.get_age())  # Output: 100
print(guitar.is_vintage())  # Output: True






