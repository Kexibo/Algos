import heapq

n = int(input())
h = list(map(int, input().split()))
heapq.heapify(h)
s = 0
for i in range (n-1):
    n1 = heapq.heappop(h)
    n2 = heapq.heappop(h)
    s += (n1+n2)* 0.05
    heapq.heappush(h, n1+n2)
print(s)