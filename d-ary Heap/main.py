from DaryHeap import DaryHeap
from DaryHeapUtility import build_new_heap


def main():
    """
    Interactive console application for performing actions on a d-ary heap.

    Returns:
       None

    Note:
       The main function provides a menu-driven console interface to interact with a d-ary heap.
       Users can insert elements, extract the maximum element, build a max-heap, increase key,
       delete key, print the heap by depth, and exit the program.
    """

    d = int(input("Enter the degree of the d-ary heap (must be at least 2): "))
    d_ary_heap = DaryHeap(d)

    while True:
        print("\nChoose an action:")
        print("1. Insert element")
        print("2. Extract maximum element")
        print("3. Build Max-Heap")
        print("4. Increase Key")
        print("5. Delete Key")
        print("6. Print Heap by Depth")
        print("7. Exit")

        choice = int(input())

        if choice == 1:
            element = int(input("Enter the element to insert: "))
            d_ary_heap.max_heap_insert(element)
        elif choice == 2:
            try:
                print("Extracted max element:", d_ary_heap.extract_max())
            except Exception as e:
                print(str(e))
        elif choice == 3:
            d_ary_heap = build_new_heap(input, d)
        elif choice == 4:
            index = int(input("Enter the index of the element to increase key: "))
            new_key = int(input("Enter the new key value: "))
            d_ary_heap.heap_increase_key(index, new_key)
        elif choice == 5:
            key_to_delete = int(input("Enter the key you want to delete: "))
            d_ary_heap.delete(key_to_delete)
        elif choice == 6:
            d_ary_heap.print_heap_by_depth()
        elif choice == 7:
            print("Exiting program. Bye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
