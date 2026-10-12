class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 1

        pos = {}
        current = 0
        lmax = 0

        for idx, char in enumerate(s):
            if char not in pos:
                pos[char] = idx
                current += 1
                
            else:
                if pos[char] >= start:
                    current -= (pos[char]-start)
                    start = pos[char]+1
                    pos[char] = idx
                else:
                    pos[char] = idx
                    current += 1
            print(idx, char, start, current, lmax, pos)

            lmax = max(current, lmax)
        return lmax

