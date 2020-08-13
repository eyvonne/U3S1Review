from comps import *
from random import randint, sample, uniform


def generate_computers():
    # generate a random number between three and five for computers and laptops
    comps = randint(3, 5)
    laps = randint(3, 5)
    # the list where we're going to store the computers
    computers = []
    # generate the computers
    for _ in range(comps):
        ram = randint(8, 24)
        storage = randint(512, 2048)
        storageType = sample(['SSD', 'HDD'], k=1)[0]
        speed = uniform(2, 5)
        computers.append(Computer(ram, speed, storage, storageType))
    # generate the laptops
    for _ in range(laps):
        ram = randint(4, 12)
        storage = randint(256, 1024)
        speed = uniform(1, 3)
        weight = uniform(5, 15)
        computers.append(Laptop(ram, speed, storage, weight))
    return computers


def mean(l):
    '''
    Helper function that returns the mean of a list
    '''
    return sum(l)/len(l)


def sell_computers(inventory):
    # "decide" how many comps will sell
    num_sold = randint(0, len(inventory))
    # Pick out that number of comps from inventory
    # I used a set because they are faster for searching, a list would be fine
    sold = set(sample(inventory, k=num_sold))
    # a quick list comprehension to pull out all the unsold computers
    unsold = [i for i in inventory if i not in sold]
    # Get the details of the computers and store them in a dict for ease of use later
    sold_details = {'ram': [i.ram for i in sold],
                    'cpu': [i.cpu for i in sold],
                    'storage': [i.storage for i in sold],
                    'SSDs': len([i.storageType for i in sold if i.storageType == 'SSD'])}
    unsold_details = {'ram': [i.ram for i in unsold],
                      'cpu': [i.cpu for i in unsold],
                      'storage': [i.storage for i in unsold],
                      'SSDs': len([i.storageType for i in unsold if i.storageType == 'SSD'])}

    # print out the stats
    print('Sold Computers:')
    print(f"Average Ram {mean(sold_details['ram'])}")
    print(f"Average CPU Speed {mean(sold_details['cpu'])}")
    print(f"Average Storage {mean(sold_details['storage'])}")
    print(f"There were {sold_details['SSDs']} SSDs sold")
    print(f"There were {len(sold) - sold_details['SSDs']} HDDs sold")
    print('------------------')
    print('Unsold Computers:')
    print(f"Average Ram {mean(unsold_details['ram'])}")
    print(f"Average CPU Speed {mean(unsold_details['cpu'])}")
    print(f"Average Storage {mean(unsold_details['storage'])}")
    print(f"There were {unsold_details['SSDs']} SSDs left unsold")
    print(f"There were {len(unsold) - unsold_details['SSDs']} HDDs left unsold")


# if you have gotten this far and need a stretch goal go back and make a price
# property on computers that is a factor of their stats, then calculate your
# 'profit'
if __name__ == '__main__':
    sell_computers(generate_computers())
