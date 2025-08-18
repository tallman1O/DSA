def natural_nums(n):
    if n == 1:
        return 1
    return n + natural_nums(n-1)

print(natural_nums(10))