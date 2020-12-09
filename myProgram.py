class Vehicle:
    engine_capacity = "1,6 Turbo"

class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    def drive(self):
        print("The vehicle is in driving mode now")

    def stop (self):
        print("The vehicle is in stop mode")

toyota = Vehicle (4, "petrol", 5,150)
print(toyota.number_of_wheels)
print(toyota.type_of_tank)
print(toyota.seating_capacity)
print(toyota.maximum_velocity)

toyota.drive()
toyota.stop()