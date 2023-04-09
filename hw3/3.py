# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#Сложность алгоритма O(n)
class Solution:
    def averageOfLevels(self, root: TreeNode):
        #Проверяем пустой ли список
        if not root:
            return []
        #Список для хранения значений
        list = []
        queue = [root]

        while queue:
            number = len(queue)
            sum = 0
            # Для каждого узла на текущем уровне
            for _ in range(number):
                # Получаем первый узел из очереди и добавляем его значение в сумму
                node = queue.pop(0)
                sum += node.val
                # Если у узла есть левый потомок, добавляем его в очередь
                if node.left:
                    queue.append(node.left)
                # Если у узла есть правый потомок, добавляем его в очередь
                if node.right:
                    queue.append(node.right) 
            # Добавляем среднее значение узлов на текущем уровне в список
            list.append(sum/number)

        return list