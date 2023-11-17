class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sorted_nums = sorted(nums)
        i = 0
        j = len(nums) - 1 
        n = 0
        while j > i:
            if (sorted_nums[i] + sorted_nums[j]) == k:
                i+=1
                j-=1
                n+=1
            elif (sorted_nums[i] + sorted_nums[j]) > k:
                j-=1
            else :
                i+=1
        return n
        