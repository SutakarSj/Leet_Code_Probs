class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                str1,str2=words[i],words[j]
                len_str1=len(str1)
                if str1 == str2[:len_str1] and str1 == str2[-len_str1:]:
                    count+=1
        return count