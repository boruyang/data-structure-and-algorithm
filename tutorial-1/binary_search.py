def binary_search(list, target):
    """
    Perform binary search for given target on given sorted list.

    Args:
        list: the sorted list we want to search.
        target: the number we want to find.
        
    Returns:
        the index position of target if found, else returns None.
    """

    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None

def verify(index):
    """
    Verify if a given index is None or not, and print the outcome.

    Args:
        index: an evaluated index.
    """
    
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = range(1, 11)

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)