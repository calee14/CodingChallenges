'''
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

# My Second Answer NOTE: Had to look at the real answer
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right   

def order_tree(root):
  res = []
  if root:
    res.append(root.val)
    res = res + order_tree(root.left)
    res = res + order_tree(root.right)
  else:
    res.append('-1')
  return res

def serialize(root):
  res = order_tree(root)
  return ' '.join(res)

def deserialize(s):
  tree_list = s.split()
  res = rebuild(tree_list)
  return res

def rebuild(tree_list):
  node = None
  if len(tree_list) != 0:
    value = tree_list.pop(0)
    if value != 1:
      node = Node(value)
      node.left = rebuild(tree_list)
      node.right = rebuild(tree_list)
    else:
      node = Node(None)
  return node


node = Node('root', Node('left', Node('left.left'), Node('left.right')), Node('right'))
print(serialize(node))
print(serialize(deserialize(serialize(node))))
assert deserialize(serialize(node)).left.left.val == 'left.left'