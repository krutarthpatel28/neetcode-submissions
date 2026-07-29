class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []
        i=0
        while i<len(numbers):
            toFind = target - numbers[i]
            if toFind in numbers:
                j = numbers.index(toFind, i + 1)
                output.extend([i+1, j+1])
                break
            else:
                i += 1
        return output