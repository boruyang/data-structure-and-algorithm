import random

def is_sorted(values):
    """
    Check if a given list is sorted or not.

    Args:
        values: the list we want to check.

    Returns:
        True if the list is sorted.
    """

    for index in range(len(values)-1):
        if values[index] > values[index+1]:
            return False

    return True

def bogo_sort(values):
    """
    Sort a given list by randomly shuffle the list.

    Args:
        values: the list we want to sort.

    Returns:
        the sorted list.
    """

    while not is_sorted(values):
        random.shuffle(values)

    return values

print(bogo_sort([1,5,4,8,2]))