

def twosum(nums, target):
    for i in range(0,len(nums)-1):
        for j in range(i,len(nums)-1):
            if nums[i]+nums[j+1]==target:
                return i,j+1
nums = list(map(int,input().split(',')))
target = int(input())
result = twosum(nums,target)
print(result)



