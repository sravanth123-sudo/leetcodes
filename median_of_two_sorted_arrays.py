def findMedianSortedArrays(nums1, nums2):
    num3 = nums1 + nums2
    num3.sort()
    length = len(num3)
    if length % 2 == 0:
        return ((num3[(length // 2) - 1] + num3[length // 2]) / 2)
    else:
        return float(num3[length // 2])

nums1 = list(map(int,input().split(',')))
nums2 = list(map(int,input().split(',')))
result = findMedianSortedArrays(nums1,nums2)
print(result)

