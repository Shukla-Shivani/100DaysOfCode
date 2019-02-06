class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        max_sum = nums[0]
        current_sum = nums[0]
        
        for i in range(1, len(nums)):
            current_sum = max(current_sum + nums[i], nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum
        
        