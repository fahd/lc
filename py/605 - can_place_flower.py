class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(0, len(flowerbed)):
            next_in_range = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0 
            prev_in_range = i == 0 or flowerbed[i-1] == 0

            if next_in_range and prev_in_range and flowerbed[i] == 0:
                flowerbed[i] = 1
                n-=1
            if n == 0:
                return True
        return n <= 0