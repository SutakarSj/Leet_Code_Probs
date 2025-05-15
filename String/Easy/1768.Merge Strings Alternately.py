class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1,w2=len(word1),len(word2)
        ans=[]
        a,b=0,0
        pointer=0
        while a < w1 and b < w2:
            if pointer==0:
                ans.append(word1[a])
                a+=1
                pointer=1
            if pointer==1:
                ans.append(word2[b])
                b+=1
                pointer=0
        while a<w1:
            ans.append(word1[a])
            a+=1
        while b<w2:
            ans.append(word2[b])
            b+=1
        return "".join(ans)