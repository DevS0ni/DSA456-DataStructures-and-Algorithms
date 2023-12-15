#    Main Author(s): Dev Soni & Sarah Haque
#    Main Reviewer(s): Sarah Haque


class MinHeap:

    def __init__(self, arr=None):
        # Initialize the heap with a copy of the provided array or an empty list if none is provided.
        self.heap = arr[:] if arr is not None else []

        # If an array is provided, convert it into a heap using heapify down method.
        if arr:
            for i in range(len(arr) // 2 - 1, -1, -1):
                self._heapify_down(i)

    def insert(self, element):
        # Add the new element to the end of the heap.
        self.heap.append(element)
        # Restore the heap property by moving the new element up as needed.
        self._heapify_up(len(self.heap) - 1)

    def get_min(self):
        # Return the smallest element (root of the heap) if the heap is not empty.
        return self.heap[0] if self.heap else None

    def extract_min(self):
        # If the heap is empty, return None.
        if not self.heap:
            return None

        # Store the minimum element.
        minimum = self.heap[0]

        # Move the last element to the root and remove the last element from the list.
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        # Restore the heap property by moving the new root down as needed.
        self._heapify_down(0)

        # Return the minimum element.
        return minimum

    def is_empty(self):
        # Check if the heap is empty.
        return len(self.heap) == 0

    def __len__(self):
        # Return the number of elements in the heap.
        return len(self.heap)

    def _heapify_up(self, index):
        # Restore the heap property by moving the element at index up.
        while index > 0 and self.heap[index] < self.heap[(index - 1) // 2]:
            # Swap the element with its parent if it is smaller than the parent.
            self.heap[index], self.heap[(index - 1) // 2] = self.heap[(index - 1) // 2], self.heap[index]
            # Move up to the parent's index.
            index = (index - 1) // 2

    def _heapify_down(self, index):
        # Restore the heap property by moving the element at index down.
        child_index = 2 * index + 1
        while child_index < len(self.heap):
            # Check if the right child exists and is smaller than the left child.
            if child_index + 1 < len(self.heap) and self.heap[child_index + 1] < self.heap[child_index]:
                child_index += 1

            # Check if we need to swap the current node with its smaller child.
            if self.heap[index] <= self.heap[child_index]:
                break

            # Swap the current element with its smaller child.
            self.heap[index], self.heap[child_index] = self.heap[child_index], self.heap[index]
            # Move down to the child's index.
            index = child_index
            child_index = 2 * index + 1

