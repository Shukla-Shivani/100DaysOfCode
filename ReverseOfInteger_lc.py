class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        num = abs(x)
        while(num!=0):
            rev = rev*10 + num%10
            num = num/10
        if x>0 and rev<2**31:
            return rev
        elif x<0 and rev<2**31:
            return -rev
        else:
            return 0 
