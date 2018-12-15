class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in nums1:
            for j in nums2:
                if(i == j):
                    ans.append(i)
        return list(set(ans))

    def intersection_better(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        small = set()
        ans = set()
        if (nums2>nums1):
            nums1,nums2=nums2,nums1
        for i in nums2:
            small.add(i)
        for i in nums1:
            if(i in small):
                ans.add(i)
        return list(ans)
