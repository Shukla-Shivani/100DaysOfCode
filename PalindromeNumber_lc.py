class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        i=0
        input = str(x)
        j = len(input)-1
        while(i<j):
            if(input[i]==input[j]):
                i = i+1
                j = j-1
            else:
                return False
        return True

print(Solution().isPalindrome(12321))


