# Lab 4

This assessment contains materials that may be subject to copyright and other intellectual property rights. 

Modification, distribution or reposting of this document is strictly prohibited. Learners found reposting this document or its solution anywhere will be subject to the college’s Academic Integrity policy.

**The active part of the lab is done in person in the lab.  You must be there in order to do the lab to get the marks for the lab as it is based on observations of what you did in the lab class. We highly recommend that you skip through its steps in advance, and review the related material before showing up in the in-person lab, such that you can do/complete all the steps in the class.**

## Objectives:

- Learn how sorting works
- Practice communicating and working together as a team.  This is an essential skill for software developers.  Techniques such as [Pair Programming](https://en.wikipedia.org/wiki/Pair_programming#Learning) require you to communicate effectively.


## Setup


All files needed for this lab were created by doing the first task in [lab 0](lab-00.md).  If you didn't do lab 0, do the first task to create your lab repository.


Unless otherwise indicated, all writing goes into lab4.md  

Note that there is nothing to write down until after your lab class.

## Learning to sort:

### Setup

* Your professors will give you a piece of paper with 16 numbers separated by lines.  

* Form teams of 3 students that all have different coloured papers.
	* If the class does not evenly divide, it is ok to have teams of two.  There should be no more than 2 teams of two in the class.

* Fold and tear apart the paper along the lines, forming 16 numbered papers
* each team should get their own table(s) that will allow them the ability to spread out the little pieces of paper in a linear fashion

### The Simple Sorts

* As a group review the algorithms for bubble sort, insertion sort and selection sort
	https://seneca-ictoer.github.io/data-structures-and-algorithms/D-Searching-And-Sorting/simple_sorts

* Assign one of these sort to each team member. (for teams of two work together on the last one)
* Each team member will demonstrate how their assigned sort works using their 16 pieces of numbered paper.
	* lay out all 16 pieces of paper on table in front of you in a row
	* perform the sorting algorithm on the paper to sort them ascendingly
* Help each other out on this, correct misconceptions as you go through the sorts.  This is how it would go if you are programming together... do not assume that the person typing is correct. 
* As a group discuss the following and note it in your lab4.md file
	* which algorithm did you find the easiest to understand?
	* which algorithm seemed to be the fastest for completing the sort?


### Merging lists

For teams of two pick up an extra set of numbers from your prof.  Make sure its different coloured than the ones you have.

#### Merging unsorted lists

* have each member of the group lay out their papers in a row but keep them unsorted... that is you should have 3 rows of 16 number each.  All easily visible but not sorted
* have one member start a timer on one of their devices (phone, computer.. doesn't matter)
* have the other members try to create one new merged list by picking out the smallest values.
* Note the following in your lab4.md file
	* how long did this take
	* did you make any mistakes along the way (did you choose the wrong number and had to move things around)?
		* How many times? 

#### Merging sorted lists

* repeat the above but instead of laying out the papers in 3 unsorted rows, sort each row first.  That is you should have 3 rows of 16 numbers, in sorted order
* repeat this merging and time how long it took.
* Note the following in your 
	* how long did this take
	* did you make any mistakes along the way (did you choose the wrong number and had to move things around)?
		* How many times? 

### Lists Partitioning

For teams of two, use all 3 sets of numbers.

#### Sorting many numbers

* Take all the number papers for your team and mix it up forming a pile of numbered papers
* Have each team member sort all the papers however they like and time the result (mix up the numbers after each round so that everyone starts with randomly ordered values)
* Record how long it took each team member to get them sorted
	* Record the fastest time
	* Describe how the team member sorted them


### Partitioning

* Take all the numbers for your team and mix it up again
* partition the pile:
	* Time how long this process takes
	* have someone pick a random paper to serve as the "pivot" put that paper on table clearly away from pile
	* go through pile and place all numbered papers that are smaller to the left of the pivot, and all bigger to the right of the pivot.  These can still be piled up.
	* repeat one more time with these two smaller piles (unless there were 5 or few papers in the pile, in which case apply the patition only to the bigger half, then out of the two new piles apply the partitioning one more time to the bigger one, if they are about the same, pick any one and do it.)
* If this was correctly done, you should end up with 4 piles of numbers separated by 3 pivots  (it is possilbe to have empty piles.)  This is fine..it means you have one less pile to deal with in the next step.
* Record how long did the partitioning took


### Sorting small piles

* At this point, have the fastest sorter in your team separately sort each of the little piles. 
* By doing this, you should have a fully sorted set of numbers
* Record how long it took to do this


## Come up with the fastest way to sort

* As a team discuss things that helped sort the papers... what was useful? what was fast to do?  What was slow?
* As a team come up with a description of how best to sort a set of numbers on paper.
* Mix up all your numbers and have each member of the team perform the sort you did.  How long did it take?


## Submitting your lab

In order to get a mark for this lab, you must submit:

* lab4.md
* this file should list all your group members
* all the timings
* all observations and discussions

When you are happy with the state of your files, submit a link to your repo's lab4 folder into blackboard.  

Note: Submission of a link to Blackboard is an indication that your lab is ready for grading in the current state.  Do not submit a link until you are ready to be graded.




## Lab Rubric:

| Criteria       | Poor - 0 mark     | Fair - 0.5 marks                                                                                                                     | Good - 1 marks                                                              |
| -------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| Lab Completion | Arrived in class to do lab more than 30 min late or  did not attend | Arrived in class to do lab more than 10 min late but less than 30 min late and/or Missing discussion | Arrived in class within the first 10 min of class and submitted work has a thorough discussion |
