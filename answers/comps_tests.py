from comps import *
import unittest


class ComputerTests(unittest.TestCase):
    '''Create two objects to run tests on'''
    comp = Computer(1, 3.4, 512, 'HDD')
    laptop = Laptop(4, 3.2, 1024, 3)

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


if __name__ == '__main__':
    unittest.main()
