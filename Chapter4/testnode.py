from Node import Node

"""
node1 = None
node2 = Node("A",None)
node3 = Node("B", node2)
print(node3.next.data)
node1 = Node("C",node3)
node = node1


while node!=None:
    print(node.data)
    node = node.next
"""

head = None
for count in range(1,6):
    head = Node(count, head)

#Print the contents of the structure
while head != None:
    print(head.data)
    head = head.next