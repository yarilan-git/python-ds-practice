def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    VOWELS = 'aeiou'
    s_as_list = list(s) 
    r_start = len(s_as_list)-1     
    start = 0
    end = len(s_as_list)-1
    for i in range(start, end):
        if s_as_list[i].lower() in VOWELS:
            r_end = i
            for j in range(r_start, r_end, -1):
                if s_as_list[j].lower() in VOWELS:
                    temp = s_as_list[i]
                    s_as_list[i] = s_as_list[j]
                    s_as_list[j] = temp
                    r_start = j-1
                    break
    return ''.join(s_as_list)    

print(reverse_vowels("Hello!"))
print(reverse_vowels("Tomatoes"))
print(reverse_vowels("Reverse Vowels In A String"))
print(reverse_vowels("aeiou"))
print(reverse_vowels("why try, shy fly?"))



