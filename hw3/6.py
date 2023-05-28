
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# Сложность цикла O(n)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Задаем быстрый и медленный маркер
        slow, fast = head, head
        # Запусткаем цикл и когда быстрый
        # маркер догонит медленный, то значит зациклилось
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False