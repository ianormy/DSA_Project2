# Find Files
I have implemented this as a recursive function.

## Time Complexity
* calling os.listdir() - O(n)
* searching for folders - O(n)
* finding the .c files and adding them to the list - O(n)

Total time: O(n * 3) = O(n). 

## Space Analysis
In the worst case you will find **n** items and return them as a list.

Total space: O(n)
