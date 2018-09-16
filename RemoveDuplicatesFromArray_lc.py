class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0):
            return 0
        prev = nums[0]
        j = 1
        for i in range(1,len(nums)):
            if(prev!=nums[i]):
                nums[j] = nums[i]
                prev = nums[i]
                j = j + 1

        return j


class Solution2(object):
    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==0):
            return 0
        i = 0
        for j in range(1,len(nums)):
            if (nums[i]!=nums[j]):
                i = i+1
                nums[i]=nums[j]
        return i+1
