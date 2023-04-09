# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Алгаритм сложности O(n)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #задаем быстрый и медленный указатель
        fast ,slow = head,head
        '''
        Проходимся по значениям связанного 
        списка быстрым и медленным указателем,
        чтобы пока быстрый дошел до конца
        медленный был посередине
        '''
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #Переворачиваем вторую часть списка
        prev =None
        while slow:
            temp = slow.next
            slow.next =prev
            prev = slow
            slow = temp

        left , right = head , prev
        # Сравнение значений первой 
        # половины списка с соответствующими значениями 
        # перевернутой второй половины
        while right:
            if left.val != right.val:
                return False
            left , right = left.next, right.next

        return True      