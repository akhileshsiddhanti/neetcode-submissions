class Solution:
    def isAlphaNumeric(self, c):
        if ord(c.lower()) >= 97 and ord(c.lower()) < (97+26):
            return True
        if ord(c) >= 48 and ord(c) <= 57:
            return True
        return False

    def isPalindrome(self, s_raw: str) -> bool:
        if len(s_raw) == 0 and len(s_raw) == 1:
            return True
        
        s = ""
        for si in list(s_raw):
            if self.isAlphaNumeric(si):
                s += si.lower() 
        
        print(s)

        return self.check_palindrome(s)

    def check_palindrome(self, s: str):
        if len(s) == 0 or len(s) == 1:
            return True
        elif s[0] == s[-1]:
            return self.check_palindrome(s[1:-1])
        else:
            return False

        