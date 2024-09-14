def sum_two_smallest_numbers(numbers):
    result = sum(sorted(numbers)[:2])
    return result