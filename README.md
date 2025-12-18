# DSA-LRU-Cache-
 LRU Cache Implementation in Python
 Overview
This project implements an LRU (Least Recently Used) Cache from scratch using core data structures.
The cache supports get and put operations in O(1) time complexity.
This design closely follows how real-world cache systems work and is commonly asked in technical interviews.
 Features
Fixed capacity cache
get(key) → retrieves value if present, else -1
put(key, value) → inserts or updates key
Automatically evicts least recently used item when capacity is exceeded
Console-based interaction
 Data Structures Used
Data Structure	Purpose
HashMap (dict)	Fast key → node lookup (O(1))
Doubly Linked List	Track usage order
Custom Node Class	Store key-value pairs
 Design Explanation
 Doubly Linked List
Most Recently Used (MRU) → near head
Least Recently Used (LRU) → near tail
Enables O(1) insertion and deletion
 HashMap
Maps keys to linked list nodes
Allows constant-time access
⚡ Why O(1)?
HashMap lookup → O(1)
Doubly linked list removal/addition → O(1)
