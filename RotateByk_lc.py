class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        arr = []
        i = 0
        length = len(nums)

        k = k%length #rotation is k%length

        kstart = length-k
        for j in range (kstart, length):
            arr.append(nums[j])

        for j in range(0, kstart):
            arr.append(nums[j])

        for x in arr:
            nums[i] = x
            i = i+1
