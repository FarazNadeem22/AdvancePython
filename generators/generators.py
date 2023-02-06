# Generators in Python
import sys
import time 


def myGenerator(number):
    for i in range(number):
        yield i**2

def infinite_sequence():
    result = 1
    while True:
        # Yield the result before performing the next operation 
        yield result
        # Perform operation 
        result *= 10

for x in range (0,12):
    values = myGenerator(x) 
    for value in values:
        print(value, end =" ")
    print(" ")
    time.sleep(0.25)

sequence = infinite_sequence()

print(next(sequence), next(sequence), next(sequence), next(sequence))
