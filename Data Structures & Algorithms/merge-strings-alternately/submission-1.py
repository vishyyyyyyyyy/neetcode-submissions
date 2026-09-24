class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        l1 = len(word1)
        l2 = len(word2)

        min = 0
        

        if l1 > l2:
            min= l2
        else:
            min = l1

        string = ""
        count =0
        for i in range(min):
            string +=word1[i]
            string += word2[i]
            count +=1


        if l1 > l2:
            string += word1[min:]
        else:
            string += word2[min:]
        
        return string
