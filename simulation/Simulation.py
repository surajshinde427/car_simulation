class Simulation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cars = {}

    def add_car(self, car):
        self.cars[car.name] = car

    def run(self):
        max_steps = max(len(car.commands) for car in self.cars.values())
        results = {}
        collisions = {}

        for step in range(max_steps):
            positions_before = {}
            for car in self.cars.values():
                if car.active:
                    positions_before[car.name] = car.current_position()

            for car in self.cars.values():
                if not car.active:
                    continue

                command = car.next_command()
                if command == 'L':
                    car.turn_left()
                elif command == 'R':
                    car.turn_right()
                elif command == 'F':
                    car.move_forward(self.width, self.height)

            positions_after = {}
            for car in self.cars.values():
                if car.active:
                    positions_after[car.name] = car.current_position()

            position_to_cars = {}
            for car_name, pos in positions_after.items():
                if pos not in position_to_cars:
                    position_to_cars[pos] = []
                position_to_cars[pos].append(car_name)

            for pos, cars_at_pos in position_to_cars.items():
                if len(cars_at_pos) > 1:
                    for car_name in cars_at_pos:
                        self.cars[car_name].active = False
                        collisions[car_name] = (cars_at_pos, pos, step + 1)

        for car_name, car in self.cars.items():
            if car_name in collisions:
                collided_with = []
                for c in collisions[car_name][0]:
                    if c != car_name:
                        collided_with.append(c)
                pos = collisions[car_name][1]
                step_num = collisions[car_name][2]
                results[car_name] = f"- {car_name}, collides with {', '.join(collided_with)} at {pos} at step {step_num}"
            else:
                results[car_name] = f"- {car_name}, ({car.x},{car.y}) {car.direction}"

        return results
