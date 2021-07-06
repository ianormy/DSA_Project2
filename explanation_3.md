# Huffman Coding
There are two phases to Huffman encoding:

1. building the Huffman tree (a binary tree)
2. generating the encoded data

I use the Python **heapq** module to implement a minimum priority queue (this
is the default).

# Time Analysis
Let n denote the number of characters in the message.

* build the frequencies for each of the unique characters in the message - O(n)
* build the tree using these frequencies - worst case O(n*log(n))
* generate the encoded data using the tree - worst case O(n)

Total worst case time: O(n * 3) = O(n)

## Space Analysis
In order to encode the tree we will create the tree with O(n log n) nodes and
return a list of O(n) items.

Total space: O(n*log(n))
