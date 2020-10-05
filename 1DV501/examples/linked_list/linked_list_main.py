import linked_list as ll

# Program starts
head = ll.get_new_head()     # Get hold of empty list

# Add 20 integers and print list content
for i in range(1,21):
    ll.append(head,i)
print( ll.to_string(head) )

# Count
print("Count:",ll.count(head))

# Get
print("get(7):",ll.get(head, 7))

# Contains
print("contains(7): ",ll.contains(head,7))
print("contains(30): ",ll.contains(head,30))

# Remove
print("remove(7): ",ll.remove(head,7))
print( ll.to_string(head) )
print("Count:",ll.count(head))
