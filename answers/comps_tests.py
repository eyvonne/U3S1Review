from comps import *
from sales import *
import unittest


class ComputerTests(unittest.TestCase):
    '''The setUp method is built in to unittest and is automatically run before
    each test'''

    def setUp(self):
        '''Create two objects to run tests on'''
        self.comp = Computer(1, 3.4, 512, 'HDD')
        self.laptop = Laptop(4, 3.2, 1024, 3)
    ''' The tearDown method is another built in from unittest and automatically runs
    after each test. This ensures that you run your tests on a unique object each time'''

    def tearDown(self):
        self.comp = None
        self.laptop = None

    def test_computer_boot(self):
        '''tests the boot speed of the computer and laptop'''
        self.assertEqual(self.comp.__bootTime__(), 'time to go make a cup of coffee')
        self.assertEqual(self.laptop.__bootTime__(), 'about 10 seconds')

    def test_computer_stats(self):
        '''tests that the stats are saved to the computer'''
        self.assertEqual(self.comp.ram, 1)
        self.assertEqual(self.comp.cpu, 3.4)
        self.assertEqual(self.laptop.storage, 1024)
        self.assertEqual(self.laptop.on, False)
        self.assertEqual(self.laptop.open, False)

    def test_turn_on_laptop(self):
        '''this test opens and turns on the laptop and tests that it worked'''
        self.laptop.openShell()
        self.laptop.turnOn()
        self.assertEqual(self.laptop.open, True)
        self.assertEqual(self.laptop.on, True)


class SalesTests(unittest.TestCase):
    def setUp(self):
        self.inventory = generate_computers()
        self.desks = [i for i in self.inventory if type(i) == Computer]
        self.laps = [i for i in self.inventory if type(i) == Laptop]

    def tearDown(self):
        self.inventory = None

    def test_number_computers(self):
        '''tests that the appropriate number of computers are generated'''
        self.assertTrue(6 <= len(self.inventory) <= 10)

        self.assertTrue(3 <= len(self.desks) <= 5)
        self.assertTrue(3 <= len(self.laps) <= 5)

    def test_lap_stats(self):
        for lap in self.laps:
            self.assertTrue(4 <= lap.ram <= 12)
            self.assertTrue(256 <= lap.storage <= 1024)
            self.assertEqual(lap.storageType, 'SSD')
            self.assertTrue(1 <= lap.cpu <= 3)
            self.assertTrue(type(lap.cpu) == float)
            self.assertTrue(5 <= lap.weight <= 15)

    def test_comp_stats(self):
        for comp in self.desks:
            self.assertTrue(8 <= comp.ram <= 24)
            self.assertTrue(512 <= comp.storage <= 2048)
            self.assertIn(comp.storageType, ['SSD', 'HDD'])
            self.assertTrue(2 <= comp.cpu <= 5)
            self.assertTrue(type(comp.cpu) == float)


if __name__ == '__main__':
    unittest.main()
