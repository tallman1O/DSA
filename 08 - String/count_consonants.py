def count_consonants(s):
    """
    Function to count the number of consonants in the input string.

    Parameters:
    s (str): The input string to check for consonants.

    Returns:
    int: The count of consonants in the input string.
    """
    # Your code here
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in s.lower():
        if char.isalpha() and char not in vowels:
            count += 1

    return count


print(count_consonants("hello"))
