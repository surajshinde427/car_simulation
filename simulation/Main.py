from Car import Car
from Simulation import Simulation
def get_positive_int_input(prompt):
    while True:
        try:
            value = input(prompt)
            x, y = map(int, value.strip().split())
            if x > 0 and y > 0:
                return x, y
        except ValueError:
            pass

def get_direction_input(prompt):
    while True:
        value = input(prompt).strip().upper()
        if value in ['N', 'S', 'E', 'W']:
            return value

def get_cmd_input(prompt):
    while True:
        value = input(prompt).strip().upper()
        while True:
            value = input(prompt).strip().upper()
            is_valid = True
            for c in value:
                if c not in ['L', 'R', 'F']:
                    is_valid = False
                    break
            if is_valid:
                return value
            else:
                print("Invalid command! Please use only L, R, or F.")

def main():
    while True:
        print("Welcome to Auto Driving Car Simulation!")
        width, height = get_positive_int_input("Please enter the width and height of the simulation field in x y format:\n")
        print(f"You have created a field of {width} x {height}.")

        simulation = Simulation(width, height)

        while True:
            print("Please choose from the following options:")
            print("[1] Add a car to field")
            print("[2] Run simulation")
            choice = input()

            if choice == '1':
                car_name = input("Please enter the name of the car:\n").strip().upper()
                pos_input = input(f"Please enter initial position of car {car_name} in x y Direction format:\n").strip().split()
                if len(pos_input) == 3:
                    x, y = int(pos_input[0]), int(pos_input[1])
                    direction = pos_input[2].upper()
                    if direction in ['N', 'S', 'E', 'W'] and 0 <= x < width and 0 <= y < height:
                        commands = input(f"Please enter the commands for car {car_name}:\n").strip().upper()
                        car = Car(car_name, x, y, direction, commands)
                        simulation.add_car(car)
                        print("Your current list of cars are:")
                        for car in simulation.cars.values():
                            print(f"- {car.name}, ({car.x},{car.y}) {car.direction}, {''.join(car.commands)}")
                    else:
                        continue
                else:
                    continue
            elif choice == '2':
                print("Your current list of cars are:")
                for car in simulation.cars.values():
                    print(f"- {car.name}, ({car.x},{car.y}) {car.direction}, {''.join(car.commands)}")
                print("\nAfter simulation, the result is:")
                results = simulation.run()
                for res in results.values():
                    print(res)

                while True:
                    print("\nPlease choose from the following options:")
                    print("[1] Start over")
                    print("[2] Exit")
                    post_choice = input()
                    if post_choice == '1':
                        break
                    elif post_choice == '2':
                        print("Thank you for running the simulation. Goodbye!")
                        return
                break
if __name__ == "__main__":
    main()