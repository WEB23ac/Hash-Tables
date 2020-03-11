# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f'{self.key} {self.value} {self.next}'


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        # * determine index
        index = self._hash_mod(key)
        current_entry = self.storage[index]

        # * if nothing is at c_e assign it a new LP
        if not current_entry:
            self.storage[index] = LinkedPair(key, value)

        # * insert a new LP w/ the previous entry set to next
        # * if current is not none
        while current_entry:
            if current_entry.key == key:
                current_entry.value = value
                return
            # * if key does not match and there is a next value, assign that to the current_entry
            elif current_entry.next:
                current_entry = current_entry.next
            # * finally, if there is no next, insert the value at c_e.next
            else:
                current_entry.next = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        index = self._hash_mod(key)
        current_entry = self.storage[index]

        if current_entry is None:
            print('Error: Key not found.')
        elif current_entry.key == key and current_entry.next is None:
            self.storage[index] = None

        elif current_entry.key == key and current_entry.next is not None:
            next_index = self._hash_mod(current_entry.next.key)
            self.storage[next_index] = current_entry.next
            current_entry = current_entry.next

        elif current_entry.key != key and current_entry.next is not None:
            left_entry = current_entry
            right_entry = current_entry.next
            while right_entry is not None:
                if right_entry.key == key:
                    left_entry.next = right_entry.next
                    right_entry = None
                    return
                left_entry = right_entry
                right_entry = right_entry.next
            print('Error:Key not found.')

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        current_entry = self.storage[index]
        # * returns none when entry is none --- could be simplified
        if current_entry is None:
            return None
        # * if the entry is not none,
        else:
            # *return the value that matches the key argument
            if current_entry.key == key:
                return current_entry.value
            # * otherwise, iterate through the next items in LinkedPairs and find the matching object
            while current_entry.next is not None:
                current_entry = current_entry.next
                if current_entry.key == key:
                    return current_entry.value
            # * when no match is found, return None
            else:
                return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # * Doubles capacity
        self.capacity *= 2
        # * copies current storage list into old_storage list
        old_storage = self.storage.copy()
        # * resets entries in storage to None
        self.storage = [None] * self.capacity

        # * begins iterating over entries in old_storage list to insert into storage
        for entry in old_storage:
            # * insert entries that are not None
            if entry is not None:
                self.insert(entry.key, entry.value)

            # * Iterate over any next values in LinkedPair and insert
                if entry.next is not None:
                    current_entry = entry.next
                    while current_entry is not None:
                        self.insert(current_entry.key, current_entry.value)
                        current_entry = current_entry.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
