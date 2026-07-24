class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seted = set(nums)
        if len(nums) != len(seted):
            return True
        else:
            return False