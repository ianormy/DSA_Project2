"""
Blockchain

A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and
how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the
previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the
Greenwich Mean Time when the block was created, and text strings as the data.
"""
import unittest
import hashlib
import time


class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return
        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


class Block:
    def __init__(self, timestamp, data, previous_hash):
        if timestamp is None:
            raise ValueError("timestamp cannot be None")
        if data is None:
            raise ValueError("data cannot be None")
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        time_str = time.strftime('', self.timestamp)
        hash_str = '{}{}{}'.format(time_str, self.data, self.previous_hash).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChainTestCase(unittest.TestCase):
    def test_blockchain(self):
        block_chain = DoublyLinkedList()
        gmt = time.gmtime()
        head = Block(gmt, "first_block", None)
        block_chain.append(head)
        block1 = Block(gmt, "second_block", head.hash)
        block_chain.append(block1)
        block2 = Block(gmt, "third_block", block1.hash)
        block_chain.append(block2)

    def test_invalid_block_timestamp(self):
        with self.assertRaises(ValueError):
            Block(None, "test data", None)

    def test_invalid_block_data(self):
        with self.assertRaises(ValueError):
            Block(time.gmtime(), None, None)


if __name__ == '__main__':
    unittest.main()
