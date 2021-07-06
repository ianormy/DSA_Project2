# Least Recently Used Cache
I have implemented this using a double-linked list and a hash-map. 
The double-linked list allows me to add elements to the head and remove
elements from the tail in **O(1)** time. The hash-map is used for storing
the key values and reference the corresponding node in the double-linked list.

## Time Analysis
**set value**
* Add to head of double-linked list: O(1)
* Delete from tail if list has got too big: O(1)
* Delete from hash map if list has got too big: O(1)
* Add key/value to hash map: O(1)

Total time: O(1) 

**get value**
* Get value from hash map if in cache: O(1)
* Return -1 if value not in cache: O(1)
* Move accessed node in linked-list to head: O(1)

Total time: O(1)

## Space Analysis
An LRU cache that has **n** items requires a double-linked list of length 
**n** and a hash map of **n** items.

Total space: O(n + n) = O(n)
