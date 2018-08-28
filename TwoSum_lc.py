# Runtime in O(n^2),Space: O(1)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length-1):
            for j in range(i+1,length):
                if nums[i]+nums[j]==target:
                    return [i,j]


"""
LeetCode solution in O(n),Space:O(n)
"""
class Solution_1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Given two sum, we can iterate and try out every combination. This will cause n^2 times.
        else we can use hashmap to store each number as key and index as value and try to see if the target sum exists.
        """
        dic = {}
        for i, val in enumerate(nums):
            if target - val in dic:
                return [i, dic[target - val]]
            dic[val] = i


print(Solution().twoSum([2,4,5,8],13))
print(Solution_1().twoSum([2,4,5,8],13))
