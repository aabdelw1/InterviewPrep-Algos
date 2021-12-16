from collections import deque


end = "AACCGGTA"

queue = deque([(end, 0)])
print(queue)

curr = queue.popleft()
curr_gene = curr[0]
curr_steps = curr[1]

print(curr)
print(curr_gene)
print(curr_steps)