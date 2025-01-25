# Python ZeroDivisionError Example

This example showcases a common error in Python: ZeroDivisionError.  The code demonstrates a function that handles the division by zero case but in an unusual way, returning 0 instead of raising the error, which might mask the root issue. It illustrates that while the code runs without crashing, it might produce unexpected or incorrect results.

## How to Reproduce
1. Save the code as `bug.py`.
2. Run the script from your terminal using `python bug.py`.

## Solution
The provided solution enhances error handling for better robustness and clarity. Consider the scenarios where returning 0 might not be sufficient. Alternative solutions might include logging an error message, raising a custom exception or defaulting to a value based on context.