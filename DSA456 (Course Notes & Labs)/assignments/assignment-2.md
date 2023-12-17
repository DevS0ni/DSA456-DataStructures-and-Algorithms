# Assignment 2

### This assignment is worth 12% of your final grade.

### Assignment Completion

In order for this assignment to be considered complete:

* parts A, B and C must pass testing on github (Green check for each part in action tab)

Note: Assignment completion is the minimum requirement for your assignment to be considered complete.  It does not mean you will receive full marks.

**Assignment completion is mandatory to pass dsa456**


## Assignment Objectives

In this assignment we will:

*  implement a hash table
*  implement a graph
*  implement a heap


NOTE: **as this assignment is about implementing data structures, you are not allowed to make use of any python libraries or use built-in python data structures and functions unless specified.  If you are not sure, please ask your professor.  Any use a built-in libraries or functions without approval will result in having to redo the assignment with a grade penalty of -50%**

## Repo Creation

### Written instructions
In this assignment you can choose to work in a group of two or three.  You have until Nov 6 to create a team of your choosing and create your repo.  After this date, students not in a team will be teamed up together by their profs.  **Working alone is not an option.**  In general we will try not to make adjustments to teams that you put together but there may be situations where we have no other ways of placing every student into a team without making changes to existing teams.  Our preference will always be to add someone to a team rather than breaking a team up and thus a three person team is very unlikely to be altered where as a two person team may end up with an additional person (but we will try to avoid this).

**Make sure you are clear how many people you are working with and who they are before using the appropriate link.  You will not be able to modify this once you have created the teams.  When you create your team, your team name will need to use every member's seneca user name**

If you do not have a team, try to find one by posting to course forums.  Be sure to include which section you are in as you cannot work with people not in your section.

**Make sure you use the correct link below!  It must match your team size.  Individual teams will receive a penalty.  READ The TEAM NAMING DETAILS CAREFULLY!**

* [Repo Creation for teams of 2](repo-creation-g2.md)
* [Repo Creation for teams of 3](repo-creation-g3.md)

Your team will last for only this assignment.  If you decide that you were not able to work together after this assignment, you can find new partners for the other assignments. 

Every member of the team must submit a link to their assignment repo by the repo creation due date.  This means that not only must the repo be created, but every team member must have also joined the correct team.


## Work Divsion

* Every member of the team must contribute to the coding portions (parts A, B, and C) of the assignment.  As there are 3 coding components, we expect each member to be the lead author in one of the 3 sections.  It doesn't mean that other team members can't help ... but the lead should be the main contributer to that part of the assignment.
* Every member is expected to **push their own code**
  * **it is NOT ok to use email or have just one person commit all the code. git/github is a professional tool that employers expect our graduates to know how to use, so learn it now.  If you aren't sure, check out the git tutorial listed in the resources section in course repo.**
* Team members that do not commit code for one of the coding components will not receive any credit for the assignment.  They will be removed from the group and will need to redo the entire assignment with late penalties.

## Part A: Hash Table (15 marks)


In this part of the assignment you will implement a class called HashTable which implements a hash table.  

When doing this portion of the assignment you can use:

* python lists (and functions to manipulate the list) for the main table (but not to handle collisions for a closed addressing implementation)
* python hash() function - don't write your own
* Your linked list from A1 (if you wish to create a chaining hash table)

You may use either chaining or linear probing as your collision resolution method.  The exact method and details of implementation (such as using tombstones or not if you choose linear probing) is up to you.


### Member functions


---

```python
	def __init__(self, capacity=32):
```
The initializer for the table defaults the initial table capacity to 32.  It creates a list with capacity elements all initialized to None.

---


```python
	def insert(self, key, value):
```
This function adds a new key-value pair into the table. If a record with matching key already exists in the table, the function does not add the new key-value pair and returns False. Otherwise, function adds the new key-value pair into the table and returns True.  When an insertion causes the HashTable's load factor to exceed 0.7, the list used to store the table must be resized.  Resizing must still allow every existing record to be found.



---

```python
	def modify(self, key, value):
```
This function modifies an existing key-value pair into the table. If no record with matching key exists in the table, the function does nothing and returns False. Otherwise, function changes the existing value into the one passed into the function and returns True

---

```python
	def remove(self, key):
```

This function removes the key-value pair with the matching key.  If no record with matching key exists in the table, the function does nothing and returns False.  Otherwise, record with matching key is removed and returns True

---

```python
	def search(self, key):
```

This function returns the value of the record with the matching key.  If no reocrd with matching key exists in the table, function returns None

---

```python
	def capacity(self):
```
This function returns the number of spots in the table.  This consists of spots available in the table.  

---

```python
	def __len__(self):
```

This function returns the number of Records stored in the table.

---


## Part B: Graphs (20 marks)

When doing this coding portion of the assignment you can use:
* Python lists (and functions to manipulate the list)
* [Python Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)


A Graph data structure is a data structure used to represent a graph.  
See: https://seneca-ictoer.github.io/data-structures-and-algorithms/G-Graphs/representation

### Graphs

There are two ways to represent a graph.  It is up to you to choose the underlying data structure you will use.  To create an adajacency matrix, use a fixed sized list of fixed sized list (ie a 2D array).  To create an adjacency list use a fixed sized list of linked lists where the second dimension linked lists are initially linked lists from assignment 1.


Your Graph class will have the following member functions:

```python
def __init__(self, number_of_verts)
```
This function creates a Graph object and initializes it to support **number_of_verts** vertices.

---

```python
def add_vertex(self)
```

This function adds an additional vertex to the graph.  (ie your graph now supports one more vertex than it had previously supported)

---

```python
def add_edge(self, from_idx, to_idx, weight=1)
```
* from_idx and to_idx are index values of two vertices
* weight is an optional 3rd value for the weight of the edge with a default weight of 1

If either of the vertices are invalid, or the edge already exists, this function does nothing and returns False.
Otherwise, this function will create a directed edge from the vertex from_idx to the vertex to_idx and return True 


---

```python
def num_edges(self)
```

This function returns the number of edges in the graph.

---

```python
def num_verts(self)
```
This function returns number of vertices in the grpah

---

```python
def has_edge(self, from_idx, to_idx)
```
* from_idx and to_idx are index values of two vertice
* this function returns True if there is an edge from vertex from_idx to vertex to_idx, otherwise it returns False
* if either of the vertices are invalid, function does nothing and returns False

---
```python
def edge_weight(self, from_idx, to_idx)
```
* from_idx and to_idx are index values of two vertice
* if either of the vertices are invalid, function does nothing and returns None
* if there is no edge from vertex from_idx to vertex to_idx function returns None
* Otherwise this function returns the weight for the edge from vertex from_idx to vertex to_idx

---
```python
def get_connected(self, v)
```
Finds all the vertices connected from v. That is all vertices that can be reached with a direct link starting from v.  This function returns an array of tuples where the first value of the tuple is the index of the vertex and the second value is the weight of the edge to that vertex.


---

### A Labeled Graph 

When doing this coding portion of the assignment you can use:
* Python lists (and functions to manipulate the list)
* [Python Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
* Any class you wrote for assignment 1 and assignment 2


Your LabelGraph class will have the following member functions:

```python
def __init__(self, vertex_list)
```
This function creates a LabelGraph object with an initial list of vertices named according to the values in vertex_list.  All vertices are not connected.

---

```python
def add_vertex(self, vertex_name)
```

This function adds an additional vertex to the graph with name vertex_name.

---

```python
def add_edge(self, from_vertex, to_vertex, weight=1)
```
* from_vertex and to_vertex are the names of the two vertices
* weight is an optional 3rd value for the weight of the edge with a default weight of 1

If either of the vertices are invalid, or the edge already exists, this function does nothing and returns False.
Otherwise, this function will create a directed edge from the vertex from_vertex to the vertex to_vertex and return True 


---

```python
def num_edges(self)
```

This function returns the number of edges in the graph.

---

```python
def num_verts(self)
```
This function returns number of vertices in the grpah

---

```python
def get_verts(self)
```
This function returns list of vertex names

---

```python
def has_edge(self, from_vertex, to_vertex)
```
* from_vertex and to_vertex are the names of the two vertices
* this function returns True if there is an edge from vertex from_vertex to vertex to_vertex, otherwise it returns False
* if either of the vertices are invalid, function does nothing and returns False

---
```python
def edge_weight(self, from_vertex, to_vertex)
```
* from_vertex and to_vertex are the names of the two vertices
* if either of the vertices are invalid, function does nothing and returns None
* if there is no edge from vertex from_vertex to vertex to_vertex function returns None
* Otherwise this function returns the weight for the edge from vertex from_vertex to vertex to_vertex

---
```python
def get_connected(self, from_vertex)
```
* from_vertex is the name of the initial vertex
This function finds all the vertices that can be reached with a direct link starting at from_vertex.  This function returns an array of tuples where the first value of the tuple is the name of the vertex connected to from_vertex and the second value is the weight of the edge to that vertex.


## Part C: Heap (15 marks)
Create a class that will implement a MinHeap.  A MinHeap has the following member functions:

```python
def __init__(self, arr = [])
```
When a MinHeap is instantiated, it is passed a python list that may be empty.  You may assume that any values in the list are comparable using comparison operators such as <, <=, >=, >, == and !=.   This initializer will initialize a heap using this array.


***

```python
def insert(self, element)
```
This function adds element to the MinHeap

***

```python
def get_min(self)
```
This function returns smallest value in the MinHeap without altering the data structure

***
```python
def extract_min(self)
```

This function removes the smallest value from the MinHeap and returns that value

***

```python
def is_empty(self):
```
This function returns True if the MinHeap does not have any values in the heap, False otherwise

```python
def __len__(self):
```
This function returns number of values stored in the heap


## Part D: Reflection (5 marks):

This component is to be individually written and graded.  Please clearly put your name in the title of your reflection.
Complete this section in the a2.md file, please remember to put your name into the appropriate heading

In your reflection include the following:

1. Please detail what exactly **you** did for the assignment.
2. What was one thing **you** learned when doing this assignment?
3. What was its most challenging aspect and what did **you** do to overcome this challenge?

This answer is not about what your team did as a whole.  It is about what each team member individually contributed.


## Submission:

In order to for this assignment to be considered completed you must submit:

* a successful run for parts A, B and C(green checks for parts A, B and C in actions)

Please make sure you follow the steps listed below fully

### What/How to submit

for parts A, B and C you must submit the corresponding programming files into your repository.  You will also need to submit the reflections part in the .md file.

### Resubmissions

* With the test verification there is very rarely a need to have you resubmit your program.  However, if there are many errors in your program or it misses the point entirely, you may be asked to resubmit your work.  Any work that is resubmitted, will receive a 50% penalty

## Grading Breaking

### Parts A, B and C

| Criteria | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|---|
| **Documentation - 20%** - Documentation is about Intention.  "This function is suppose to do" X.  It doesn't state HOW "we loop, then there is an if, then ..." - this is an example of what not to do.  It doesn't repeat code.  For each function ensure that it describe what it does (at a high level), what it accepts as arguments and any sort of restrictions (number must be positive for example) and what the function should return under what condition (returns true if found for example) |Almost no documentation of any type |only a few functions got documented and documentation tends to be code description as opposed to code intention. | many function documentation missing or severe lack of details for function description or documentation is done only at code level (within the code) and not as an overall intention| a few functions documentation missing. or function description comments lack some detail.  Over documentation.  documenting every line of code is not a good... let the code speak | For all functions state what parameters are (and any limitations, what return value is, what it does. |
| **Code Styling - 10%** Consistent styling is key.  This category describes things like indentation, consistent naming strategies, good variable names, not adding public member functions etc. | more than 5 cases of inconsistent or bad styling | 3 to 5 cases of inconsistent  or bad styling | 2 to 3 cases of inconsistent or bad styling functions | 1 case of inconsistent  or bad styling | Consistency is key. same variable name styling (snake_case is standard for python), same data member styling, same curly bracket positioning, correct and consistent indentation, good variable names | 
|**Correctness and Completeness of Code - 35%**.  This category generally describes errors in logic or missing functionality that may occur only in some cases.  This category also includes using things you are not suppose to use or not following specifications correctly | 4 or more errors | 3 errors | 2 errors - using something you are not suppose to use will count as two errors right away as it is a spec violation | 1 errors | all functions completed and correct |
| **Efficiency - 35%** - Anything that is completely off from optimal run time will always count as an instance of inefficiency.. thus if runtime can be O(n) and your code is written to O(n^2). Writing unnecessary code will also be counted as inefficient even if runtime is same.. for example copying array more than 1 time during a grow() operation | 4 or more instance of inefficiency | 3 instance of inefficiency | 2 instance of inefficiency| 1 instance of inefficiency | Function is as efficient as possible |

### Reflection Rubric

 Criteria | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|---|
| Reflection | No reflection written | Reflection has no specifics with generic statements that can apply to anything | Reflection lacks depth, only a brief description without any details | Reflection shows some depth with some descriptions.  It does not go far beyond the basic requirements | A clearly written reflection with clear thought that shows depth|
