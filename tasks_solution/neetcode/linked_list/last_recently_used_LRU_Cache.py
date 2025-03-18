# implement last resiliently used (LRU) cache
#  get and put should have O(1) time complexity
#
# Input:
# ["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]
# Output:
# [null, null, 10, null, null, 20, -1]
#
# Explanation:
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 10);  // cache: {1=10}
# lRUCache.get(1);      // return 10
# lRUCache.put(2, 20);  // cache: {1=10, 2=20}
# lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
# lRUCache.get(2);      // returns 20
# lRUCache.get(1);      // return -1 (not found)


class Node:
    def __init__(self,key, val,):
        self.val = val
        self.key = key
        self.previous = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity # how much we store
        self.cache = {}          # where we store

        # add base object for left right linked list
        self.left = Node(0,0) # dummy head nod
        self.right = Node(0,0)# dummy tail node

        # made a references between objects left_obj <-> right_obj
        self.left.next = self.right
        self.right.previous = self.left


        # insert to head of the linked list
    def insert(self,node):
        node.previous = self.left # add dummy head to previous pointer
        node.next = self.left.next # add second node to next pointer
        self.left.next.previous = node #  link second node previous pointer to new head node
        self.left.next = node  # add to dummy head next pointer


        # obj1 <-> obj2 <-> obj1
    def remove(self, node):
        previous_reference = node.previous
        previous_reference.next = node.next # new for  next pointer  obj1 -> obj3
        next_reference = node.next
        next_reference.previous = node.previous  # new for previous pointer obj1 <- obj3
        node.next, node.previous = None, None # clean pointer for deleted node


    def put(self, key: int, value: int)-> None:
        if key in self.cache:
            # if key in cache the remove node
            self.remove(self.cache[key])
        # if key not in cache the add node to cache
        self.cache[key] = Node(key, value)
        # and add node to linked list
        self.insert(self.cache[key])

        # if capacity is over lowed then remove last recently used node
        if len(self.cache) > self.capacity:
            last_recently_used_node = self.left.next
            self.remove(last_recently_used_node)
            del self.cache[last_recently_used_node.key]


    def get(self, key):
        if key in self.cache:
            # remove node from the linked list
            self.remove(self.cache[key])
            # add the same node to the front of linked list (to the head)
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1




