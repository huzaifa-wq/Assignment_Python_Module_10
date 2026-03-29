import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):
        self.distance_traveled += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:

            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"\nRace status: {self.name}")
        print(f"{'Car':<15}{'Speed':<10}{'Distance':<10}")
        print("-" * 35)
        for car in self.cars:
            print(f"{car.registration_number:<15}{car.current_speed:<10}{car.distance_traveled:<10}")
        print("-" * 35)

    def race_finished(self):
        return any(car.distance_traveled >= self.distance for car in self.cars)



if __name__ == "__main__":

    cars = [Car(f"Car-{i+1}", random.randint(100, 200)) for i in range(10)]


    race = Race("Grand Demolition Derby", 8000, cars)

    hours = 0
    while not race.race_finished():
        race.hour_passes()
        hours += 1
        if hours % 10 == 0:
            race.print_status()


    print("\n*** Race Finished! ***")
    race.print_status()