def is_perfect(number):
    if number < 1: return False

    return sum([factor for factor in range(1, number // 2 + 1) if number % factor == 0]) == number
