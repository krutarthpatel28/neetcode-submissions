class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}
        for i in range(len(strs)):
            string = "".join(sorted(strs[i]))
            if string in word_dict:
                word_dict[string].append(strs[i])
            else:
                word_dict[string] = [strs[i]]
        output = []
        for _, value in word_dict.items():
            output.append(value)
        return output
