class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_hash = {}
        for index, num in enumerate(nums):
            index_hash[num] = index
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in index_hash and i != index_hash[complement]:
                return [i, index_hash[complement]]