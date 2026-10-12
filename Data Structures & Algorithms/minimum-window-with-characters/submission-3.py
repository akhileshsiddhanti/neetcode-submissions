class Solution:

    def is_valid_window(self, w_map, t_map) -> bool:
        for i in range(128):
            if w_map[i] < t_map[i]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if s == t:
            return s
        if len(s) == len(t) and len(s) == 1:
            if s==t:
                return s
            else:
                return ""

        t_map = [0 for i in range(128)]
        w_map = [0 for i in range(128)]
        n = len(s)
        min_length = n*2
        min_window = (0,n-1)

        for char in t:
            t_map[ord(char)] += 1

        l = 0

        print(t_map)
        for i, char in enumerate(s):
            w_map[ord(s[i])] += 1

            while self.is_valid_window(w_map, t_map) and l<=i:
                
                if i-l+1 < min_length:
                    min_length = i - l + 1
                    min_window = (l,i)
                
                w_map[ord(s[l])] -= 1
                l += 1
        if min_length <= n:
            return s[min_window[0]:min_window[1]+1]
        return ""
