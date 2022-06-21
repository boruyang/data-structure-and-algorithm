def selection_sort(values):
    """
    Sort a given list by selection sort.

    Args:
        values: the list we want to sort.

    Returns:
        the sorted list.
    """

    sorted_list = []
    for _ in range(len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
    
    return sorted_list

def index_of_min(values):
    """
    Find the index of the smallest number of a list.

    Args:
        values: the list we want to check.

    Returns:
        the index with the smallest number.
    """

    min_index = 0
    for i in range(len(values)):
        if values[i] < values[min_index]:
            min_index = i
    
    return min_index

print(selection_sort([1,5,4,8,2]))