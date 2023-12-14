# Complex Lambda Function Example in Python

This Python program showcases the use of a more complex lambda function enclosed within a function. The lambda function is utilized to calculate the square root of a number entered by the user.

## Code Explanation:

The program consists of two functions:

### `square_root_calculator()`
- This function:
  - Prompts the user to input a number.
  - Defines a lambda function `calculate_square_root` that computes the square root using `math.sqrt()`.
  - Computes the square root of the entered number using the lambda function.
  - Returns the calculated square root.

### `main()`
- This function:
  - Acts as the driver function.
  - Calls `square_root_calculator()` to obtain the square root of the user-input number.
  - Displays the resulting square root.

## Usage:

1. **Prompt for Input:**
   - The user is asked to input a number for which the square root needs to be calculated.

2. **Lambda Function Usage:**
   - The lambda function `calculate_square_root` is employed to compute the square root of the entered number.

3. **Display Result:**
   - Finally, the calculated square root is displayed to the user.

## Example Code:

```python
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
