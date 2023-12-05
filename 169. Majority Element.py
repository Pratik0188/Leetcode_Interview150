from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        count=Counter(nums)
        items=count.items()
        length=len(nums)

        for n,i in items:
            if i>(length/2):
                return n