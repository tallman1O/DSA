def first_non_repeating_char(s):
    seen = {}

    for char in s:
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1

    for char in s:
        if seen[char] == 1:
            return char

    return None


s = "swiss"
print(first_non_repeating_char(s))