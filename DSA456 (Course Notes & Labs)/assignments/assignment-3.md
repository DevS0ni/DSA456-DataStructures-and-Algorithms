# Assignment 3

### This assignment is worth 8% of your final grade.  

## Assignment Completion

In order to for this assignment to be considered completed you must submit:

* a successful test run of parts A and B through actions (green check mark for both parts in the action tab)
* a video demonstrating your part C

Note: Assignment completion is the minimum requirements for your assignment.  It does not mean you will receive full marks.


## Assignment Objectives:

In this assignment, you will:

* Complete a board game by providing the code for bots
* Add features to the game

NOTE: **as this assignment is about implementing data structures, you are not allowed to make use of any python libraries or use built-in python data structures and functions unless specified.  If you are not sure, please ask your professor.  Any use a built-in libraries or functions without approval will result in having to redo the assignment with a grade penalty of -50%**

## Repository Setup

### Group Creation:

In this assignment you can choose to work in a group of two or three. You have until November 26 to create a team of your choosing. After this date, students not in a team will be teamed up together by their profs. In general we will try not to make adjustments to teams that you put together but there may be situations where we have no other ways of placing every student into a team without making changes to existing teams. Our preference will always be to add someone to a team rather than breaking a team up and thus a three person team is very unlikely to be altered where as a two person team may end up with an additional person (but we will try to avoid this)

**Make sure you are clear how many people you are working with and who they are before using the appropriate link. You will not be able to modify this once you have created the teams. When you create your team, your team name will need to use every member's seneca user name**

If you receive an error message you may have used the same name as your previous assignment, remember to add a3 to the start of your team name so that it will be unique.


* [Repo Creation for teams of 2](repo-creation-g2.md)
* [Repo Creation for teams of 3](repo-creation-g3.md)



## Overview and Rules of the Game

This game is a 2D board game.  Initially player 1 has a gem in the top left corner and player 2 has a gem in the bottom right corner. Players take turns adding one gem per turn to the board.  A gem can be added to any empty square or any square where the player has at least one gem.  If the number of gems in a square reaches the number of neighbours for the cell, the gems overflow into its neighbours, increasing the number of gems and changing the colour of gems to that player's colour (follows the rules of the overflow() function from assignment 1.)

The game ends if every single gem on the board is the same colour.  The player represented by that colour is the winner of the game.

Your repo includes an implementation of the game.  You will need to run this locally as codespaces won't properly support pygames.

To run the game, first download and install pygames:

https://www.pygame.org/wiki/GettingStarted

Then use the command:

```
python game.py
```

The work below is described in 3 parts to better help you divide the work up if you had a group of 3.  Each part should have a main author but others in the group can help with implementation and ideas (especially in part C)

## Part A: A game and some bots (10 marks)

In this part of the assignment you will provide a small modification of the assignment 1 overflow() function and add an evaluation function

### Modifying the overflow() function

Make the following change to the overflow() function from A1.  Doing this is necessary to avoid a stack overflow:

- If the values of every square has the same sign, the overflow() function adds the board to the queue and returns 1.
- Your function will be retested for part A


### Write an Evaluation Function

Write the following function

```python
def evaluate_board(board, player)
```

* **board** - The board is a 2D grid with numbers.
	- 0 indicates that the cell is empty
	- the absolute value of a non-zero number indicates the number pieces in the corresponding cell
	- the sign indicates which player's pieces are in the cell.  Positive numbers are player 1.  Negative numbers are player 2
* **player** - This number is either +1 or -1.  A +1 means we are evaluating the board for player 1.  A -1 indicates the function is evaluating the board for player 2.

Given a board and the player you are evaluating the board for, this function returns a score for the board.  The higher the score, the better it is for the given player.

There is a lot of ways for you to write this function and how good your bot will play the game is partly determined by how good this function is.  Use your imagination on exactly how to write this.  The following are the only criteria that your board will need to meet:

* A win for the player is a loss for the opponent.  Thus if you evaluate the board for p1 and they won, the same board would mean a loss for p2
* A winning board for the player must given a score that is higher than any other score for a non-winning board (can be any state other than a win for the player)
* A losing board for the player must be given a score lower than any other score for a non-losing board (can be any state other than a loss for the player)
* All winning boards for the player must have same score as any other winning board.
* All losing boards for the player must have same score as any other losing boards


## Part B: Implement a Game Tree (10 marks)

A game tree is a data structure that allows you to search through a series of possible next moves players can make in a game.  This data structure allows you to consider not only what you can do but what your opponent can do based on what you did, then you can choose what to do based on what your opponent did and so on...


For games with a small number of possible states, it is possible to generate all possible moves to a terminal state.  That is a state where the game has ended because someone has won or a the game has reached some sort of tied state where no one else can make any more moves.

For example, it is possible to generate all possible states of a game like tic-tac-toe as there are less than 9! = 362880 nodes in a game tree starting from an empty board.  Thus tic-tac-toe is considered to be solved. the computer can always play to a tie game no matter what the opponent does.  If the opponent makes any mistakes, the computer will always win.  

For games that have more possible states (like chess), where it is not possible to generate all moves to a terminal state from the starting position, game trees are typically created to a certain height.  The boards at the leafs are evaluated using an evaluation function that tries to estimate a score for a given board.  A minimax function is then applied to the tree in order to find the best move (see below)


### Game Tree class

#### Nodes

A game tree node has a set of pointers its children node. represents what moves it can make. This Node class must be internal to your GameTree Class

```python
__init__(board,depth, player, tree_height = 4)
```
When a node is instantiated, it is passed 
* a 2D array representing the board for the node, 
* the depth of this node
* the height of the game tree
* the player (1 or -1) the tree is being created for.
This function initializes the node.  Note that what you store in this node may not match what is passed.  You will for example need to store the score of the node (which is determined either by the evaluation function if it is a leaf node or the mini max algorithm if it is an innter node).  You may store the board or you may decide that you don't need it. You will need to store references to its children but how you do that is up to you.. just make sure you can associate the move made (row, col of where piece was added) with the child node.

***

#### GameTree Class

```python
__init__(board, player, tree_height = 4)
```

This function initializes the GameTree Object.  It is passed:

* board - the 2D array representing the board of the game in its current state
* tree_height - the maximum height of the tree to be generated
* player - the player the tree is being created for


The init function will build the game tree to a height of tree_height

In the construction of the game tree, you will create children for each node representing the placement of a piece.  Depending on the level of the node, the player placing the piece will be different.  The root represents the board in the current state, all nodes at level 1 (root's children) represent the placement of the player's piece to the original board. After placing the piece and performing the overflow routine as needed, you will get a new board for each placed piece.  that new board form the boards for the nodes of level 1.  After the player makes a move, the opponent makes a move. Thus, each node in level 2 is formed by the opponent placing a piece onto the board in its parent node.  At level 3, we go back to the player's move and so on.

##### Scoring each node

Your tree will have leaf's due to various conditions:
	a) the board for the node is in a terminal state (someone has won)
	b) the node has reached its maximum depth (tree_height-1).  

For any leaf node, the board is evaluated using the evaluation function.

For any inner node (non-leaf), the minimax algorithm determines the score for the node.

minimax is based on the following:

* You want the best possible board for yourself
* Your opponent wants the worst for you


Thus, if you are making a move, you want the best possible move you can make.  However, if your opponent is making a choice on what move to make, they will want the worst possible move for you. But... then you will want to make the best move out of that... and your opponent will want the worst move for you...

Perhaps this scene from the Princess Bride better describes the situation:

https://www.youtube.com/watch?v=rMz7JBRbmNo


To score an inner node, choose the best or worst score in the children nodes depending on who is making the move. A node at an even level is scored as the max of the children's scores while the node at an odd level is scored as the min of the children's scores.

Since you need to score nodes based result's of children, it is necessary to score the nodes in a depth first manner (ie you can't find the score of a node unless you know the scores of all the children)

You can either create the entire tree, then perform a depth first traversal to score each node, or you can score the nodes as you create the tree.  The choice is yours

***

```python
def get_move(self)
```
This function gets (row,col) which is the position of the choice from the tree.

***

```python
def clear_tree(self)
```
This function destroys the game tree by unlinking all nodes in order to allow the garbage collector to work on clearing the memory.


## Part C: Game Improvements (10 marks)

This part of the assignment is open ended.  There are different features that you can add to make this game better.  Exactly what you implement is up to you!  The only rule is the basic game must remain the same.  Note, the feature added needs to be coding based.. so changing out the artwork for something that looks better is not considered a valid extra feature.  Here are some suggestions to get you started.. but you are free to use your imagination to add more.

* Create an "undo" last move button for any human players (AI bots shouldn't be allowed to undo) as long as they haven't lost.  This undo reverts the game to a state before that human player's last move.
* Add Animations... the gems currently just "appear" when they overflow.. you can animate the movement
* Add UI elements to increase/decrease the smartness of the bots (the taller the game tree the smarter the bot)


This is only a very very limited set of ideas.  You are free to be creative and add others.

If you need a Stack, Dequeue, Queue, HashTable, LinkedList or Graph to implement your idea, you must make use of the data structure you wrote earlier in the class.  If you need other data structures, you can use the built in python ones for this part of the assignment.


This part of the assignment has no testers as we don't know what you will implement.  Thus, aside from pushing an updated version of game.py to the repo, you will need to also provide the following:

* A video with voice over the video must:
	1. demonstrate the feature(s) you added
	2. explain how you implemented the features
	3. especially speak to the data structures you used and how they helped in the implementation.
	4. This video should be around 2 to 3 minutes.  Any video over 5 minutes long will receive a reduced grade.  Be succint in your explanation.

* Submit the video using Seneca's one-drive and share it so that anyone with link can view the video.  Make sure that the access is properly given as an inability to view the video can result in a reduced grade
* Alternative you can can put it on youtube as an unlisted video and submit the link for that.


See rubric for grading

## Part D: Reflection (5 marks):

This component is to be individually written and graded.  Please clearly put your name in the title of your reflection.
Complete this section in the a3.md file, please remember to put your name into the appropriate heading

In your reflection include the following:

1. Please detail what exactly **you** did for the assignment.
2. What was one thing **you** learned when doing this assignment?
3. What was its most challenging aspect and what did **you** do to overcome this challenge?

This answer is not about what your team did as a whole.  It is about what each team member individually contributed.


## Submission:

In order to for this assignment to be considered completed you must have:
* a successful run for parts A and B (green checkmark in action tab for each part)
* video describing what you did for part C
* all files needed to properly run the game.  Note that the way to run the game must stay as 

```
python game.py
```

Please make sure you follow the steps listed below fully

### What/How to submit

A3 uses a number of classes created in a1.  You must include these files in your repo.  Minimally you will need:

* a1_partd.py
* a1_partc.py

For part A and B to be considered completed, you must submit your a3_parta.py, a3_partb.py. Your assignment is not complete unless it passes testing (look in the action tab for) a greencheckmark for assignment 3a and assignment 3b and meet the specifications of the described data structure and algorithm (part A and B are mandatory)


For part C to be considered completed:
* you must submit all code files needed to run your game.  In otherwords, if we clone your repo we can run python game.py and your game will run.


For part D, please complete the reflection for this assignment.  This part is individually done and graded. It is not required but you wil not receive marks for this component if you do not do it.



### Resubmissions

* With the test verification there is very rarely a need to have you resubmit your program.  However, if there are many errors in your program or it misses the point entirely, you may be asked to resubmit your work.  Any work that is resubmitted, will receive a 50% penalty

## Grading Rubrics


### Parts A, B

| Criteria | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|---|
| **Documentation - 20%** - Documentation is about Intention.  "This function is suppose to do" X.  It doesn't state HOW "we loop, then there is an if, then ..." - this is an example of what not to do.  It doesn't repeat code.  For each function ensure that it describe what it does (at a high level), what it accepts as arguments and any sort of restrictions (number must be positive for example) and what the function should return under what condition (returns true if found for example) |Almost no documentation of any type |only a few functions got documented and documentation tends to be code description as opposed to code intention. | many function documentation missing or severe lack of details for function description or documentation is done only at code level (within the code) and not as an overall intention| a few functions documentation missing. or function description comments lack some detail.  Over documentation.  documenting every line of code is not a good... let the code speak | For all functions state what parameters are (and any limitations, what return value is, what it does. |
| **Code Styling - 10%** Consistent styling is key.  This category describes things like indentation, consistent naming strategies, good variable names, not adding public member functions etc. | more than 5 cases of inconsistent or bad styling | 3 to 5 cases of inconsistent  or bad styling | 2 to 3 cases of inconsistent or bad styling functions | 1 case of inconsistent  or bad styling | Consistency is key. same variable name styling (snake_case is standard for python), same data member styling, same curly bracket positioning, correct and consistent indentation, good variable names | 
|**Correctness and Completeness of Code - 35%**.  This category generally describes errors in logic or missing functionality that may occur only in some cases.  This category also includes using things you are not suppose to use or not following specifications correctly | 4 or more errors | 3 errors | 2 errors - using something you are not suppose to use will count as two errors right away as it is a spec violation | 1 errors | all functions completed and correct |
| **Efficiency - 35%** - Anything that is completely off from optimal run time will always count as an instance of inefficiency.. thus if runtime can be O(n) and your code is written to O(n^2). Writing unnecessary code will also be counted as inefficient even if runtime is same.. for example copying array more than 1 time during a grow() operation | 4 or more instance of inefficiency | 3 instance of inefficiency | 2 instance of inefficiency| 1 instance of inefficiency | Function is as efficient as possible |

### Part C Rubric

 Criteria | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|---|
| Part C | The feature presented is unclear as to what it does or how it was implemented... it is unclear if that it even works from video or program does not actually run | There is at least one clear feature presented but the discussion of how it is implemented is unclear or wrong | There is at least one feature that is clearly presented and the explanation about how the feature is implemented at a high level but lacks details OR a demonstration of multiple features with clear explanations that has exceeded the maximum length of 5 minutes | More than one feature is implemented with a good description of the implementation | More than one feature is implemented with an excellent indepth but succinct description of the implementation|

### Reflection Rubric

 Criteria | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|---|
| Reflection | No reflection written | Reflection has no specifics with generic statements that can apply to anything | Reflection lacks depth, only a brief description without any details | Reflection shows some depth with some descriptions.  It does not go far beyond the basic requirements | A clearly written reflection with clear thought that shows depth|









