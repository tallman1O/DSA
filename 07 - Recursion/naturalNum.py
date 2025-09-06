# def natural_nums(n):
#     if n == 1: ## Base Case
#         return 1
#     return n + natural_nums(n-1)
#
# print(natural_nums(4))

# Print 1 to n
def natural_nums(n):
    if n <= 0:
        return

    natural_nums(n - 1)
    print(n)



print(natural_nums(10))

# Print n to 1
def natural_nums(n):
    if n <= 0:
        return

    print(n)
    natural_nums(n - 1)

print(natural_nums(5))

