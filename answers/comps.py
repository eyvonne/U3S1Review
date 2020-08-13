'''Computer classes to review for the Unit 3 Sprint 1 SC'''


class Computer:

    def __init__(self, ram, cpu, storage, storageType, on=False):
        self.ram = ram
        self.cpu = cpu
        self.storage = storage
        self.storageType = storageType.upper()
        self.on = on

    def __bootTime__(self):
        '''returns the approximate boot Time of the computer'''
        if self.storageType == 'SSD':
            return 'about 10 seconds'
        elif self.storageType == 'HDD':
            return 'time to go make a cup of coffee'
        else:
            raise ValueError(f"{self.storageType} is not a recognized drive")

    def turnOn(self):
        if self.on == False:
            print('Powering on now, you have', self.__bootTime__(),
                  'before it turns on')
            self.on = True
        else:
            print('Computer is already turned on')


class Laptop(Computer):
    open = False

    def __init__(self, ram, cpu, storage, weight,
                 storageType='SSD'):
        super().__init__(ram, cpu, storage, storageType)
        self.weight = weight

    def turnOn(self):
        if self.open == False:
            print("you'll need to open the laptop first")
        else:
            super().turnOn()

    def openShell(self):
        if self.open == False:
            print('Opening up the Laptop')
            self.open = True
        else:
            print('your laptop is already open')


if __name__ == '__main__':
    base = Computer(1, 4, 52, 'SSD')
    base.turnOn()
    base = Laptop(1, 1.6, 50, 2)
    base.openShell()
    base.turnOn()
