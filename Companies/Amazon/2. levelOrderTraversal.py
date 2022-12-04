from collections import deque

def levelOrder(root):
    queue = [root]
    # queue.append(root)
    while(len(queue)>0):
        node = queue.pop(0)
        print(node.info, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def levelOrder(root):
    queue = [root]
    while len(queue) > 0:
        current = queue[0]
        print(current, end=' ')
        if current.left: queue += [current.left]
        if current.right: queue += [current.right]
        queue.pop(0)


def levelOrder(root):
  
    if root is None:
        return

    d = deque()
    d.appendleft(root)

    while(len(d) > 0):
        node = d.pop()
        print(node.info, end = ' ')

        if node.left is not None:
            d.appendleft(node.left)
        if node.right is not None:
            d.appendleft(node.right)

def levelOrder(root):
    q = deque([root])
    while q:
        n = q.popleft()
        if n:
            print(n.info, end=' ')
            q.extend([n.left, n.right])

def levelOrder(root):
    q = deque([root])
    while q:
        n = q.popleft()
        if n:
            print(n.info, end=' ')
            q.extend([n.left, n.right])