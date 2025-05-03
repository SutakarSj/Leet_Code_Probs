
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s)==0:
            return t
        res = 0
        for i in s + t:
            res ^= ord(i) # ord() ASCii value
        return chr(res) # chr() char value
