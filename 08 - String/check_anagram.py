def check_anagram(s, t):

    if len(s) != len(t):
        return False

    for char in s:
        if char not in t:
            return False

    return True
