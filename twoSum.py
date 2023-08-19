# Two Sum problem 
# Return a list of integers whose sum equals target
# example [8,6,11,3] target 9 return [1,3]

def two_sum(nums, target):
    d = {}

    for i in range(len(nums)):
        if target - nums[i] in d:
            print(d)
            return [d[target-nums[i]], i]
        
        d[nums[i]] = i

    return -1

L = [8,6,11,3]
print(two_sum(L,9))

L2 = [2,5,3,7,4]
print(two_sum(L2,10))
