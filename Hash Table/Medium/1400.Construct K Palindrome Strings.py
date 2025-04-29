class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k>len(s):
            return False
        total = Counter(s)
        result = 0
        for i in total.values():
            if i%2==1:
                result+=1
        return result<=k        