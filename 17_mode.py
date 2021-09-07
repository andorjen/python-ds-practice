def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    (highestNum, count) = (0, 0)
    uniqueNum = set(nums)
    for num in uniqueNum:
        if nums.count(num) > count:
            count = nums.count(num)
            highestNum = num
    return highestNum


# snake_case variables

# frequency counter for O(n) solution
#library- counter
