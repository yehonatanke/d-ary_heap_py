from DaryHeap import DaryHeap


def build_new_heap(scanner, d):
    """
    Builds a new d-ary heap based on user input.

    Args:
        scanner: The input scanner for reading user input.
        d (int): The arity of the heap.

    Returns:
        DaryHeap: A new d-ary heap.

    Raises:
        ValueError: If the number of elements is negative or the list of elements is empty.

    Note:
        The function prompts the user to enter the number of elements and each element for the new heap.

    Time Complexity:
        O(n), where n is the number of elements entered.

    Space Complexity:
        O(n), where n is the number of elements entered.
    """
    print("Enter the number of elements for the new heap: ")
    num_elements = int(input())

    if num_elements < 0:
        raise ValueError("Number of elements must be non-negative")

    elements = []
    for i in range(num_elements):
        print(f"Enter element {i + 1}: ")
        elements.append(int(input()))

    if not elements:
        raise ValueError("List of elements cannot be empty")

    return DaryHeap(d, elements)
