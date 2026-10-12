class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mem_s = [0 for i in range(26)]
    
        for i in range(len(s)):
            mem_s[ord(s[i]) - 97] += 1
            mem_s[ord(t[i]) - 97] -= 1
            
        for i in range(26):
            if mem_s[i] != 0:
                return False

        return True

        

        

        