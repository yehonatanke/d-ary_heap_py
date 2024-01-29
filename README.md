<div align="center">
  <img src="https://img.shields.io/badge/language-Python-%233776AB.svg?logo=python">
  <img src="https://custom-icon-badges.demolab.com/github/license/denvercoder1/custom-icon-badges?logo=law">
</div>

# d-ary Heap

## Overview
The D-ary Heap implements a D-ary max heap data structure in Python. It supports essential operations such as insertion, extraction of the maximum element, building a max heap, increasing a key, deleting a key, and printing the heap by depth. The implementation utilizes a list as the underlying data structure. Detailed comments, time, and space complexity analyses are provided for each method.

## Table of Contents
1. [General Information](#general-information)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Program Structure](#program-structure)
    - [DaryHeap Class](#daryheap-class-methods-)
    - [Main Program](#main-program-functions)
    - [Usage](#usage-1)
5. [License](#license)
6. [Author](#author)

### General Information
d-ary data structure is a variant of a binary heap, where each node has D children

## Installation

To use the DaryHeap library in your Python project, follow these simple steps:

1. Clone Repository:
   ```bash
   git clone [https://github.com/yehonataKe/d-ary_heap_py.git] 

2. Include in Your Project:
- Include the DaryHeap.py file in your project.
- Ensure the file is in the correct directory or adjust import statements accordingly.

## Usage

To use the DaryHeap in your Python program, follow these steps:

- Import DaryHeap class:
   ```python
   from DaryHeap import DaryHeap
   ```
- Create an instance of the DaryHeap class.
- Use the provided methods like max_heap_insert and delete for manipulating the heap.

## Program Structure

### DaryHeap Class Methods 
#### `delete(self, i)`
- Deletes a node at a given index from the D-ary heap.
- Args: `i (int)`: Index of the node.
- Returns: `None`
- Raises: `IndexError`: If the index is out of bounds.
- Time Complexity: O(log_d(n)), where n is the number of elements in the heap.
- Space Complexity: O(1)

#### `print_heap_by_depth(self)`
- Prints the D-ary heap with elements grouped by depth.
- Returns: `None`
- Time Complexity: O(n), where n is the number of elements in the heap.
- Space Complexity: O(1)

#### `is_empty(self)`
- Checks if the D-ary heap is empty.
- Returns: True if the heap is empty, False otherwise.
- Time Complexity: O(1)
- Space Complexity: O(1)

#### `parent(self, i)`
- Calculates the index of the parent node for a given index in the D-ary heap.
- Args: `i (int)`: Index of the node.
- Returns: Index of the parent node.
- Time Complexity: O(1)
- Space Complexity: O(1)

### Main Program Functions

#### `build_new_heap(scanner, d)`
- Builds a new D-ary heap based on user input.
- Args: `scanner`: The input scanner for reading user input, `d (int)`: The arity of the heap.
- Returns: A new D-ary heap.
- Raises: `ValueError`: If the number of elements is negative or the list of elements is empty.
- Time Complexity: O(n), where n is the number of elements entered.
- Space Complexity: O(n), where n is the number of elements entered.

### Usage

#### DaryHeap Class Usage:
```python
# Example usage of DaryHeap class
d = 3
dary_heap = DaryHeap(d, [5, 8, 2, 12, 7])
dary_heap.build_max_heap()
print("Max-Heap:", dary_heap.heap)  # Example: [12, 8, 2, 5, 7]
```

## License
This program is open-source and released under the [MIT License](https://github.com/yehonatanke/d-ary_heap_py/blob/main/LICENSE).

## Author

yehonataKe
