class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_hash = {}
        for i in nums:
            if i not in count_hash:
                count_hash[i] = 1
            else:
                count_hash[i] += 1
        for k, v in count_hash.items():
            if v != 1:
                return True
        return False