def recursive_binary_search(list, target):
    """
    Perform recursive binary search for given target on given sorted list.

    Args:
        list: the sorted list we want to search.
        target: the number we want to find.
        
    Returns:
        True if found, else returns False.
    """

    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        elif list[midpoint] < target:
            return recursive_binary_search(list[midpoint+1:], target)
        else:
            return recursive_binary_search(list[:midpoint], target)

def verify(result):
    """
    Print whether the target is found.

    Args:
        result: the result printed.
    """
    
    print("Target found:", result)

numbers = range(1, 11)

result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)