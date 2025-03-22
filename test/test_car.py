import unittest
from simulation.Car import Car
from simulation.Simulation import Simulation

class TestCar(unittest.TestCase):
    def test_turn_left(self):
        car = Car('A', 0, 0, 'N', '')
        car.turn_left()
        self.assertEqual(car.direction, 'W')
        car.turn_left()
        self.assertEqual(car.direction, 'S')

    def test_turn_right(self):
        car = Car('A', 0, 0, 'N', '')
        car.turn_right()
        self.assertEqual(car.direction, 'E')
        car.turn_right()
        self.assertEqual(car.direction, 'S')

    def test_mv_forward_within_bounds(self):
        car = Car('A', 0, 0, 'N', '')
        car.move_forward(5, 5)
        self.assertEqual(car.current_position(), (0, 1))

    def test_mv_forward_out_of_bounds(self):
        car = Car('A', 0, 0, 'S', '')
        car.move_forward(5, 5)
        self.assertEqual(car.current_position(), (0, 0))

    def test_next_command(self):
        car = Car('A', 0, 0, 'N', 'FLR')
        self.assertEqual(car.next_command(), 'F')
        self.assertEqual(car.next_command(), 'L')
        self.assertEqual(car.next_command(), 'R')
        self.assertIsNone(car.next_command())

class TestSimulation(unittest.TestCase):
    def test_single_car_no_collision(self):
        sim = Simulation(5, 5)
        car = Car('A', 0, 0, 'N', 'FFRFF')
        sim.add_car(car)
        results = sim.run()
        self.assertIn('- A, (2,2) E', results['A'])

    def test_two_cars_no_collision(self):
        sim = Simulation(5, 5)
        car1 = Car('A', 0, 0, 'N', 'FF')
        car2 = Car('B', 1, 0, 'N', 'FF')
        sim.add_car(car1)
        sim.add_car(car2)
        results = sim.run()
        self.assertIn('- A, (0,2) N', results['A'])
        self.assertIn('- B, (1,2) N', results['B'])

    def test_collision(self):
        sim = Simulation(5, 5)
        car1 = Car('A', 0, 0, 'E', 'F')
        car2 = Car('B', 1, 0, 'W', 'F')
        sim.add_car(car1)
        sim.add_car(car2)
        results = sim.run()
        self.assertIn('collides', results['A'])
        self.assertIn('collides', results['B'])

    def test_cross_path_collision(self):
        sim = Simulation(5, 5)
        car1 = Car('A', 0, 0, 'N', 'FRF')
        car2 = Car('B', 2, 1, 'W', 'FLF')
        sim.add_car(car1)
        sim.add_car(car2)
        results = sim.run()
        for result in results.values():
            print(result)

if __name__ == '__main__':
    unittest.main()
