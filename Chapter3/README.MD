# SEARCHING, SORTING AND COMPLEXITY ANALYSIS
Criteria for assessing the quality of an algorithm
1. Correctness
2. Readability
3. Ease of maintenance
4. Run-time performance

## MEASURING THE EFFICIENCY OF ALGORITHMS

### Measuring the Run Time of an ALgorithm
See sample code in [timing1.py](/Chapter3/timing1.py) and [timing2.py](/Chapter3/timing2.py)

This method permits accurate predictions of the running times of many algorithms. However, there are two major problems:
1. Different hardware platforms have different processing speeds. 
2. It is impractical to determine the running time for some algorithms with very large data sets.

### Counting Instructions
Another technique used is to count the instructions executed with different problem sizes. However counting the instructions in the high-level code in which the algorithm is written, not instructions in the executable machine language program.

When analyzing an algorithm, you distinguish between two classes of instructions:
* Instructions that execute the same number of times regardless of the problem size
* Instructions whose execution count varies with the problem size

See sample code for counting [iterations](/Chapter3/counting.py) and [Fibonacci function](/Chapter3/countfib.py)

## COMPLEXITY ANALYSIS
### Order of Compexity
Some sample orders of compexity
|n|Logarithmic|Linear|Quadratic|Exponential|
|:-|:-|:-|:-|:-|
|100|7|100|10,000|Off the chart|
|1000|10|1,000|1,000,000|Off the chart|
|1000|20|10,000|1,000,000,000,000|Off the chart|

### Big-O Notation

### The Role of the Constant of Proportionality
The constant of proportionality involves the terms and coefficients that are usually ignored during big-O analysis.


## SEARCH ALGORITHMS
See sample code [here](/Chapter3/Search.py) for different search algorithms

### Search for the Minimum
### Sequential Search of a List
### Best-Case, Worst-Case, and Average-Case Performance
1. worst case: O(n)
2. best case: O(1)
3. average case: O(n)

### Binary Search of a Sorted List
See sample code [here](/Chapter3/Search.py)
Complexity: O(logn)

### Comparing Data Items
In search algorithms, we assume that the items in the list are comparable with each other. In Python, this means that the items are of the same type and they recognize the comparison operators ==, <, and >.
To allow algorithms to use the comparison operators ==, < and> with new class of objects, the programmer should define __eq__, __lt__, __gt__ methods in that class.
```python
def __lt__(self, other):
```
See sample code [here](/Chapter3/SavingAccount.py)

## BASIC SORT ALGORITHMS
See sample code [here](/Chapter3/sort.py)
### Selection Sort
Complexity: O(n^2)
### Bubble Sort
Complexity: O(n^2)
### Insertion Sort