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






