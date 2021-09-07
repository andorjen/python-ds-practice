def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """
    word_lower = word.lower()
    letter_lower = letter.lower()
    sum_letter = 0
    for l in word_lower:
        if l == letter_lower:
            sum_letter += 1
    return sum_letter

    # check out .count()
