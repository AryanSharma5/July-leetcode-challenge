class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.ans = 0
        self.grid = grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j]:
                    self.helper(i, j)
        return self.ans
    def helper(self, i, j):
        p = 4
        if self.grid[i][j]:
            if 0<=i-1<len(self.grid) and self.grid[i-1][j]:
                p -= 1
            if 0<=i+1<len(self.grid) and self.grid[i+1][j]:
                p -= 1
            if 0<=j-1<len(self.grid[0]) and self.grid[i][j-1]:
                p -= 1
            if 0<=j+1<len(self.grid[0]) and self.grid[i][j+1]:
                p -= 1
            self.ans += p