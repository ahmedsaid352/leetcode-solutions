class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = int(len(nums)/2)
        nums_count = {}
        for num in nums:
            if num in nums_count.keys():
                nums_count[num] += 1
            else:
                nums_count[num] = 1

        for number , count in nums_count.items():
            if count > n :
                return number