# python3
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = nums1 + nums2
        l.sort()
        n = len(l)//2
        if len(l)%2 == 0:
            return (l[n] + l[n-1]) / 2
        else:
            return l[n]