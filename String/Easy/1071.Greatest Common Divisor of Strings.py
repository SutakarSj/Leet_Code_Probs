﻿class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1+str2)==(str2+str1):
            GCD=gcd(len(str1),len(str2))
            res=str1[0:GCD]
            return res
        return ""