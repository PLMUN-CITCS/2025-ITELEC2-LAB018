def square(num):
    """Returns the square of the given number."""
    return num * num  # Or num ** 2

def sum_of_squares(numbers):
    """Returns the sum of the squares of the numbers in the list."""
    total = 0
    for n in numbers:
        total += square(n)  # Call the square function and add to total
    return total

numbers_list = [2, 3, 4]
result = sum_of_squares(numbers_list)

print(f"The sum of squares is: {result}")