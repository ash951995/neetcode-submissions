class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res={}
        for i,num in enumerate(nums):
            val = target - num
            if val in res:
                return [res[val] , i]
            res[num] = i

        