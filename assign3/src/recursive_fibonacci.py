from .fibonacci import validate_position

@validate_position
def recursive_fibonacci(position, function_to_call = lambda _: recursive_fibonacci(_)):
    return function_to_call(position - 1) + function_to_call(position - 2) if position > 1 else 1
