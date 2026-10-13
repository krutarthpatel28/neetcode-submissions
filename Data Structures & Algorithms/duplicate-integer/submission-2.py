class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe_dict = {}
        for i in nums:
            if i not in dupe_dict:
                dupe_dict[i] = True
            else:
                return True
        return False