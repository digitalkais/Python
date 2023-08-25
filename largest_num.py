def find_second_largest(numbers):
    """
    This function takes a list of numbers as input and returns the second largest number in the list.
    """
    largest = None
    second_largest = None

    for num in numbers:
        if largest is None:
            largest = num
        elif num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num

    return second_largest


numbers = [5, 3, 9, 1, 7, 2, 7]
second_largest = find_second_largest(numbers)
print(second_largest)