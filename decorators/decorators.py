# Import necessary libraries
import time
import sys

# Decorator function to calculate execution time of another function
def timed(function):
    def wrapper(arg):
        # Record the starting time
        startTime = time.time()
        # Execute the function with the provided argument
        value = function(arg)
        # Record the stopping time after the function execution
        stopTime = time.time()
        # Get the name of the function being timed
        functionName = function.__name__
        # Print the execution time of the function
        print(f"{functionName} took {stopTime - startTime} seconds to execute.")
        return value  # Return the value returned by the original function
    return wrapper  # Return the wrapper function

# Decorated function to calculate factorial
@timed
def calculateFactorial(x):
    result = 1
    # Calculate factorial for the given number
    for i in range(1, x+1):
        result *= i
    return result

# Function to prompt user for printing large factorials
def getChoice(arg):
    choice = input(
        f"The value {arg} factorial is very large. Do you want to print it to the screen (Y,N)? ")
    return choice

# Main function to orchestrate factorial calculation and user interaction
def main(arg):
    # Calculate the factorial of the provided argument
    factorial = calculateFactorial(arg)
    
    # Check if the factorial is larger than 10^100
    if factorial > 10**100:
        # Ask the user whether to print the large factorial
        choice = getChoice(arg)
        
        # Validate user input
        while choice.upper() not in ['Y', 'N']:
            print(f"You entered an incorrect choice: {choice}")
            choice = getChoice()
        
        # Act based on user choice
        if choice.upper() == 'Y':
            print(f"{arg}! = {factorial:,}")  # Print the large factorial
        else:
            print("Goodbye")  # Exit message if user chooses not to print
    else:
        # Print the factorial directly if it's smaller than 10^100
        print(f"{arg}! = {factorial:,}")

# Entry point of the script
if __name__ == "__main__":
    # Get the command line argument and pass it to the main function after converting to an integer
    main(int(sys.argv[1]))
