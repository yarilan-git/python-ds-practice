def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    valid_inputs = ["add", "remove", "begining", "end"]
    if command not in valid_inputs or location not in valid_inputs:
        return None
    if command == "add":
        if location == "begining":
            lst.insert(0, value)
        else:
            lst.append(value)
    else:
        if location == "begining":
            lst.pop(0)
        else:
            lst.pop(len(lst) - 1)
    return lst
    
print(list_manipulation([2, 4, 6, 8, 10], "add", "begining", 1))
print(list_manipulation([2, 4, 6, 8, 10], "add", "end", 100))
print(list_manipulation([2, 4, 6, 8, 10], "remove", "begining"))
print(list_manipulation([2, 4, 6, 8, 10], "remove", "end"))
print(list_manipulation([2, 4, 6, 8, 10], "sing", "begining", 1))
print(list_manipulation([2, 4, 6, 8, 10], "add", "middle", 1))
    
    
