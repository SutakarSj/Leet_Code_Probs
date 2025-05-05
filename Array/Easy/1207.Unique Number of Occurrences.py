class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq=Counter(arr)
        if len(set(freq.values()))==len(freq.values()):
            return True 
        return False