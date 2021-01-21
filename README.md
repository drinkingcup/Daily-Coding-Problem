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

<a href="/Solutions/problem_6.py">Solution</a>
_________________________________________________________________________________________________________________________________________________________________________________
