class DaryHeap:
    def __init__(self, d, elements=None):
        """
        Initializes a d-ary heap.

        Args:
            d (int): The arity of the heap.
            elements (list, optional): Initial elements of the heap. Defaults to None.

        Returns:
            None

        Time Complexity:
            O(n), where n is the number of elements in the heap.

        Space Complexity:
            O(n)
        """
        self.d = d
        if elements is not None:
            self.heap = elements[:]
            self.build_max_heap()
        else:
            self.heap = []

    def max_heap_insert(self, key):
        """
        Inserts a key into the d-ary heap while maintaining the max-heap property.

        Args:
            key: The key to be inserted.

        Returns:
            None

        Raises:
            ValueError: If the new key is smaller than the current key.

        Time Complexity:
            O(log_d(n)), where n is the number of elements in the heap.

        Space Complexity:
            O(1)
        """
        self.heap.append(float('-inf'))
        self.heap_increase_key(len(self.heap) - 1, key)

    def extract_max(self):
        """
        Extracts the maximum key from the d-ary heap while maintaining the max-heap property.

        Returns:
            The maximum key in the heap.

        Raises:
            Exception: If the heap is empty.

        Time Complexity:
            O(log_d(n)), where n is the number of elements in the heap.

        Space Complexity:
            O(1)
        """
        if len(self.heap) < 1:
            raise Exception("Heap underflow: no elements to extract")
        max_element = self.heap[0]
        last_element = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_element
            self.max_heapify(0)
        return max_element

    def build_max_heap(self):
        """
        Builds a max-heap from the current elements of the d-ary heap.

        Returns:
            None

        Time Complexity:
            O(n), where n is the number of elements in the heap.

        Space Complexity:
            O(1)
        """
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.max_heapify(i)

    def heap_increase_key(self, index, new_key):
        """
        Increases the key of a node in the d-ary heap.

        Args:
            index (int): Index of the node.
            new_key: New key value.

        Returns:
            None

        Raises:
            ValueError: If the new key is smaller than the current key.

        Time Complexity:
            O(log_d(n)), where n is the number of elements in the heap.

        Space Complexity:
            O(1)
        """
        if new_key < self.heap[index]:
            raise ValueError("New key is smaller than the current key")
        self.heap[index] = new_key
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def swap(self, i, j):
        """
        Swaps elements at two indices in the d-ary heap.

        Args:
            i (int): Index of the first element.
            j (int): Index of the second element.

        Returns:
            None

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def is_max_heap(self):
        """
        Checks if the current state of the heap satisfies the max-heap property.

        Returns:
            True if it's a max-heap, False otherwise.

        Time Complexity:
            O(n), where n is the number of elements in the heap.

        Space Complexity:
            O(1)
        """
        for i in range(len(self.heap)):
            left_child = self.d * i + 1
            if left_child < len(self.heap) and self.heap[i] < self.heap[left_child]:
                return False
        return True

    def max_heapify(self, index):
        """
        Maintains the max-heap property starting from a given index.

        Args:
            index (int): Index to start the max-heapify operation.

        Returns:
            None

        Time Complexity:
            O(log_d(n)), where n is the number of elements in the heap.

        Space Complexity:
            O(1)
        """
        max_child = self.find_max_child(index)
        if max_child != -1 and self.heap[index] < self.heap[max_child]:
            self.swap(index, max_child)
            self.max_heapify(max_child)

    def find_max_child(self, index):
        """
        Finds the index of the maximum child of a node in the d-ary heap.

        Args:
            index (int): Index of the node.

        Returns:
            Index of the maximum child or -1 if no child exists.

        Time Complexity:
            O(d), where d is the arity of the heap.

        Space Complexity:
            O(1)
        """
        start_child = self.d * index + 1
        end_child = min(start_child + self.d - 1, len(self.heap) - 1)
        max_child_index = -1
        max_child_value = float('-inf')

        for i in range(start_child, end_child + 1):
            if self.heap[i] > max_child_value:
                max_child_value = self.heap[i]
                max_child_index = i

        return max_child_index

    def delete(self, i):
        """
        Deletes a node at a given index from the d-ary heap.

        Args:
            i (int): Index of the node to be deleted.

        Returns:
            None

        Raises:
            IndexError: If the index is out of bounds.

        Time Complexity:
            O(log_d(n)), where n is the number of elements in the heap.

        Space Complexity:
            O(1)
        """
        if i < 0 or i >= len(self.heap):
            raise IndexError("Index out of bounds")
        last_index = len(self.heap) - 1
        self.swap(i, last_index)
        self.heap.pop()
        self.max_heapify(i)

    def print_heap_by_depth(self):
        """
        Prints the d-ary heap with elements grouped by depth.

        Returns:
            None

        Time Complexity:
            O(n), where n is the number of elements in the heap.

        Space Complexity:
            O(1)
        """
        depth = 0
        level_size = 1

        print(f'd-ary Heap (d = {self.d}): ', end='')
        for i in range(len(self.heap)):
            if i == level_size:
                print('\t', end='')  # Move to the next level
                depth += 1
                level_size += self.d ** depth

            print(f'{self.heap[i]} ', end='')

        print('')  # Print a newline at the end

    def is_empty(self):
        """
        Checks if the d-ary heap is empty.

        Returns:
            True if the heap is empty, False otherwise.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        return len(self.heap) == 0

    def parent(self, i):
        """
        Calculates the index of the parent node for a given index in the d-ary heap.

        Args:
            i (int): Index of the node.

        Returns:
            Index of the parent node.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        return (i - 1) // self.d
