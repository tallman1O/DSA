def is_palindrome(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            return False

        left=+1
        right=-1

    return True

if __name__ == "__main__":
    arr = [7, 8, 9, 8, 7]
    print(is_palindrome(arr))
