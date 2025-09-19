def check_for_duplicates(arr):
    ans = {}

    for num in arr:
        if num in ans:
            return True
        else:
            ans[num] = 1
    return False

nums1 = [1,2,3]
print(check_for_duplicates(nums1))