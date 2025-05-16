class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        word_len = len(words)
        for i in range(word_len):
            if words[i].startswith(pref):
                count+=1
        return count