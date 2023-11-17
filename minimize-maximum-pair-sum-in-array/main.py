class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_pair = 0
        sorted_nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        while j > i:
            if (sorted_nums[i] + sorted_nums[j]) > max_pair:
                max_pair = sorted_nums[i] + sorted_nums[j]
            i+=1
            j-=1
        
        return max_pair
        