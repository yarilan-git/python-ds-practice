def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counter = {}
    for num in nums:
        if num not in counter:
            counter[num] = nums.count(num)
    most_common = 0
    for (k, v) in counter.items():
        if v > most_common:
            most_common = k
    return most_common

print(mode([1, 2, 1]))
print(mode([2, 2, 3, 3, 2]))

