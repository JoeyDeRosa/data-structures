# data-structures

This repository contains sample code for several classic data structures in Python.

## Linked List:
A singly-linked list containing nodes that all stem from the head.
methods:
- push(val)
    adds a node containing val to the head of the list.
- pop()
    removes the node at the head of the list and returns the value.
- size()
    returns the number of nodes on the stack.
- search(val)
    returns the closest node to the head of the list that contains val.
- remove(node)
    removes node from the list.
- display()
    returns a string displaying the contents of the list in the format of a tuple.

## Stack (composed from linked list):
A data structure with basic first-in: first-out functionality
methods:
- push(val)
    adds a node containing val to the top of the stack
- pop()
    removes and returns the value at the top of the stack

## Double Linked List:
A doubly-linked list containing nodes that point to the nodes before and after them.
methods:
- push(val)
    adds a node containing val to the head of the list.
- append(val)
    adds a node containing val to the tail of the list.
- pop()
    removes the node at the head of the list and returns the value.
- shift()
    removes the node at the tail of the list and returns the value.
- search(val)
    returns the closest node to the head of the list that contains val.
- remove(val)
    removes the node containing val closest to the head from the list.
Use-cases:
        A double-linked list would be more appropriate than a single-linked list if the list was bing used
    as a way to store and retrieve data. In that use-case the abiliry to navigate up and down the list in order to find data would be necessary. A single-linked list would be more appropriate than a double-linked list if the user was intnded to only have one chance to access the node and then move on. A use-case like this would probably be simmilar to an online test where the user couldn't change answers once they had been submited.

## Queue:
A queue containing nodes that can be added to the end of the list and removed from the front.
methods:
- enqueue(val)
    add a node containing val to the end of the que.
- dequeue()
    removes a node from the front of the queue and return the value.
- size()
    returns the number of nodes in the queue.
- peek()
    returns the value of the head withoud dequeueing it.

Developed by Avery Pratt, Patrick Saunders, and Joey DeRosa