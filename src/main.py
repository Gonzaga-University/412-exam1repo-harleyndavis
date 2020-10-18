#!/usr/bin/env python3

import sys

class Adder():
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def getSum(self):
        return self.val1 + self.val2

class Divider():
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def getQuotient(self):
        return self.val1 / self.val2

class Average():
    def __init__(self, values):
        self.values = values

    def getAverage(self):
        return sum(self.values) / len(self.values)

if __name__ == "__main__":
    print("Starting program")

    adder = Adder(10, 20)
    print(adder.getSum())
    divider = Divider(20, 2)
    print(divider.getQuotient())

    average = Average([1,2,3,4,5,6,7,8,9])
    print(average.getAverage())

    print("Done with program")
