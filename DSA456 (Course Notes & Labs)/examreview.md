## Exam Review Questions

**1.** Given a relatively balanced binary search tree, why is the search() function O(log n)?

```
Solution-1:

In a relatively balanced binary search tree, the search() function = O(log n)
Because at each level of the tree, it eliminates half of the remaining nodes.
The tree's balanced nature ensures a logarithmic search time.
```

**2.** Explain why you need a max_heap (biggest is at root, parent > children) for heap sort that sorts an array in ascending order (small to big)?

```
Solution-2:

For heap sort to sort an array in ascending order using a max_heap,
for that the array is first converted to a max-heap.
Because the largest element (root) is swapped with the last element, and the heap property is then restored.
The process repeats, resulting in ascending order.
Max-heap allows efficient extraction of the maximum element.
```

**3.** If you were to implement a reverse phone directory (You enter a phone number to find a person), what data structure would you use for the table?

```
Solution-3:

A hash table would be suitable for implementing a reverse phone directory.
The phone numbers could be hashed, and the corresponding values would be stored at the hashed index.
```

**4.** Explain why search through a balanced Binary Search tree is O(log n)?

```
Solution-4:

Searching through a balanced Binary Search Tree = O(log n)
Because at each step, it divides the search space in half.
This logarithmic behavior results from the balanced structure of the tree.
```

**5.** Can you binary search a sorted linked list? Explain why or why not?

```
Solution-5:

Binary search cannot be efficiently performed on a sorted linked list.
Binary search relies on random access to elements, which is not possible in a linked list.
The time complexity would decrease to O(n) as you need to traverse the list linearly.
```
**6.** 

Given the following declaration of a binary search tree:
```python
class BST:
	class Node:
		# Node's init function
		def __init__(self, value=None, left=None, right=None):
			self.value = value
			self.left = left
			self.right = right

	#BST's init function
	def __init__(self):
		self.root = None
```
Write the following member function of BST.

```python
def print_between(min, max): 
```
This function prints every value in the tree that is between min and max inclusive. 
Function only visits a subtree where the values may be valid.

```python
# Solution-6:

def print_between(self, min_val, max_val):
    self._print_between(self.root, min_val, max_val)

def _print_between(self, node, min_val, max_val):
    if node is not None:
        if min_val < node.value:
            self._print_between(node.left, min_val, max_val)
        if min_val <= node.value <= max_val:
            print(node.value)
        if node.value < max_val:
            self._print_between(node.right, min_val, max_val)
```

**7.** Given the following declaration of a binary tree:
```python
class BT:
	class Node:
		# Node's init function
		def __init__(self, value=None, left=None, right=None):
			self.value = value
			self.left = left
			self.right = right

	#BT's init function
	def __init__(self):
		self.root = None
```
Write the BT class method:
```python
def height(self):
```
This method returns the height of the binary tree.

```python
# Solution-7:

def height(self):
    return self._height(self.root)

def _height(self, node):
    if node is None:
        return 0
    left_height = self._height(node.left)
    right_height = self._height(node.right)
    return max(left_height, right_height) + 1
```

**8.** Draw 7 circles and label them A, B, C, D, E, F, G.  Draw random arrows between these circles.  This will form a graph.
  * draw out the adjacency matrix and the adjacency list that corresponds to the graph

```
Solution-8:

--Adjacency Matrix
      A B C D E F G
    A 0 1 0 0 1 0 0
    B 1 0 1 0 0 1 1
    C 0 1 0 0 0 1 0
    D 0 0 0 0 1 0 0
    E 1 0 0 1 0 0 1
    F 0 1 1 0 0 0 0
    G 0 1 0 0 1 0 0

-- Adjacency List
A: [B, E]
B: [A, C, F, G]
C: [B, F]
D: [E]
E: [A, D, G]
F: [B, C]
G: [B, E]
```

**8b.** Add some weights to your graph.  Using Dijkstra's algorithm, find the shortest path from A to every other node.

```
Solution-8(B):

A: 0
B: 1
C: 2
D: 5
E: 1
F: 3
G: 3
```

**9.** Draw a binary tree with at least 20 nodes and put in some random labels (numbers, letters, doesn't really matter as long as they are unique).

Base on this tree:

  * list the leaf nodes
  * list the root node
  * list the nodes in a preorder, postorder, inorder, breadthfirst manner
  * height of the tree
  * depth of all leaf nodes

```
Solution-9:

Leaf nodes: 10, 25, 35, 45, 62, 80

Root node: 80

Preorder: 80, 70, 60, 50, 40, 30, 20, 65, 62, 10, 25, 21, 22

Postorder: 22, 21, 25, 10, 30, 40, 50, 62, 65, 20, 60, 70, 80

Inorder: 10, 20, 21, 22, 25, 30, 40, 50, 60, 62, 65, 70, 80

Breadthfirst: 80, 70, 60, 65, 50, 30, 40, 62, 10, 25, 21, 22, 20

Height: 4

Depth of leaf nodes:

10: 3
25: 3
35: 2
45: 2
62: 2
80: 1
```

**10.** Create a BST tree by adding the following numbers to these trees in the order given as:

80, 70, 60, 50, 40, 30, 20, 10, 35, 45, 43

Draw the result of each tree after an insertion.

```
Solution-10:

      80
     /  \
    70   85
   / \   / \
  60 75 80  90
 / \
50  65
     \
     75
```

**10b.** Remove these numbers from the tree formed in 10 in the order given as: 

10, 70, 40 

Draw the result of each tree after a value is removed

```
Solution-10(B):
After Removal 10-
    80
   /  \
  70   85
 / \   / \
60 75 80  90

```

**11.**

Create a min heap (smaller value, higher priority) by inserting these values in order given: 

40, 30, 10, 60, 50, 70, 20, 35, 65, 5, 7, 22, 15
Draw the result of each the tree after each insertion.

**11b.** 

perform remove() 3 times from your heap in 11 and draw the results.

**12.**

Create an AVL tree by adding the following numbers to these trees in order given as:

80, 70, 60, 50, 40, 30, 20, 10, 35, 45, 43

Draw the result of each the tree after each insertion.

**13.**

Create a Red-Black tree by adding the following numbers to these trees in order given as:

10, 20, 30, 40, 50, 60, 70, 80, 46, 56, 44, 48, 49

Draw the result of each the tree after each insertion.

**14.**

Create a 2-3 tree by adding the following numbers to these trees in order given as:

80, 70, 60, 50, 40, 30, 20, 65, 62, 10, 25, 21, 22

Draw the result of each the tree after each insertion.
 
**15.**

Suppose you are given the list: [15, 12, 14, 11, 10, 9, 7, 5, 2, 1].  
Draw the complete binary tree associated with the list. 

**15b.**

Make heap in place using the heapify algorithm on the list in part 13a to form a **min-heap**.  Draw the final heap and state the final list created from the heapify routine.  

**16.**

Given the following BST class declaration

```python
class BST:
	class Node:
		# Node's init function
		def __init__(self, value=None, left=None, right=None):
			self.value = value
			self.left = left
			self.right = right

	#BST's init function
	def __init__(self):
		self.root = None
```

Write the BST class method:
```python
def inorder_successor(self, value):
```
This method returns the inorder successor of value. If there are no nodes with this value in the BST, or the node containing this value does not have an inorder succesor, this method should return None.

**17.**

Is it possible to write a program that can check for infinite loops?
