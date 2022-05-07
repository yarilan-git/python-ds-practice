def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    words = phrase.lower().split(" ")
    capped_phrase = words[0].capitalize()
    for word in words[1:]:
        capped_phrase += f" {word.capitalize()}"
    return capped_phrase

print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))

