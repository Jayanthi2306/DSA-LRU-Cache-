# DSA-LRU-Cache-
# LRU Cache System

## Description
This project implements an **LRU (Least Recently Used) Cache** using core data structures.  
The cache stores key-value pairs with a fixed capacity and evicts the least recently accessed item when the capacity is exceeded.

The implementation guarantees **O(1)** time complexity for both retrieval and insertion operations.

---

## Data Structures Used

- Hash Map (Dictionary)
- Doubly Linked List
- Custom Node Class

---

## Features

- Insert key-value pairs into the cache
- Retrieve values in constant time
- Automatic eviction of least recently used items
- Efficient update of recently accessed elements
- Console-based interactive interface

---

## System Design Overview

The cache is implemented using a combination of a hash map and a doubly linked list.

### Hash Map
- Maps keys directly to nodes in the linked list
- Enables constant-time lookup

### Doubly Linked List
- Maintains the access order of cache elements
- Most recently used node is placed near the head
- Least recently used node is placed near the tail

Dummy head and tail nodes are used to simplify insertion and deletion logic.

---

## Operations Supported

- `put(key, value)`  
  Inserts or updates a key in the cache.

- `get(key)`  
  Returns the value if the key exists, otherwise returns `-1`.

- Automatic eviction  
  Removes the least recently used key when capacity is exceeded.

---



