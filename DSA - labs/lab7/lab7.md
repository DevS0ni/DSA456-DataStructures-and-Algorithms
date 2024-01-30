# Lab 7

* Dev Soni - 130759210

## Part A: BST Insert

As a group review bst insertion algorithm.

* Take one photo of the original row of sticky notes
![lab7-1](https://github.com/seneca-dsa456-f23/labs-dasoni4/assets/88739819/45431ffd-b53f-4c16-9525-bdfa09f381f4)

* When completed, take one photo of the final tree
![lab7-2](https://github.com/seneca-dsa456-f23/labs-dasoni4/assets/88739819/7a46b0c0-0c1d-46d8-bd99-7d6f5db63c58)

Answer this question.

* What is the height of your final tree?
```
The height of the tree is 6. This is because we would count the leaf nodes starting from 1 and continue
with each level going upwards. Therefore, the total number of nodes from root to furthest leaf is what
would be counted as the height.
```

## PART B: BST Deletion

* Find a node in your tree with 2 children and remove that node.
	* Take a picture of tree
![lab7-3](https://github.com/seneca-dsa456-f23/labs-dasoni4/assets/88739819/ac91473a-4876-424d-99e5-ef3f7daf7c9b)

* find another node with 2 children and remove that node
	* Take picture of tree
![lab7-4](https://github.com/seneca-dsa456-f23/labs-dasoni4/assets/88739819/138ba1b4-4798-4476-a1ad-1f875d42742b)

* remove the root node of the tree
	* take picture of tree
![lab7-5](https://github.com/seneca-dsa456-f23/labs-dasoni4/assets/88739819/ceec7219-346b-4bbd-826c-258f76efdff2)

Answer this question:

* Anytime you remove a node with 2 children, you need to find a node to take over for node being removed.  Explain how you found your replacement.
```
When a node with 2 children needs to be removed from the tree it will take the left side of the node and move it forward.
When removing the number 19 then it has to be removed with 12 because 12 it bigger number than 9, thats why, it would go
as the parent node for that subtree section. Afterwards, while removing 91, the number 82 would go upwards to take it's place because it is
on the left side of the tree and that is the rule to take the left side of the node. Finally, removing the root of the tree was
again replaced by the left side of the tree and therefore, leaving the root with the number 2. The idea from my understanding
is we are going to look at the left side until there is no more left since it is the smallest value typically and then take the
inorder successor to replace the node we are removing which is what we have done in our tree shown above.
```

## Part C AVL



* Take one photo of the original row of sticky notes
![lab7-6](https://github.com/seneca-dsa456-f23/labs-dasoni4/assets/88739819/81fd029a-9d6c-428e-86a4-d4eb3d470cbf)

* When completed, take one photo of the final tree
![lab7-7](https://github.com/seneca-dsa456-f23/labs-dasoni4/assets/88739819/5cdf142d-86bf-4f8e-a85a-c6ddea59f12c)

Answer these questions. 
* How many times you had to do a single rotation?
```
There were  in total 4 single rotations completed during this AVL tree exercise. The first single rotation that
occured in the tree was after adding 12 and then 53, since they all fell on the right side, it did a single
rotation to the left to balance the numbers. The second single rotation right occured on the left side of the subtree when
adding the value 2 which went down and 5 came up to balance the tree. Afterwards, adding the value 100 to the
bottom right node, there was a single rotation left, making the root value 55. Finally, another single rotation
when adding the last value 22 to the bottom of the tree, then leading 21 to go upwards. From my understanding
a single rotation occurs when the tree is not height balanced so it would need to be rotated to balance the
numbers in the tree.
```
* How many times you had to do a double rotation?
```
There were 3 double rotations that occured during this AVL tree exercise. The first double rotation occured
after adding the value 82 to the tree, a double rotation to the right would occur which then brought 55 down
and 82 up. The second double rotation was after adding the number 73 there was a double rotation left because
it was then inbalanced on the right and left side so it would bring up 73 to be the child of 82 and the sibling
of 91. Finally, when adding the number 38 to the tree it would bring it higher in the tree and 19 down in the
double rotation.
```
* How tall is your final tree?
```
Our tree has 5 levels.
Level 1 - (left to right) which has all the child nodes: 2, 9, 19, 22, 44, 73, 100.
Level 2 - which is the parents of those children: 5, 21, 53, 91. Level 3: 38, 82.
Level 4: - 12.
Level 5 - the root value: 55. 
```

## Part D Red-black trees (optional)
*--NOTE: This part D is optional so not attempting this*

* Take one photo of the original row of sticky notes

* When completed, take one photo of the final tree

* how many times did you perform a colour swap, zig-zig and zig-zag rotation?

## Part E 2-3 trees


* Take one photo of the original row of sticky notes
![lab7-8](https://github.com/seneca-dsa456-f23/labs-dasoni4/assets/88739819/91a3156a-7c25-4ee6-ac3b-d5b9ae0e8183)

* When completed, take one photo of the final tree
![lab7-9](https://github.com/seneca-dsa456-f23/labs-dasoni4/assets/88739819/2a314248-8479-4238-8e6b-e12e164f195d)

* How many times did you split?
```
This 2-3 tree split 7 times in total. The first split happens after the third number, 21 was added so it will then
split into 2 individual leafs showing as 21 left child node of 44 root and 73 right child leaf. Furthermore,
split happens after adding the number 2 which would go in the same circle as 2 and 21 but once 2 is added
then 9 will go up with 44. This happens because there cannot be more than 2 numbers in a leaf so you would
 take the medium number to the root of the child leafs. The third  time a split happened was with 12, 21, 22
which split with 21 going up to the original root making it 9, 21 & 44. This then spliting the root node again
so 21 is only at the root of the tree since it is considered the medium in that leaf.
Afterwards at last, the diagram follows the similar pattern with the other values 7 times throughout adding a number
to the correct side of the tree based on if it's higher or lower than the parent then being split afterwards.
```
## Part F Dijkstra's Algorithm


![Graph](https://user-images.githubusercontent.com/1699186/203682880-1f8d6068-3668-4b2c-9abe-40cb79294177.png)


Use Dijkstra's algorithm to find the shortest distance from vertex A to every other vertex.  Show your work by creating the table below:

| Vertex | Distance to A | Previous Vertex | Known|
|---|---|---|---|
| A  |  0 | -  |  False |
| B  |  5 | A  |  True  |
| C  |  9 | B  |  True  |
| D  |  11 | C  |  True  |
| E  |  10 | F  |  True  |
| F  |  3 | A  |  True  |
| G  |  13 | D  |  True  |

Result summary: Fill in the final result in this table.  For path list all nodes for example, if you are going from A to B to C to D, then path is A-B-C-D


| Vertex | Path | Distance to A|
|---|---|---|
| A  |  - | 0 |
| B  | A-B | 5 |
| C  | A-B-C | 9 |
| D  | A-B-C-D | 11 |
| E  | A-F-E | 10 |
| F  | A-F | 3 |
| G  | A-B-D-G | 13 |

## Part G: Reflection

This last part is to be completed individually.

Write a short paragraph about what you learned from this lab.

I found the lab pretty interesting, especially as it walked us through different tree types and patterns. Diving into Dijkstra's algorithm was a bit overwhelming at first, but as I looked into how it works, I realized it's not about fixed structures like in regular trees. Instead, it's all about finding the shortest path to a specific goal, like point A. The process of starting with all nodes as 'False' and gradually figuring out their status made more sense as we worked through it as a group.

Working on AVL trees was another eye-opener. While I got the idea of placing smaller numbers on the right and larger ones on the left of a parent node, understanding when to do zig-zag rotations was confusing initially. Practice was key in understanding that AVL trees aim for height balance, not perfect symmetry. The decision to rotate depends on the number of subtrees on each side, and we need to do rotations as we add numbers to keep things balanced.

To sum it up, this lab not only taught me about different tree patterns but also highlighted the importance of hands-on practice in understanding complex algorithmic concepts.

