from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flag_fall = 4.50  # class variable for flag_fall

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Calculate and return the fare for the taxi trip."""
        return super().get_fare() + self.flag_fall

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi."""
        return f"{super().__str__()} plus flag_fall of ${self.flag_fall:.2f}"
