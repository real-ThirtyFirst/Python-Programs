def bubble_sort(arr):
    print("\n--- Bubble Sort ---")
    n = len(arr)
    swapped_once = False
    swapped = False
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                swapped_once = True
        if not swapped:
            continue
        else:
            print(f"Pass {i + 1}: {arr}")
    if swapped_once:
        print("Finished Sorting")
    if not swapped:
        print("Already Sorted")
    return arr

def insertion_sort(arr):
    print("\n--- Insertion Sort ---")
    n = len(arr)
    swapped_once = False
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        swapped = False
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            swapped = True
            swapped_once = True
        arr[j + 1] = key
        if swapped:
            print(f"Pass {i}: {arr}")
    if not swapped_once:
        print("Already Sorted")
    else:
        print("Finished Sorting")
    return arr

def selection_sort(arr):
    print("\n--- Selection Sort ---")
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Pass {i + 1}: {arr}")
    return arr

# Input with validation
while True:
    try:
        size = int(input("Enter array size (1-25): "))
        if 1 <= size <= 25:
            break
        else:
            print("Size must be between 1 and 25.")
    except ValueError:
        print("Please enter a valid integer.")

arr = []
for i in range(size):
    while True:
        try:
            num = int(input(f"Enter element {i + 1} (1-100): "))
            if 1 <= num <= 100:
                arr.append(num)
                break
            else:
                print("Number must be between 1 and 100.")
        except ValueError:
            print("Please enter a valid integer.")

# Ask user which sort to use
print("\nChoose sorting algorithm:")
print("1 - Bubble Sort")
print("2 - Insertion Sort")
print("3 - Selection Sort")

while True:
    choice = input("Enter choice (1/2/3): ")
    if choice in ['1', '2', '3']:
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

# Clone array to preserve original
to_sort = arr.copy()

if choice == '1':
    bubble_sort(to_sort)
elif choice == '2':
    insertion_sort(to_sort)
elif choice == '3':
    selection_sort(to_sort)

print("\nFinal Sorted Array:", to_sort)
