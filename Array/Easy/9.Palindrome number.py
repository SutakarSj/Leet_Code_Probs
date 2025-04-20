class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        value,pali = x,0
        while x != 0:  
            pali = pali * 10 + x%10
            x//=10
        return value == pali        