class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        d = deque()

        opening_brackets = ['(', "[", "{"]
        closing_brackets = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in opening_brackets:
                d.append(char)
            else:
                if len(d) > 0 and char == closing_brackets[d[-1]]:
                    d.pop()
                else:
                    return False
        
        if len(d) == 0:
            return True
        else:
            return False



        