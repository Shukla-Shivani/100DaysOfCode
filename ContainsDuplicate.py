class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        for i in range(0,length-1):
            for j in range(i+1,length):
                if(nums[i] == nums[j]):
                    return True
        return False
#Runtime: O(n^2); Space: O(1)

class Solution_1(object):
            def containsDuplicate(self, nums):
                """
                :type nums: List[int]
                :rtype: bool
                """
                length = len(nums)
                nums.sort()
                for i in range (0, length-1):
                    if(nums[i]==nums[i+1]):
                        return True
                return False
#Runtime: O(nlogn); Space: O(1)

class Solution_2(object): #Hashtable
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for it in nums:
            if it in s:
                return True
            s.add(it)
        return False
