import sys
sys.path.append('src')
from get_perfect_number import is_perfect

def find_perfect_numbers(number):
    return [perfect_number for perfect_number in range(1, number + 1) if is_perfect(perfect_number)]
