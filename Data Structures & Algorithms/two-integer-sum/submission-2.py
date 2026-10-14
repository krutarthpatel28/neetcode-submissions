class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_hash = {}
        for index, num in enumerate(nums):
            index_hash[num] = index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in index_hash and index_hash[complement] != i:
                return [i, index_hash[complement]]
            else:
                continue