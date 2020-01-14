# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.initial_capacity = capacity
        self.storage = [None] * capacity
        self.items = 0


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

    
    def load_factor(self):
        return self.items / self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        #get index and item
        index = self._hash_mod(key)
        item = LinkedPair(key, value)
        #if key already exist delete to update
        if self.retrieve(key):
            self.remove(key)
        #if value already there add it to the linked list
        if self.storage[index]:
            item.next = self.storage[index]
        #set item node to it
        self.storage[index] = item
        #increase items for load factor
        self.items = self.items + 1
        #if load factor increases past .7 resize
        if self.load_factor() > 0.7:
            self.resize()
            
       



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        if self.retrieve(key) is None:
            return

        #get index
        index = self._hash_mod(key)
        
        #check if item exists
        if self.storage[index]:
            #if first item key match change the value for the next keys value
            item = self.storage[index]
            if item.key == key:
                self.storage[index] = item.next
                self.items = self.items - 1
            else:
                #else loop over the list
                while item.next is not None:
                    # if found set pointer to one node over to remove
                    if item.next.key == key:
                        item.next = item.next.next
                        self.items = self.items - 1
                        break
                    else:
                        item = item.next
        
        if self.load_factor() < 0.2 and self.capacity > self.initial_capacity:
            self.resize()

        

        


            


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        #initialize index as the hashed key
        index = self._hash_mod(key)
        #check if there is a value at that index in storage
        if self.storage[index]:
            #if there is set item to it
            item = self.storage[index]
            #check if the keys match
            if item.key == key:
                #if they do return value
                return item.value
            #else check the linked list
            else:
                #while item.next exists check keys else set item to next
                while item.next is not None:
                    if item.next.key == key:
                        return item.next.value
                    else:
                        item = item.next
        #return none if nothing is found
        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        #initialize a new capacity to work with
        new_capacity = self.capacity
        #if load factor is greater than .7 double capacity
        if self.load_factor() > 0.7:
            new_capacity = new_capacity * 2
        #else if its less than 0.2 and the capacity is greater than initial one, make capicity half
        elif self.load_factor() < 0.2 and self.capacity > self.initial_capacity:
            new_capacity = new_capacity // 2
        #if its still same size dont do anything
        if new_capacity == self.capacity:
            return

        #create a new hashtable
        new_hasttable = HashTable(new_capacity)
        
        #get old hast table into new one
        #loop over the buckets
        for node in self.storage:
            current_node = node
            #loop over each bucket if there is more than one node
            while current_node is not None:
                new_hasttable.insert(current_node.key, current_node.value)
                current_node = current_node.next
        #update the capacity and storage
        self.capacity = new_capacity
        self.storage = new_hasttable.storage



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
