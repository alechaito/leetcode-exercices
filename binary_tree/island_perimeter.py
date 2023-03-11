class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:    
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    strip = 4
                    # checking top
                    if i-1 >= 0 and grid[i-1][j] == 1:
                        strip -= 1
                    # checking bottom
                    if i+1 <= len(grid)-1 and grid[i+1][j] == 1:
                        strip -= 1
                    # checking left
                    if j-1 >= 0 and grid[i][j-1] == 1:
                        strip -= 1
                    # checking right
                    if j+1 <= len(grid[0])-1 and grid[i][j+1] == 1:
                        strip -= 1
                    
                    perimeter += strip
        
        return perimeter