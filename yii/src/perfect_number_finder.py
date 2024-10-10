import sys
sys.path.append('src')
from get_all_perfect_numbers_fetch import find_perfect_numbers

def get_user_input():
    return int(input("Please enter a number greater than or equal to 1: "))

def display_perfect_numbers(number, perfect_numbers):
    print(f"Here are the perfect numbers from 1 to {number}: {', '.join(map(str, perfect_numbers))}")

def run_perfect_number_finder():
    while True:
        number = get_user_input()
        perfect_numbers = find_perfect_numbers(number)
        display_perfect_numbers(number, perfect_numbers)

if __name__ == "__main__":
    run_perfect_number_finder()
