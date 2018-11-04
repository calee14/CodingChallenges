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

############################# Answer #############################
class Node(object):
    '''
    Args:
        val(any)
        left(Node)
        right(Node)
    '''
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(tree_node):
    '''
    Use -1 to represent an empty leaf. Use ' ' to sperate different nodes.
    Args:
        tree_root(class Node): the root of the tree
    Returns:
        string: a serialized tree
    '''
    preorder_list = preorder_trav(tree_node)
    return ' '.join(str(x) for x in preorder_list)


def preorder_trav(node):
    '''
    Args:
        node(class Node): a node on which the traverse starts
    Returns:
        list: pre-order traverse
    '''
    tree_list = []
    if node is not None:
        tree_list.append(node.val)
        tree_list.extend(preorder_trav(node.left))
        tree_list.extend(preorder_trav(node.right))

    if node is None:
        tree_list.append('-1')
    return tree_list


def deserialize(tree_string):
    '''
    Args:
        tree_string(string): a serialized tree representation
    Returns:
        class Node: the root of a tree
    '''
    tree_list = tree_string.split(' ')
    tree = rebuild(tree_list)
    return tree


def rebuild(tree_list):
    '''
    Args:
        tree_list: a list of all nodes in a tree
    Returns:
        class Node: the root of a tree
    '''
    if len(tree_list) != 0:     # use == to compare value, 'is' to compare objects
        value = tree_list.pop(0)
        if value != '-1':       # use == or != to compare two strings
            node = Node(value)
            node.left = rebuild(tree_list)
            node.right = rebuild(tree_list)
        else:
            node = Node(None)
    return node
############################# End Of Answer #############################

node = Node('root', Node('left', Node('left.left'), Node('left.right')), Node('right'))
print(serialize(node))
print(serialize(deserialize(serialize(node))))
assert deserialize(serialize(node)).left.left.val == 'left.left'