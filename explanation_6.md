# Union and Intersection
I have used a linked list for the union and intersection task.

## Time Analysis
Let m and n denote the number of elements in the first and second
linked lists respectively. 

### Union
To perform the union operation we:
* traverse the first linked list looking for unique values and adding them to 
  the output list  - O(m)
* traverse the second linked list looking for unique values that aren't already
  in the output list and add them to the output list - O(n)
* each addition or lookup of the hash-map takes O(1) time

Total Time Complexity: O(m+n).

### Intersection
To perform the intersection operation we:
* traverse the first linked list storing each unique elements in a Hash-map - O(m)
* traverse the second linked list checking if it is already present in 
  the first linked list's Hash-map and hasn't already been added, 
  then add it to the output linked list - O(n)
* each addition or lookup of the hash-map takes O(1) time.

Total Time Complexity: O(m+n).
