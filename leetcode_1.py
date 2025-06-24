nums = [3,2,3]
target = 6

def ejercicio(nums, target):
        a = []
        for i in range(len(nums)):
            if nums[i]*2 == target:
                numsb = nums[i+1::]
                if target-nums[i] in numsb:
                    a = [i, numsb.index(target-nums[i])+i+1]
                    break
            elif target-nums[i] in nums:
                a = [i, nums.index(target-nums[i])]
                break


        return a

print(ejercicio(nums, target))