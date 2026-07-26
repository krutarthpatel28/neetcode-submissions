class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}
        for i in range(len(nums)):
            if nums[i] in numDict:
                numDict[nums[i]] += 1
            else:
                numDict[nums[i]] = 1
        sorted_dict = dict(sorted(numDict.items(), key=lambda item: item[1], reverse=True))
        count = 0
        output=[]
        for key, value in sorted_dict.items():
            output.append(key)
        return output[:k]