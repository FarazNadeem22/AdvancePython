import math

def square_root_calculator():
    # Function to calculate square root using a lambda function
    
    # Get user input for the number
    num = float(input("Enter a number to find its square root: "))
    
    # Lambda function to calculate square root
    calculate_square_root = lambda x: math.sqrt(x)
    
    # Calculate square root using the lambda function
    result = calculate_square_root(num)
    
    return result

def main():
    # Driver function to execute the square_root_calculator
    
    # Calculate square root
    result = square_root_calculator()
    
    # Display the result
    print(f"The square root of the entered number is: {result}")

# Call the driver function
if __name__ == "__main__":
    main()
