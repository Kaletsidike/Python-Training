# def insertion_sort(arr):
#  for i in range(1, len(arr)):
#      j=i
#      while arr[j-1]> arr[j] and j >0:
#         arr[j-1], arr[j] = arr[j], arr[j-1]
#         j-=1

# arr=[2,4,5,7,1,6]
# insertion_sort(arr)
# print(arr)

########## OR  in a logical manner
def insertion_sort(arr):
    """Sorts an array of numbers using the insertion sort algorithm in-place.

    Args:
        arr: The array of numbers to be sorted.

    Returns:
        None. The array is sorted in-place.
    """

    for i in range(1, len(arr)):
        """Iterates through the array (starting from the second element) to insert each element into its correct position."""

        current = arr[i]  # Store the current element to be inserted.
        j = i  # Initialize the index for comparisons.

        while j > 0 and arr[j - 1] > current:  # Shift larger elements to the right if necessary.
            arr[j] = arr[j - 1]
            j -= 1

        arr[j] = current  # Insert the current element at its correct position.

# Example usage
arr = [2, 4, 5, 7, 1, 6]
insertion_sort(arr)
print(arr)  # Output: [1, 2, 4, 5, 6, 7]
