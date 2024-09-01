def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    # Apply the decorator to the function and return the decorated function
    return decorator_func(func)

# Define a test function
@apply_decorator
def my_function():
    return "Function executed"

# Call the decorated function
print(my_function())  # Output: Decorator Applied \n Function executed
