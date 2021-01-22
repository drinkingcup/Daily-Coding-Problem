# Daily-Coding-Problem
These solutions are my personal suggestions. If there are ways to make it better/ optimal, do feel free to contact me @ shindosan@gmail.com

_________________________________________________________________________________________________________________________________________________________________________________

Problem 1:
Good morning! Here's your coding interview problem for today.

This problem was asked by Yahoo.

Write an algorithm that computes the reversal of a directed graph. 
For example, if a graph consists of A -> B -> C, it should become A <- B <- C.

<a href="/Solutions/problem_1.txt">Solution</a>
_________________________________________________________________________________________________________________________________________________________________________________

Problem 2:
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.

<a href="/Solutions/problem_2.py">Solution</a>
_________________________________________________________________________________________________________________________________________________________________________________

Problem 3:
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

is_locked, which returns whether the node is locked
lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.

<a href="/Solutions/problem_3.py">Solution</a>
_________________________________________________________________________________________________________________________________________________________________________________

Problem 4:
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}. By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.

<a href="/Solutions/problem_4.py">Solution</a>
_________________________________________________________________________________________________________________________________________________________________________________

Problem 5:
Good morning! Here's your coding interview problem for today.

This problem was asked by Dropbox.

What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?

functions = []

for i in range(10):

    functions.append(lambda : i)

for f in functions:

    print(f())
   
<a href="/Solutions/problem_5.py">Solution</a>
_________________________________________________________________________________________________________________________________________________________________________________

Problem 6:
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Implement a file syncing algorithm for two computers over a low-bandwidth network. What if we know the files in the two computers are mostly the same?

<a href="/Solutions/problem_6.txt">Solution</a>
_________________________________________________________________________________________________________________________________________________________________________________

Problem 7:
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].

_________________________________________________________________________________________________________________________________________________________________________________

Problem 8:
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

_________________________________________________________________________________________________________________________________________________________________________________

Problem 9:
Good morning! Here's your coding interview problem for today.

This problem was asked by Jane Street.

Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.

The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.

_________________________________________________________________________________________________________________________________________________________________________________

Problem 10:
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a binary search tree and a range [a, b] (inclusive), return the sum of the elements of the binary search tree within the range.

For example, given the following tree:

    5
   / \
  3   8
 / \ / \
2  4 6  10
and the range [4, 9], return 23 (5 + 4 + 6 + 8).

_________________________________________________________________________________________________________________________________________________________________________________



