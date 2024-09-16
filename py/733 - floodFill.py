def travel(image: List[List[int]], sr:int, sc:int, color:int, val:int):
    # out of bounds y
    if sr < 0 or sr >= len(image):
        return
    # out of bounds x
    if sc < 0 or sc >= len(image[0]):
        return
    # if already the color we want
    if image[sr][sc] == color:
        return
    # not the original value we are changing, we want to exit out
    if image[sr][sc] != val:
        return
    
    image[sr][sc] = color
    
    dirs = [
        [0,1],  #down
        [0,-1], #up
        [1,0],  #right
        [-1,0]  #left
    ]

    for x,y in dirs:
        travel(image, sr + y, sc + x, color, val)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        travel(image, sr, sc, color, image[sr][sc])
        return image

        