def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    nums.sort()
    i  = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            return nums[i]
        i += 1
    
print(find_the_duplicate([1, 2, 1, 4, 3, 12]))
print(find_the_duplicate([6, 1, 9, 5, 3, 4, 9]))
print(find_the_duplicate([2, 1, 3, 4]))
        
