from silver_service_taxi import SilverServiceTaxi

# Create a SilverServiceTaxi with fanciness of 2
luxury_taxi = SilverServiceTaxi("Hummer", 200, 2)

# Drive the taxi 18 km
luxury_taxi.drive(18)

# Print the taxi's details and fare
print(luxury_taxi)
print(f"Total fare: ${luxury_taxi.get_fare():.2f}")
