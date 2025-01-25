def improved_function(a, b):
    if a == 0:
        print("Warning: Division by zero encountered.")  # Log the issue
        return None # Return None or a default value that makes sense
        #raise ZeroDivisionError("Division by zero") # Alternatively, re-raise for better error tracking
    return b / a

result = improved_function(0, 10)
print(result) # Output: Warning: Division by zero encountered. None

result = improved_function(10, 0)
print(result) # Output: Warning: Division by zero encountered. None