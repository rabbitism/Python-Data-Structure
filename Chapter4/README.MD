# CHapter 4: ARRAYS AND LINKED STRUCTURES
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