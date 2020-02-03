import time
import helpers as test

class Node: 
  def __init__(self, key):
    self.key = key
    self.left = None 
    self.right = None 

def insert(root, node):
  if root.key is None:
    root == node 
  else: 
    if node.key < root.key:
      if root.left is None:
        root.left = node 
      else:
        insert(root.left, node)
    else:
      if root.right is None:
        root.right = node 
      else: 
        insert(root.right, node)

def heapify(arr):
  root = Node(arr[0])
  for i in arr[1:]:
    insert(root, Node(i))
  return root

def unsorted(node):
  if node is None:
    return 
  else: 
    print(node.key)
    unsorted(node.left)
    unsorted(node.right)

def sorted(node):
  sa = []
  if node is None:
    return 
  else: 
    sorted(node.left)
    sa.append(node.key)
    sorted(node.right)
  return sa



arr = test.randArr(10000)
start = time.time()
h = heapify(arr)
sa = sorted(h)
end = time.time()
print(end - start)



    
