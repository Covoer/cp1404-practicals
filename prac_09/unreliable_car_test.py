from unreliable_car import UnreliableCar

# Creating an UnreliableCar instance
my_unreliable_car = UnreliableCar("Old Clunker", 100, 50)  # 50% reliability

# Attempt to drive the car multiple times
for _ in range(5):
    distance_driven = my_unreliable_car.drive(30)  # Trying to drive 30 km each time
    print(f"Attempted to drive 30km, drove {distance_driven}km. Fuel left: {my_unreliable_car.fuel}.")