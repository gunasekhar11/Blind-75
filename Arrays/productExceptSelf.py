def productExceptSelfBruteForce(nums):
    result = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if j != i :
                product *= nums[j]
        result.append(product)
    return result

def productExceptSelfOptimal(nums):
    left_array=[]
    left_product=1
    right_array=[]
    right_product=1
    result = []
    for i in range(len(nums)):
        left_array.append(left_product)
        left_product *=nums[i]
    for j in range(len(nums)-1,-1,-1):
        right_array.append(right_product)
        right_product *= nums[j]
    right_array = right_array[::-1]
    for i in range(len(nums)):
        result.append(left_array[i]*right_array[i])
    return result

arr = [1,2,3,4]
print(productExceptSelfBruteForce(arr))
print(productExceptSelfOptimal(arr))