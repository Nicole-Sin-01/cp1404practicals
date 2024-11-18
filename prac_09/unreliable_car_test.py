"""
CP1404/CP5632 Practical
Testing the UnreliableCar class
"""
from prac_09.unreliable_car import UnreliableCar

def test_unreliable_car():
    # Create two UnreliableCar instances with a reliability of 20% and 80%
    car_80 = UnreliableCar("Pretty reliable", 100, 80)
    car_20 = UnreliableCar("Not reliable", 100, 20)

    # Test driving the car multiple times
    for i in range(1,10):
        # Try driving 100 km and print the results
        print(f"{car_80.name:12} drove {car_80.drive(100):2} km")
        print(f"{car_20.name:12} drove {car_20.drive(100):2} km")

# Run the test
test_unreliable_car()
