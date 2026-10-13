class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_hash = {}
        for i in s:
            if i in count_hash:
                count_hash[i] += 1
            else:
                count_hash[i] = 1
            
        for i in t:
            if i in count_hash:
                count_hash[i] -= 1
            else:
                return False
        flag = True
        for key in count_hash:
            if count_hash[key] != 0:
                return False
            else:
                continue
        return True