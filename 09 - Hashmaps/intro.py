# hashmaps = {}
# hashmaps['one'] = 1  # key: one , value: 1
# print(hashmaps)



def count_frequency(nums):
    result = {}

    for num in nums:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1
    return result


nums = [1,2,2,2,3,4,5,5,6,6,6,6,6,6,8,9,10,10]
print(count_frequency(nums))