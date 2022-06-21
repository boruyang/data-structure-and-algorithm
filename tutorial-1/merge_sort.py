def merge_sort(list):
    """
    Sort a list in a ascending order by merge sort.

    Args:
        list: the list we want to sort.

    Returns:
        a new sorted list.
    """
    
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists.

    Args:
        list: the list we want to split.

    Returns:
        two lists - left and right.
    """

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    """
    Merge two lists (arrays), sorting them in the process.
    
    Args:
        left: the first list we want to merge.
        right: the second list we want to merge.

    Returns:
        a new merged and sorted list.
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1
    
    while j < len(right):
        l.append(right[j])
        j += 1

    return l

def verify_sorted(list):
    """
    Verify if a given list is sorted.

    Args:
        list: the list we want to verify.

    Return:
        True if the list is sorted.
    """

    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])

new_list = [33, 24, 17, 81, 1]
sorted_list = merge_sort(new_list)
print(sorted_list)
print(verify_sorted(sorted_list))