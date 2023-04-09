#Сложность алгоритма - O(mn)
class Solution:
    def numIslands(self, grid):
        #Получаем длину строк и колонок
        rows, cols = len(grid), len(grid[0])
        #Поиск в глубину
        def dfs(i,j):
            #Если ничего нет выходим из функции
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == "0":
                return
            #Убираем 1 чтобы он не искал покругу
            grid[i][j] = "0"
            #Применяем к соседним ячейкам
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        #Переменная для количества островов
        islands = 0
        #Проходимся по матриче и ищем острова
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i,j)

        return islands