class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp={}
        for i,n in enumerate(nums):
            if n in mp:
                return True
            mp[n] = i
        return False