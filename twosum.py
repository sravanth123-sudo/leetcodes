
#
def twosum(nums, target):
    for i in range(0,len(nums)-1):
        for j in range(i,len(nums)-1):
            if nums[i]+nums[j+1]==target:
                return i,j+1
nums = list(map(int,input().split(',')))
target = int(input())
result = twosum(nums,target)
print(result)









'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num3 = nums1 + nums2
        num3.sort()
        length = len(num3)
        if length % 2 == 0:
            return ((num3[(length // 2) - 1] + num3[length // 2]) / 2)
        else:
            return float(num3[length // 2])
'''
from typing import Optional, List

'''
def maxArea( height):
    sum = 0
    index1 = 0
    index2 = len(height)-1
    while index1 < index2:
        sum = max(sum,((index2-index1)*min(height[index1],height[index2])))
        if height[index1]<height[index2]:
            index1+=1
        else:
            index2-=1
    return sum
height = [1,8,6,2,5,4,8,3,7]
result = maxArea(height)
print(result)
'''


'''
class ListNode:
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    list1 = []
    if len(lists)==0:
        return list1
    elif len(lists)==1:
        list1 = lists[0]
        return list1
    else:
        for i in range(0,len(lists)):
            k = lists[i]
            for j in range(0,len(lists[i])):
                list1.append(k[j])
        list1.sort()
        return list1
lists = [[1,4,5],[1,3,4],[2,6]]
#lists = [[]]
result = mergeKLists(lists)
print(result)
'''

