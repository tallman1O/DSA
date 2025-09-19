def topKFrequent(nums, k) :
    ans = {}
    result = []

    for num in nums:
        if num in ans:
            ans[num] += 1
        else:
            ans[num] = 1

    sorted_ans = sorted(ans, key=ans.get, reverse=True)

    for i in range(k):
        result.append(sorted_ans[i])

    return result

nums = [1,2,2,3,4,5,5]
k = 2
print(topKFrequent(nums, k))
