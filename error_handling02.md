Certainly! Here's an example of Python code that demonstrates raising custom exceptions with an explanation line by line:

```python
# Example 2: Raising Custom Exceptions

class CustomError(Exception):
    # Define a custom exception by inheriting from the base Exception class
    pass

def check_number(value):
    if not isinstance(value, int):
        # Raise a custom exception if the input is not an integer
        raise CustomError("Input must be an integer.")

    if value < 0:
        # Raise a custom exception if the input is negative
        raise CustomError("Input must be a non-negative integer.")

    return value

try:
    user_input = int(input("Enter a non-negative integer: "))
    result = check_number(user_input)
    print("Result:", result)

except CustomError as ce:
    # Handle the custom exception and print the error message
    print(f"Custom Error: {ce}")

except ValueError:
    # Handle the ValueError if the user enters a non-integer value
    print("Error: Please enter a valid integer.")

except Exception as e:
    # Catch any other exceptions that may occur
    print(f"An unexpected error occurred: {e}")

else:
    # Execute if no exception is raised
    print("No errors occurred.")

finally:
    # Always execute, whether an exception occurred or not
    print("This block will always be executed.")
```

Now, let's go through the code:

1. `class CustomError(Exception):`: Defines a custom exception named `CustomError` by inheriting from the base `Exception` class.

2. `def check_number(value):`: Defines a function `check_number` that takes a parameter `value` and raises the custom exception if the conditions are not met.

3. `if not isinstance(value, int):`: Checks if the input is not an integer.

4. `raise CustomError("Input must be an integer.")`: Raises the custom exception with a specific error message.

5. `if value < 0:`: Checks if the input is negative.

6. `raise CustomError("Input must be a non-negative integer.")`: Raises the custom exception with another specific error message.

7. `try:`: The try block where the main code is executed.

8. `user_input = int(input("Enter a non-negative integer: "))`: Gets user input and converts it to an integer.

9. `result = check_number(user_input)`: Calls the `check_number` function to validate the input.

10. `except CustomError as ce:`: Handles the custom exception, printing the specific error message.

11. `except ValueError:`: Handles the ValueError if the user enters a non-integer value.

12. `except Exception as e:`: Catches any other exceptions that may occur.

13. `else:`: Executes if no exception is raised in the try block.

14. `finally:`: Always executes, whether an exception occurred or not.

This code demonstrates how to define and raise custom exceptions and handle them in a structured way.
