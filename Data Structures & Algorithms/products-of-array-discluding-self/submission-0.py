class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i in range(len(nums)):
            if(i==0):
                prefix.append(nums[i])
            else:
                prefix.append(prefix[i-1]* nums[i])
        postfix = [1] * len(nums)
        postfix[-1] = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            postfix[i] = nums[i] * postfix[i+1]
        
        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(postfix[i+1])
            elif i== len(nums)-1:
                output.append(prefix[i-1])
            else:
                output.append(prefix[i-1] * postfix[i+1])
        return output