from linked_list.linked_list import LinkedList

class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self.buckets = size * [None]

    def hash(self, key):
        '''
        Arguments: key
        Returns: Index in the buckets for that key
        '''
        sum = 0
        for idx, ch in enumerate(key):
            if idx % 2 == 0:
                sum += ord(ch) * 7
            else:
                sum += ord(ch) * 11
        return sum * 97 % self.size

    def add(self, key, value):
        '''
        Arguments: key, value
        Returns: nothing
        This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
        Should a given key already exist, replace its value from the value argument given to this method.
        '''
        index = self.hash(key)
        if self.buckets[index]:
            current = self.buckets[index].head
            duplicate = False
            while current:
                if key in current.value:
                    current.value[key] = value
                    duplicate = True
                    break
                current = current.next
            if not duplicate:
                self.buckets[index].insert({key: value})
        else:
            self.buckets[index] = LinkedList()
            self.buckets[index].insert({key: value})

    def get(self, key):
        '''
        Arguments: key
        Returns: Value associated with that key in the table
        '''
        index = self.hash(key)
        if self.buckets[index]:
            current = self.buckets[index].head
            while current:
                if key in current.value:
                    return current.value[key]
                current = current.next
            raise KeyError(f'key {key} does not exist in this hashtable!')
        else:
            raise KeyError(f'key {key} does not exist in this hashtable!')

    def contains(self, key):
        '''
        Arguments: key
        Returns: Boolean, indicating if the key exists in the table already.
        '''
        return key in self.keys()

    def keys(self):
        '''
        Returns: Collection of keys
        '''
        keys = []
        for bucket in self.buckets:
            if bucket:
                current = bucket.head
                while current:
                    for key in current.value:
                        keys.append(key)
                    current = current.next
        return keys
