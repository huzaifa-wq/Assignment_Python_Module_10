class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom  # Elevator starts at the bottom floor

    def floor_up(self):
        if self.current < self.top:
            self.current += 1
            print(f"Elevator is now at floor {self.current}")
        else:
            print("Elevator is already at the top floor.")

    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
            print(f"Elevator is now at floor {self.current}")
        else:
            print("Elevator is already at the bottom floor.")

    def go_to_floor(self, target):
        if target < self.bottom or target > self.top:
            print("Invalid floor number.")
            return

        while self.current < target:
            self.floor_up()
        while self.current > target:
            self.floor_down()


if __name__ == "__main__":
    # Create an elevator from floor 1 to floor 10
    h = Elevator(1, 10)


    print("Moving to floor 5:")
    h.go_to_floor(5)


    print("\nReturning to bottom floor:")
    h.go_to_floor(h.bottom)