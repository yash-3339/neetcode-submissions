class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has={}
        complement=0
        for index,value in enumerate(nums):
            complement = target - value
            if complement in has :
                return sorted([index,has[complement]])
            has[value]=index
        return []