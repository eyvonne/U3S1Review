# U3S1Review
This review was produced to help students in the Lambda School Data Science program learn Object Oriented Programming.

# Instructions

In this review you are taking the roll of an inventory manager for a computer shop. All code should be done in .py files to best represent how you will turn in your work on the Sprint Challenge. This review is designed based on the Challenge, but does not give as much detail in the instructions.  This folder includes comps.py with the classes described already completed and comps_test.py with the unit tests to check your work. If you just copy the code out of those files it will defeat the purpose of the review.

## Part 1: Set Up the Data Structure

```
Some context about computer hardware is required to complete this review, this is
intentionally very simplified you do not need to implement these ranges in any way:

Computers have three basic pieces of hardware: Ram, CPU, and Storage

The ram is measured in gb, and for sake of this exercise you can think of them in the
range 8-24gb. More ram means more things you can do at once with your computer

The CPU or processor is measured in terms of it's clock speed, it generally falls
somewhere in the range of 1-5gHz. Faster clock speeds means faster overall
performance. In the real world there is also a count of cores which affects how much
you can do at once, but for this exercise you can assume everything only has one
core. You could model a more sophisticated computer as a stretch goal


The Storage has two features, the volume and type. The volume is typically measured in
gb, and can be anything from 256 - 1024gb. The type is either a hard drive (HDD) or
solid state drive (SSD) and affects how fast the computer can retrieve information
from it. SSDs are much faster than HDDs For the sake of this exercise the only
thing that it will affect is the startup speed.
```

While working in inventory management you've decided to use some object oriented programming. All the computers you sell have the same basic properties:
- amount of ram
- processor speed
- storage volume
- storage type
- whether or not the computer is on (All computers in your shop are off at purchase)

Write a python class that takes in these values and saves them inside of the object.

Add code to the end of your .py file to run it as a script and test that your attributes are correctly being saved.

## Part 2: Lets Get Computing

Computers stats are nice, but we really want to be able to turn them on to do anything. Add two methods in the class you created in part 1:
- checks the type of storage and if its an SSD returns 'about 10 seconds' or 'time to go get coffee' otherwise. Stretch: raise a ValueError if the drive isn't a legal type (SSD or HDD)
- Turns on the computer: Checks to see if the computer is turned on, and if it isn't calls the function above to estimate how long until its read to go (and sets the computer to on)

Adapt your scripting code to check that the new methods also work

## Part 3: But what about the laptops?

Laptops are their own beast! They are similar to base computers but with some additional attributes.

Create a subclass of the Computer you already made and add:
- weight
- make the default type of storage SSD
- add an attribute for whether or not the lid is open- all of your laptops start closed.

Additionally, you're going to need some changes to the methods:
- now you'll need to check that the lid is open before you turn on the computer (overwrite your method from the base Computer)
- create a method to open the lid

Stretch: add a *property* which determines the portability based on the weight of the laptop. Should return 'very portable', 'a little portable', and 'not really portable'. Use your judgement to choose what weight thresholds to use for these categories.


Again, adapt your script to check the new class and methods.

## General Stretch
There are lots of functions that a computer can do, add additional methods that make sense for a computer. Some ideas include:
- turn off
- run a game
- close laptop

## Part 4: Sell Some Computers!
It's time to open the store with your newly renovated inventory system! To start, create a new file called sales.py, and in it create a function called generate_computers.


This function should generate 3-5 computers and 3-5 laptops. All of the specs should comply with the ranges given in context above. These 6-10 machines should be returned in a list.
The Computers should have the specs:
- ram: 8-24gb
- storage: 512-2048gb
- speed: 2.0 - 5.0gHz
- sorage type: HDD or SSD

The Laptops should have these specs:
- ram: 4-12gb
- storage: 256-1024gb
- speed: 1.0-3.0 gHz
- weight: 5-15lbs



Create a second function called sell_computers. This function should take in the list generated by the previous function, and randomly select some subset of it to be 'sold'. The function should then print out a report of the average stats of sold computers and unsold computers.

Note: You may need to google functions from the `random` library to complete this step.


## Part 5: Tests for Days
Now, all that python scripting for tests was great, but in production we need to check programmatically that everything is working correctly. Create a test file and create a few functions for testing.

This is an area where you can really use your imagination, anything you can test about your computer you should. The answers do tests about:
- boot time response is correct
- stats are stored appropriately
- laptops can be turned on and opened

In addition to testing computers and laptops, test the sales functions, make sure to write at least two tests that ensure expected behavior from those functions.

## Part 6: Make it pretty
Hopefully as you've been coding you have been paying attention to the pep8 style guides, however if not now is the time to go back and check them. Throw your code through an automatic checker to make sure that its compliant. Additionally make sure that your code is well documented and easy to read.
