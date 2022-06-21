def linear_search(list, target):
    """
    Perform linear search for given target on given list.

    Args:
        list: the list of numbers we want to search.
        target: the number we want to find.
        
    Returns:
        the index position of target if found, else returns None.
    """

    for i in range(len(list)):
        if list[i] == target:
            return i
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

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)