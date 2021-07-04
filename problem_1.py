"""
Least Recently Used Cache

An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches
its limit. For the current problem, consider both get and set operations as a use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full,
you must write code that removes the least recently used entry first and then inserts the element.
All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.
"""
import unittest


class DoubleNode:
    def __init__(self, key, value):
        """Node stores not just a value but also the corresponding key

        Args:
            key: key to store
            value: value to store
        """
        self.value = value
        self.key = key
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def remove_node(self, node):
        """Remove an existing node from the linked list

        Args:
            node (DoubleNode): the node to remove
        """
        previous = node.previous
        next = node.next
        if self.tail is node:
            self.tail = previous
        if self.head is node:
            self.head = next
        if previous:
            previous.next = next
        if next:
            next.previous = previous

    def prepend(self, key, value):
        """ Prepend a key and value to the beginning of the list

        Args:
            key: they key to use
            value: the value to use
        """
        if self.head is None:
            self.head = DoubleNode(key, value)
            self.tail = self.head
            return
        new_head = DoubleNode(key, value)
        self.prepend_node(new_head)

    def prepend_node(self, node):
        """ Prepend a node to the beginning of the list

        Args:
            node (DoubleNode): the node to prepend to the beginning of the list
        """
        self.head.previous = node
        node.next = self.head
        self.head = node

    def to_list(self):
        """Return a list of the values in the linked list

        Returns:
            list of values
        """
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


class LRU_Cache(object):
    def __init__(self, capacity):
        """Initialise the class

        Args:
            capacity (int): the size of the cache. Must be less than 2**16 (65,536)
        """
        max_capacity = 2**16
        if capacity >= max_capacity:
            raise ValueError("capacity must be less than {}".format(max_capacity))
        self.capacity = capacity
        self.hash_map = {}
        self.access_list = DoublyLinkedList()
        self.cache_size = 0

    def get(self, key):
        """Retrieve an item using the provided key

        Args:
            key: key to use to lookup the value
        Returns:
            -1 if the key isn't in the cache, otherwise returns the value for the given key.
        """
        if key not in self.hash_map:
            return -1
        node = self.hash_map[key]
        # move this item to the top of the access list
        self.move_node_to_head(node)
        return node.value

    def move_node_to_head(self, node):
        """move the node to the head

        Args:
            node (DoubleNode): the node to move to the head of the list
        """
        self.access_list.remove_node(node)
        self.access_list.prepend_node(node)

    def set(self, key, value):
        """Set the value in the cache.

         If the key is not present in the cache it creates it.
         If the cache is at capacity it removes the oldest item.

         Args:
             key: key to use (cannot be None)
             value: value to use (cannot be None)
         """
        if key is None:
            raise ValueError("key value cannot be None")
        if value is None:
            raise ValueError("value cannot be None")
        if key in self.hash_map:
            # move it to the top of the access list?
            node = self.hash_map[key]
            node.value = value
            self.move_node_to_head(node)
            return
        if self.cache_size == self.capacity:
            # remove the least recently used entry - i.e. the one at the tail
            node = self.access_list.tail
            self.hash_map.pop(node.key)
            self.access_list.remove_node(node)
        # add the value to the head
        self.access_list.prepend(key, value)
        self.hash_map[key] = self.access_list.head
        self.cache_size += 1


class LRUCacheTestCase(unittest.TestCase):
    def test_invalid_key(self):
        our_cache = LRU_Cache(5)
        with self.assertRaises(ValueError):
            our_cache.set(None, 23)

    def test_invalid_data(self):
        our_cache = LRU_Cache(5)
        with self.assertRaises(ValueError):
            our_cache.set(22, None)

    def test_invalid_capacity(self):
        with self.assertRaises(ValueError):
            our_cache = LRU_Cache(2 ** 17)

    def test_valid_data(self):
        our_cache = LRU_Cache(5)
        our_cache.set(1, 1)
        print('cache recently used list: {}'.format(our_cache.access_list.to_list()))
        # cache recently used list: [1]
        our_cache.set(2, 2)
        print('cache recently used list: {}'.format(our_cache.access_list.to_list()))
        # cache recently used list: [2, 1]
        our_cache.set(3, 3)
        print('cache recently used list: {}'.format(our_cache.access_list.to_list()))
        # cache recently used list: [3, 2, 1]
        our_cache.set(4, 4)
        print('cache recently used list: {}'.format(our_cache.access_list.to_list()))
        # cache recently used list: [4, 3, 2, 1]
        self.assertEqual(our_cache.get(1), 1)
        print('cache recently used list: {}'.format(our_cache.access_list.to_list()))
        # cache recently used list: [1, 4, 3, 2]
        self.assertEqual(our_cache.get(2), 2)
        print('cache recently used list: {}'.format(our_cache.access_list.to_list()))
        # cache recently used list: [2, 1, 4, 3]
        self.assertEqual(our_cache.get(9), -1)  # 9 is not present in the cache
        our_cache.set(5, 5)
        print('cache recently used list: {}'.format(our_cache.access_list.to_list()))
        # cache recently used list: [5, 2, 1, 4, 3]
        our_cache.set(6, 6)
        print('cache recently used list: {}'.format(our_cache.access_list.to_list()))
        # cache recently used list: [6, 5, 2, 1, 4]
        self.assertEqual(our_cache.get(3), -1)  # the cache reached it's capacity and 3 was the least recently used entry


if __name__ == '__main__':
    unittest.main()
