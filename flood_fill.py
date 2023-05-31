# https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def bfs(image,sr,sc,color, base_color):
            if sr > len(image)-1 or sc > len(image[0])-1 or sc < 0 or sr < 0:
                return image
            if color == image[sr][sc]:
                return image
            if image[sr][sc] == base_color:
                image[sr][sc] = color
                image = bfs(image,sr,sc+1, color, base_color)
                image = bfs(image,sr,sc-1, color, base_color)
                image = bfs(image,sr+1,sc, color, base_color)
                image = bfs(image,sr-1,sc, color, base_color)
            return image
        return bfs(image,sr,sc,color,image[sr][sc])
                
                
        
        
                
        
        
