class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        last_index = n -1 
        if (nums[0] == 0) and (len(nums) > 1):
            return False
        elif (nums[0] == 0) and (len(nums) == 1):
            return True
        
        def calculate_zero_streak_distance(index):
            c = 1
            for el in nums[index+1:]:
                if el == 0:
                    c+=1
                else:
                    break
            return c

        def we_can_jump(distance , index):
            j = index - 1
            for i in range(index):
                if  ((distance + i) < nums[j]) or (nums[j] + j >= last_index):
                    return True
                else:
                    j-=1
            return False

        for i in range(n):
            if i == last_index:
                return True
            if nums[i] == 0:
                zero_streak_distance = calculate_zero_streak_distance(i)
                print(zero_streak_distance , i)
                if we_can_jump(zero_streak_distance , i) == False:
                    return False
