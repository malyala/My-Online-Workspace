This document explains the implementation of 
	1) the BinaryTree class
	2) the 20 questions game

1) For the BinaryTree class, we explain:
	a) init
		We initialize a tree with one value and None values for
		its parent and children all stored with instance variables
	b) adding kids
		To add a child we take in a value. Create a new tree with the child's
		value and assign the appropriate instance variable of self to that new tree.
		We essentially modify the existing tree object 'self'.
	c) getting BinaryTree objects- children
		We simply use . notation to access the right instance variable.
	d) getting a value
		same as c) (access self.value)
	e) checking for a leaf
		Since python represents all but None values as true in bool(value)
		we can return the negation of either child being non-None 
		(which is the same as having a None child and a None child
		or not False and not False).
	d) checking equality
		To do this we just use basic recursion and a subtlty. If 
		we have two leaves, we simply compare their values.
		Otherwise, we can check if in addition to the two trees
		having the same value, whether the children have the same value.
		If there is only one pair of children (like both lefts or rights)
		then the None== None will return true in python. Otherwise, 
		an error will result from one node having a l/r child 
		and another node not having a l/r child. Because we know
		an error implies unequal trees (which is explained in 
		the comments of this function as well), we can just use try-except and
		return false in the except. 
	e) making repr
		We also use basic recursion. If we have a leaf, we put its value
		converted to a string inside {}.
		Otherwise we represent a tree as (parents_value, repr of left_tree, repr of right_tree)
		but of course in a string form. The printing of the left and right trees are recursive calls
		in imperative style. If there is only one child, the other child is 
		a '' so we could have (parent_value,repr of left_tree,)
		


2) For the 20 questions game, we explain: 
	a) A single run of the game (the function game())
		there are lots of comments in this; the basic idea
		is to keep asking a question in a node while
		it is not a guess- a leaf. When it is not a leaf
		based on the answer to the question, the current node becomes the previous node's
		left or right kid
		
		In the end, we wither brag or update our tree as such.
	b) Repeated runs of a game where an added animal is part of the new round (play4eva())
		In the case where we want a tree that grows, we keep playing the game in a loop 
		and keep asking the user after each game if he or she wants to stop.
		
		(I could have written to a file, but I would need to learn how to do that first.)













