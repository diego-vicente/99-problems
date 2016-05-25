

def last(list):
    """Problem 1: Find the last element of a list.

    :list: list to be processed
    :returns: last element of the list
    
    >>> last([1, 2, 3, 4])
    4
    >>> last([23, 12, 1])
    1

    """
    # It is trivial to solve using array slicing
    return list[-1]

def last_but_one(list):
    """Problem 2: Find the last but one element of a list.

    :list: list to be processed
    :returns: last but one element of the list
    
    >>> last_but_one([1, 2, 3, 4])
    3
    >>> last_but_one([23, 12, 1])
    12

    """
    # It is still trivial
    return list[-2]

def at_index(list, k):
    """Problem 3: Find the Kth element of a list

    :list: list to be processed
    :k: ordinal of the element (1 = 1st, 2 = 2nd...)
    :returns: element required
    
    >>> at_index([1, 2, 3, 4], 2)
    2
    >>> at_index([23, 12, 1], 1)
    23

    """
    return list[k-1]

def length(list):
    """Problem 4: Find the number of elements of a list

    :list: list to be processed
    :returns: size of the list

    >>> length([1, 2, 3, 4])
    4
    >>> length([23, 12, 1])
    3

    """
    return len(list)

def reversed(list):
    """Problem 5: Reverse a list

    :list: list to be processed
    :returns: reversed list

    >>> reversed([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> reversed([23, 12, 1])
    [1, 12, 23]

    """
    # Expanded array slicing is `[<start>:<stop>:<step>]`
    return list[::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
