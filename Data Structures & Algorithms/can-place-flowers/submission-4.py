class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if n == 0:
            return True
        for i in range(len(flowerbed)-1):
            if n==0:
                return True

            if i ==0 and flowerbed[i] == 0 and flowerbed[i+1] ==0:
                flowerbed[i]=1
                n-=1

            if flowerbed[i+1] == 0 and flowerbed[i-1] == 0 and flowerbed[i] != 1:
                n-=1
                flowerbed[i] = 1


        last= len(flowerbed)-1
        if flowerbed[last] == 0 and flowerbed[last - 1] ==0:
            flowerbed[last] = 1
            n-=1

        if n == 0:
            return True
        
        print("n= " + str(n))
        print(flowerbed)
        return False