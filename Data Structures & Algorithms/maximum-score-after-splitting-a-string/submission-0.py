class Solution:
    def maxScore(self, s: str) -> int:
        newscore= 0

        for j in range(len(s)-1):

            arr1=s[:j+1]
            arr2=s[j+1:]

            score = arr1.count("0") + arr2.count("1")
            newscore =max(newscore, score)


        return newscore