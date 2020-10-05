# A linked list using lists of size 2 as nodes.
# head node looks like [None,next], the last node 
# looks like [value,None], all other nodes look 
# like [value,next] 

# Returns head node to be used in subsequent calls
def get_new_head():
    return [None,None]

# Append value n to the end of the list
def append(head, n):
    node = head
    while node[1] != None: # Find last node
        node = node[1]
    node[1] = [n,None]  # Attach new node

# Returns a string representation of the list content
def to_string(head):
    result = "{ "
    node = head[1]    # Node following head
    while node != None:
        result += str(node[0]) + " "
        node = node[1]
    return result + "}"

# Returns the number of elements stored in list
def count(head):
    c = 0
    node = head[1]
    while node != None:
        c += 1
        node = node[1]
    return c

# Get element at position pos, raise IndexError
# if position pos is out of range
def get(head, pos):
    n = count(head)
    if 0 <= pos < n:
        node = head[1]
        for i in range(pos):
            node = node[1]
        return node[0]
    else:
        msg = f"Index {pos} out valid range [0,{n-1}]"
        raise IndexError(msg)

# Returns True if n is in list, otherwise False
def contains(head, n):
    node = head[1]
    while node != None:
        if node[0] == n:
            return True
        node = node[1]
    return False

# Remove and return element pos
def remove(head, pos):
    n = count(head)
    if 0 <= pos < n:
        # Find node before pos
        node = head[1]
        for i in range(pos-1):
            node = node[1]
        
        #By-pass pos
        delete = node[1]
        node[1] = delete[1]
        return delete[0]
    else:
        msg = f"Index {pos} out valid range [0,{n-1}]"
        raise IndexError(msg)



