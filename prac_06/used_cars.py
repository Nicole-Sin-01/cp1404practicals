"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car

def main():
    """Demo test code to show how to use Car class."""
    my_car = Car("My Car", 50)
    my_car.drive(30)
    print(my_car)

    limo = Car("Limo", 100)  # Create a new Car object called "limo"
    limo.add_fuel(20)  # Add 20 more units of fuel
    print(f"Limo fuel: {limo.fuel}")

    limo.drive(115)  # Attempt to drive 115 km
    print(limo)

if __name__ == "__main__":
    main()
