def check_same_string(s1, s2):
    if len(s1) != len(s2):
        return False

    for char in s1:
        if char not in s2:
            return False
        return True
    return True
print(check_same_string("hello", "hello"))