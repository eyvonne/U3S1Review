'''Computer classes to review for the Unit 3 Sprint 1 SC'''


class Computer:

    def __init__(self, ram, cpu, storage, storageType, on=False):
        self.ram = ram
        self.cpu = cpu
        self.storage = storage
        self.storageType = storageType.upper()
        self.on = on

    def __boot_time__(self):
        '''returns the approximate boot Time of the computer'''
        if self.storageType == 'SSD':
            return 'about 10 seconds'
        elif self.storageType == 'HDD':
            return 'time to go make a cup of coffee'
        else:
            raise ValueError(f"{self.storageType} is not a recognized drive")

    def turn_on(self):
        if self.on == False:
            print('Powering on now, you have', self.__boot_time__(),
                  'before it turns on')
            self.on = True
        else:
            print('Computer is already turned on')


class Laptop(Computer):

    def __init__(self, ram, cpu, storage, weight,
                 storageType='SSD', open=False, on=False):
        super().__init__(ram, cpu, storage, storageType, on=on)
        self.weight = weight
        self.open = open

    def turn_on(self):
        if self.open == False:
            print("you'll need to open the laptop first")
        else:
            super().turn_on()

    def open_shell(self):
        if self.open == False:
            print('Opening up the Laptop')
            self.open = True
        else:
            print('your laptop is already open')


if __name__ == '__main__':
    base = Computer(1, 4, 52, 'SSD')
    base.turn_on()
    base = Laptop(1, 1.6, 50, 2)
    base.open_shell()
    base.turn_on()
