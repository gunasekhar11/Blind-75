def maxArea(height):
    p1 = 0
    p2 = len(height)-1
    max_area = 0
    while p1 < p2:
        calculated_area = (min(height[p1],height[p2])*(p2-p1))
        if(max_area<calculated_area):
            max_area = calculated_area
        if(height[p1]>height[p2]):
            p2-=1
        else:
            p1+=1
    return max_area

arr = [1,8,6,2,5,4,8,3,7]
print(maxArea(arr))