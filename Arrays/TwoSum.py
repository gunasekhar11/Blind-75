def TwoSum(arr,target):
    hashmap = {}
    for i in range(len(arr)):
        remaining = target - arr[i]
        if(remaining in hashmap):
            return [hashmap[remaining],i]
        hashmap[arr[i]] = i
arr = [1,2,3,4,5,6,100]
target = 101
print(TwoSum(arr,target))
