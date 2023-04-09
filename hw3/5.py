#Сложность O(mn)
class Solution:
    def islandPerimeter(self, grid):
        #Проверка на пустую матрицу
        if not grid:
            return 0
        
        #Длина колонок и рядов
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        
        #Проходимся по матрице
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # Если находим сушу значит периметр уже 4 
                    perimeter += 4
                    
                    # Проверяем соседей
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                        
        return perimeter