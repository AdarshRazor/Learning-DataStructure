def twonumbersum(arr,target):
    for i in range(len(arr)):
        a=arr[i]
        for j in range(i+1, len(arr)):
            if a+arr[j]==target:
                return [a,arr[j]]
    return []

def twonumbersum2(arr,target):
    nums={}
    for num in arr:
        if target - num in nums:
            return [target-num, num]
        else:
            nums[num] = True
    return []

def twonumbersum3(arr,target):
    arr.sort()
    left=0
    right=len(arr)-1
    while right > left:
        sum = arr[left] + arr[right]
        if sum == target:
            return[arr[left],arr[right]]
        elif sum > target:
            right -= 1
        elif sum < target:
            left += 1
    return []


arr= [ 3,5,-4,8,11,1,-1,6]
target=10
print(twonumbersum(arr,target))
print(twonumbersum2(arr,target))
print(twonumbersum3(arr,target))