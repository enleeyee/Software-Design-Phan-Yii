from functools import reduce
from .fibonacci import validate_position

@validate_position
def functional_fibonacci(position):
    return reduce(lambda pair, i: (pair[1], pair[0] + pair[1]), range(position), (1, 1))[0]
