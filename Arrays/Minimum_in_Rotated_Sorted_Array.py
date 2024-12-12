def FindMinimumInRotatedSortedArray(arr):
    l = 0
    r = len(arr)-1
    while l<r:
        mid = (l+r)//2
        if(arr[mid]>arr[mid+1]):
            return arr[mid+1]
        elif(arr[mid]<arr[mid-1]):
            return arr[mid]
        if(arr[mid]>arr[l]):#Left Side Sorted
            l = mid+1
        else:##Right Side Sorted
            r = mid-1
    return arr[l]

arr = [5,6,7,3,4,4,5,5,5,5,5]
print(FindMinimumInRotatedSortedArray(arr))

