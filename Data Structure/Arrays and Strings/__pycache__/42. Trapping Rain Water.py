def trap(height):
    if len(height)==0:
        return 0
    left, right = 0, len(height)-1
    left_max, right_max = height[left], height[right]
    res = 0
    while left<=right:
        if left_max < right_max:
            left_max = max(left_max, height[left]) 
            res += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            res += right_max - height[right]
            right -= 1
    return res
trap([0,1,0,2,1,0,1,3,2,1,2,1])