# CHapter 4: ARRAYS AND LINKED STRUCTURES
**This chapter talks about data structures in sample code. It is not specific data structure built in Python.**

The two data structures most often used to implement collections in programming languages are *arrays* and *linked structures*

## THE ARRAY DATA STRUCTURE
AN array represents a sequence of items that can be accessed or replaced at given index positions.

*In fact, the data structure underlying a Python list is an array. But array is mor erestrictive. The programmer cannot add or remove positions or make the length of the array larger or smaller. Typically the length or capacity of an array is fixed when it is created.*

### Random Access and Contiguous Memory
Array indexing is a *random access* operation. During random access, the computer obtains the location of the ith item by performing a constant number of steps. Thus ** no matter how large the array, it taks the same amount of time to access the first time as it does to access the last item.**

Because the addresses of the items are in numerical sequence, the address of an array item can be computed by adding two values: the array's *base address* and the item's *offset*. The array's base address is the machine address of the first item, an item's offset is equal to its index. To summarize:
* Fetch the base address of the array's memory block.
* Return the result of adding the index to this address.

This requires that the array be represented in a block of contiguous memory.

### Static Memory and Dynamic Memory
Modern languages provide dynamic arrays. A dynamic array occupies a cntiguous block of memory and supports random access. However, the length of a dynamic array need not be known until runtime. Thus the programmers can specify the length of a dynamic array during instantiation. 

Three ways of adjusting length of an array:
1. Create an array with a reasonable default size at program start-up.
2. When the array cannot hold more data, create a new, larger array and transfer the data items from the old array. 
3. When the array seems to be wasting memory (some data have been removed by the application), decrease its length in a similar manner.

### Physical Size and Logical Size
The **physical size** of an array is its total number of array cells, or the number used to specify its capacity when the array is created. The **logical size** of an array is the number of items in it that should be currently available to the application. 

* if the logical size is 0, the array is empty. That is, the array contains no data items
* Otherwise, at any time, the index of the last item in the array is the logical size minus 1.
* If the logical size equals the physical size, there is no more room for data in the array.

## OPERATIONS ON ARRAYS
### Increasing the Size of an Array
1. Create anew, larger array.
2. Copy the data from the old array to the new array.
3. Reset the old array variable to the new array object. 

The overall time performance for adding n items to an array is 1+2+3+...+n or O(n^2)

Yu can achieve more reasonable time performance by doubling the size of the array each time you increase its size. The gain in time performance is achieved at the cost of wasting some memory.

### Decreasing the Size of an Array
Steps:
1. Create a new, smaller array.
2. Copy the data fromt he old array to the new array.
3. Reset the old array variable to the new array object.

### Inserting an item into an Array That Grows
1. Chekc for available space before attempting an insertion and increase the physical size of the array, if necessary, as described earlier.
2. Shift the items from the logical end of the array to the target index position down by one. This process opens a hole for the new item at the target index.
3. Assign the new item to the target index position
4. Increment the logical size by one.

The time performance for shifting items during an insertion is linear on the average, so the insertion operation is linear

### Removing an item from an array
Removing an item from an array inverts the process of inserting an item into the array.
1. Shift the tiems from the one following the target index position to the logical end of the array up by one. This process closes the hole left by the removed item at the target index.
2. Decrement the logical size by one.
3. Check for wasted space and decrease the physical size of the array if necessary.

### Complexity Trade-Off: Time, Space, and Arrays
Table: The Running Times of Array Operations

|Operation|Running Time|
|:---|:---|
|Access at *i*th position|O(1), best and worst cases|
|Replacement at *i*th position|O(1), best and worst cases|
|Insert at logical end|O(1), average case|
|Remove from logicla end|O(1), average case|
|Insert at *i*th position|O(n), average case|
|Remove from *i*th position|O(n), average case|
|Increase capacity|O(n), best and worst cases|
|Decrease capacity|O(n), best and worst cases|

## TWO-DIMENSIONAL ARRAYS(GRID)
### Processing a Grid
### Ragged Grids and Multidimensional Arrays

## LINKED STRUCURES
After arrays, linked structures are probably the most commonly used data structures. A linked structure is a concrete data type that implements many types of collections, including lists. 

### Singly Linked Structures and Doubly Linked Structures
A linked structure consists of items that are linked to other items. THe two simplest linked structures are the *singly linked structure* and the *doubly linked structure*.

A user of a singly linked structure access the first item by following a single external **head link**. The user then access other items by chaining through the single links that emanate from the items. Thus, in a singly linked structure, **it is easy to get to the successor of an item, but not so easy to get to the predeccessor of an item.**

A doubly linked structure contains links running in both directions. Thus, it is easy for the user to mvoe to an items's successor or to its predecessor. A second externla link called the **tail link**, allows the user of a doubly linked structure to access the last item directly.

The last item in either type of linked structure has no link to the next item. the first item in a doubly linked structure has no link to the preceding item.

Like arrays, these linked structures represent linear sequences of items. However, the programmer who uses a linked structure cannot immediately access an item by specifying its index position.Instead, the programmer must start at one end of the structure and follow the links until the desire position or item is reached.

They way in which memory is allocated form linked structure is also different from array and has two important consequences for insertion and removal operations:
* Onece an insertion or removal point has been found, the insetion or removal can take place with no shifting of data items in memory.
* The linked structure can be resized during each insertion or removal with no extra memory and no copying of data items.

### Noncontiguous Memory and Nodes
A linked structure decouples the logical sequence of items in the structure from any ordering in memory. That is, the cell for a given item in a linked structure can be found anywhere in memory as long as computer can follow a link to its address or location. This kind of memory representation scheme is called **noncontiguous memory**.
The basic unit of representation in a linked structure is a node. A singly linked node contains the following components or fileds:
* A data item
* A link to the next node in the structure.
* (In addition, a doubly linked node contains a link to the previous node in the structure. )

#### Implementation of Linked structure in different languages.
1. In early languages like FORTRAN, use two parallel arrays. The first one stores data items, the other array contained the index positions.
2. In C++/Pascal, a node contains a data item and a pointer value.
3. Python and other: using references to object. defines a singly linked node by defining an object that contains two fields: a reference to a data item and a reference to antoehr node. 

### Defining a Singly Linked Node Class
See sample code [here](/Chapter4/Node.py)

### Using the Singly Linked Node Class
See sample code [here](/Chapter4/Node.py)

In general, you can guard again exceptions by asking whether a given node variable is `None` before attempting to access its fileds:
```python
if nodeVariable != Node:
    <access a field in nodeVarialbe>
```
See sample code [here](/Chapter4/testnode.py)

Note the following points about this sample program:
* One pointer, head, generates the linked structure. This pointer is manipulated in such a way that the most recently inserted item is always at the beginning of the structure.
* Thus, when the data are displayed, they appear in the reverse order of their insertion.
* Also, when the data are displayed, the head pointer is reset to the next node, until the head pointer becomes `None`. Thus, at the end of this process, the nodes are effectively deleted from the linked structure. They are no longer available to the program and are recycled during the next garbage collection.

## Operations on Singly Linked Structures
Almost all the operations on array are indexed based. This section explores how these maniulations are performed in common operations such as traversals, inertions, and removals.
### Traversal
[This sample code](/Chapter4/testnode.py) removed each node form the linked structure. But sometimes we only need to visit. Thus we need t temporary pointer. This is called a **traversal**
See sample code [here](/Chapter/nodeManipulation.py)

In general, a traversal of a singly linked structure visits evey node and terminates when an empty link is reached. Thus, the value `None` serves as a `sentinel` that stops the process.
**Traversals are linear in time and require no extra memory**.

## Searching
The sequential search of a linked structure resoembles a traversal in that you must start at the first node and follow the links until you reach a sentinel. There are two possible sentinels:
1. The empty link, indicating that there are no more data items to examine.
2. A data item that equals the target item, indicating a successful search.

See sample code [here](/Chapter/nodeManipulation.py)

On average, the sequential search is linear for singly linked structures. Unfortunately, accessing the *i*th item of a linked structure is also a sequential search operation.

Linked structures do not support random access. Thus you cannot search a singly linked structure whose data are in sorted order as efficiently as in array. However, there are ways to organize the data in other types of linked structures to remedy this defect.

### Replacement
Same as traversal

### Inserting at the Beginning
```python
head = Node(newItem, head)
```
There is no need for extra memory. This means that inserting data at the beginning of a linked structure uses constant time and memory.

### Inserting at the End
Inserting an item at the end of an array requires constant time and memory unless the array must be resized. The same process for a singly linked structure must consider two cases:
* The head pointer is None, so the head pointer is set to the new node.
* The head pointer is not None, so the code searches for the last node and aims its next pointer at the new node.

See sample code [here](/Chapter4/nodeManipulation.py)

### Removing at the Beginning
```pyhton
head = head.next
```

### Removing at the End
Removing an item at the end of an array requires constant time and memory unless you must resize the array. For linked structure, there are two cases to consider:
1. There is just one node, the `head` pointer is set to None
2. There is a node before the last node. THe code searches for this second to last node and sets its next pointer to None.

### Inserting at Any Position
Two cases:
* That node's next pointer is None. This means that i>=n, so you should place the new item at the end of the linked structure.
* That node's next pointer is not None. That means that 0<i<n, so you must place the new item between the node at position i-1 and the node at position i.

To avoid going off the end of the linked structure in the search. Thus the loop has an additional condition to tests the current node's next poitner to see if it's the final node.
```python
if head is None or index<=0:
    head = Node(newItem, head)
else:
    #Search for node at position index -1 or the last position
    probe = head
    while index>1 and probe.next!=None:
        probe = probe.next
        index-=1
    probe.next=Node(newItem, probe.next) #make this new initialized node the next of probe, and original probe's next the next of this new initialized node.
```

### Removing at Any Position
The removal of the `i`th item from a linked structure has three cases:
* **i<=0** - You use the code to remove the first item
* **0<i<n** - You search for the node at position i-1, as in insertion, and remove the following node. (and linke the next of removed node to the i-1 node)
* **i>=n** - You remove the last node

```python
# Assumes that the linked structure has at least one item
if index<=0 or head.next is None:
    removedItem = head.data
    head = head.next
    return removedItem
else: 
    # Search for node at position index -1 or the next to last position
    probe = head
    while index>1 and probe.next.next!=None:
        probe = probe.next
        index-=1
    removedItem = probe.next.data
    probe.next = probe.next.next
    return removed Item
```

### Complexity Trade-Off: Time, Space, and Singly Linked Structures
|Operation|Running Time|
|:--|:--|
|Access at `i`th position|O(n), average case|
|Repacement at `i`th postion|O(n), average case|
|Insert at beginning|O(1), best and worst case|
|Remove from beginning|O(1), best and worst case|
|Insert at `i`th postion|O(n), average case|
|Remove from `i`th postion|O(n), average case|


## VARIATIONS ON A LINK
### A Cirtular Linked Structure with a Dummy Header Node

The insertion and removal of the first node are special cases as they head pointer must be reset. You can simplify these operations by using a circular linked sctructure with a dummy header node. The circular linked structure contains a link from the last node back to the first node in the structure. The dummy header has no value but servs as a marker for the beginning and the end of the linked structure. 

Initialization
```python
head = Node(None, None)
head.next = head
```
Search
```python
#Search for node at position index-1 or the last position
probe = head
while index>0 and probe.next!=head:
    probe = probe.next
    index-=1

# Insert new node after node at position index-1 or last position
probe.next = Node(newItem, probe.next)
```

THe advantage of this implementation is that the insertion and removal operations have only one case to consider - the case in which the ith node lies between a prior node and the current `i`th node. When the `i`th is the first node, the prior node is the header node. when i>=n, the last node is the prior node and the header is the next node. 

### Doubly Linked Structure
In addition to singly linked structure, allows the user to:
* Move left, to the previous node, from a given node
* Move immediately to the last node. 

The Python implementation of a node class for doubly linked structure see sample code [here]().
