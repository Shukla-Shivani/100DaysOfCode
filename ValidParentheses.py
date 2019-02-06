class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if s=="":
            return True
        for i in s:
            if i=="(":
                stack.append(")")
            elif i=="{":
                stack.append("}")
            elif i=="[":
                stack.append("]")
            elif not stack or stack.pop() != i:
                return False
        return not stack
                
## Complexity - O(n)