class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest_seq = 1
        current_seq = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i-1] + 1 == nums[i]:
                current_seq += 1
            else:
                longest_seq = max(current_seq, longest_seq)
                current_seq = 1
        return max(current_seq, longest_seq)