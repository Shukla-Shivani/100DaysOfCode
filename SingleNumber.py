#Using a Dictionary
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for i in nums:
            counts[i] = counts.get(i,0) + 1

        for key, value in counts.items():
            if value == 1:
                return key
#Runtime: O(n); Space: O(n)



#Bit Manipulation
class Solution_1(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r=0
        for n in nums:
            r^=n

        return r
#Runtime: O(n); Space: O(1)
