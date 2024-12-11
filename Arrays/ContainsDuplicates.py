def containsDuplicate(nums):
    hashmap = {}
    for i in range(len(nums)):
        if nums[i] in hashmap:
            return True
        hashmap[nums[i]] = i
    return False

arr = [1,2,3,4,2,5]
print(containsDuplicate(arr))