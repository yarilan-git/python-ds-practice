def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    sum = 0
    if len(nums) > 0:
        i = 0       
        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums):
                if nums[i] < nums[j]:
                    sum += 1
                j += 1
            i += 1
    return sum

print(find_greater_numbers([1, 2, 3]))
print(find_greater_numbers([6, 1, 2, 7]))
print(find_greater_numbers([5, 4, 3, 2, 1]))
print(find_greater_numbers([]))
        
