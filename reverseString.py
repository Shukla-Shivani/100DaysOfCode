class Solution(object):
    def reverseString_1(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = list(s)
        i = 0
        j = len(s) - 1
        while i<j:
            r[i], r[j] = r[j], r[i]
            i = i+1
            j = j-1

        return "".join(r)

    def reverseString(self, s):
        #slice notation

        return s[::-1]
