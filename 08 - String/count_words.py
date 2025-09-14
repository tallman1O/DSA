def count_words(s):
    """
    Function to count the number of words in the input string.

    Parameters:
    s (str): The input string to check for words.

    Returns:
    int: The count of words in the input string.
    """
    # Your code here
    count = 0
    in_word = False

    for char in s:
        if char != ' ':
            if not in_word:  # start of a new word
                count += 1
                in_word = True
        else:
            in_word = False  # space ends the word

    return count
