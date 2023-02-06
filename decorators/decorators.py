import time
import sys


def timed(function):
    def wrapper(arg):
        startTime = time.time()
        value = function(arg)
        stopTime = time.time()
        functionName = function.__name__
        print(f"{functionName} took {stopTime - startTime} seconds to execute.")
        return value
    return wrapper


@timed
def calculateFactorial(x):
    result = 1
    for i in range(1, x+1):
        #print(f"{result} * {i} = ", end=" ")
        result *= i
        # print(result)
    return result


def getChoice():
    choice = input(
        "The value of factorial is very large do you want to print to screen (Y,N)? ")
    return choice


def main(arg):
    factorial = calculateFactorial(arg)
    if factorial > 10**100:
        choice = getChoice()
        while choice.upper() not in ['Y', 'N']:
            print(f"You entered an incorrect choice {choice}")
            choice = getChoice()
        if choice.upper() == 'Y':
            print(f"{arg}! = {factorial: ,}")
        else:
            print("Goodbye")
    else:
        print(f"{arg}! = {factorial: ,}")


if __name__ == "__main__":
    main(int(sys.argv[1]))