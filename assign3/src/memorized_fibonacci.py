from .fibonacci import validate_position
from .recursive_fibonacci import recursive_fibonacci

@validate_position
def memorized_fibonacci(position, cache=None):
    cache = {0: 1, 1: 1} if cache is None else cache

    if position not in cache:
        cache[position] = recursive_fibonacci(position, lambda position: memorized_fibonacci(position, cache))
        
    return cache[position]
