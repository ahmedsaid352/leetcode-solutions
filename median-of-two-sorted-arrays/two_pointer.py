# python3
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = nums1 + nums2
        l.sort()
        i=0
        j=len(l)-1
        while i < j :
            if j == i+1:
                return ((l[i]+l[j])/2)
                break
            i+=1
            j-=1
        if j==i:
            return (l[i])