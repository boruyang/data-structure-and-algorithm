def quick_sort(values):
    """
    Sort a given list by quick sort.

    Args:
        values: the list we want to sort.

    Returns:
        the sorted list.
    """

    if len(values) <= 1:
       return values

    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]

    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)

    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

print(quick_sort([1,5,4,8,2]))
