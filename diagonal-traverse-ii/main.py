class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        from itertools import chain
        index_sum = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if (i + j) >= len(index_sum):
                    index_sum.append([nums[i][j]])
                else:
                    index_sum[i+j].insert(0, nums[i][j])
        return list(chain.from_iterable(index_sum))

        