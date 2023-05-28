
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#Сложность алгоритма составляет O(n)
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        #Задаем указатель
        ptr = head
        #Задаем переменную дя хранения двоичного числа
        s = ''
        #Вытаскиваем все значения
        while ptr != None:
            #print(ptr.val)
            #Записываем их впеременную и идем к следующему значению
            s += str(ptr.val)
            ptr = ptr.next
        #print(s)
        #Используем int для переделки в 10 систему
        return int(s, 2)