class Solution(object):
    def rotate(self, nums, k):
        k=k%5
        nums[:]=nums[-k:]+nums[:-k]