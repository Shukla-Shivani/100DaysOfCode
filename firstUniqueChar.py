class Solution(object):
    def firstUniqChar_1(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0:
            return -1
        if length == 1:
            return 0
        for i in range(0,length):
            for j in range(0, length):
                if i == j:
                    if i!=length-1:
                        continue
                    return i
                if s[i] == s[j]:
                    break
                if j == length-1:
                    return i
        return -1

    def firstUniqChar(self, s):
        count = {}
        length = len(s)
        for i in s:
            if i in count:
                count[i] = count[i] + 1
            else:
                count[i] = 1

        for i in range(length):
            if count[s[i]] == 1:
                return i
        return -1
