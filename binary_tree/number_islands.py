
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


def numIslands(grid) -> int:
    rows = len(grid)
    cols = len(grid[0])

    def bfs(row, col):
        if row < 0 or row == rows:
            return
        elif col < 0 or col == cols:
            return
        
        if grid[row][col] != '1':
            return
        
        grid[row][col] = 'V'

        bfs(row+1, col)
        bfs(row-1, col)
        bfs(row, col+1)
        bfs(row, col-1)

    
    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] == '1'):
                bfs(i, j)
                islands += 1
        
    print(islands)


numIslands(grid) 