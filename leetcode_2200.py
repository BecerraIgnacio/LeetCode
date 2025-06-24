nums = [2,2,2,2,2]
key = 2
k = 2

def ejercicio(nums, key, k):
    check = []
    for num in range(0, len(nums)):
        if nums[num] == key:
            check.append(num)
    result = []
    if check != []:
        for i in range(0, len(nums)):
            for j in range(0, len(check)):
                if abs(i - check[j]) <= k and nums[check[j]] == key:
                    result.append(i)
                    break

    return result

print(ejercicio(nums, key, k))