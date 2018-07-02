from Node import Node

head = None
for count in range(1,6):
    head = Node(count, head)

#Traverse
probe = head
while probe!=None:
    print(probe.data)
    probe = probe.next


# Search

probe = head
targetItem = int(input("Input item to search"))
while probe!=None and targetItem!=probe.data:
    probe=probe.next
if probe!=None:
    print("Target has been found")
else:
    print("Target is not in the lined structure")


# Search a specific index item
probe = head
index = int(input("Input index: "))
while index>0:
    probe = probe.next
    index-=1
print(probe.data)


# Inserting at the End
newNode = Node("A")
if(head is None):
    head = newNode
else:
    probe = head
    while probe.next!=None:
        probe = probe.next
    probe.next = newNode

probe = head
while probe!= None:
    print(probe.data)
    probe = probe.next

# Removing at the end
removedItem = head.data
if head.next is None:
    head = None
else: 
    probe = head
    while probe.next.next!=None:
        probe = probe.next
    removedItem = probe.next.data
    probe.next = None
    