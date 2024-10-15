import matplotlib.pyplot as plt

# Data
sizes = [10000, 25000, 50000, 100000, 150000, 200000]
merge_sort_times = [2000, 5000, 11000, 22000, 33000, 45000]
quick_sort_times = [1500, 3700, 9000, 18000, 27000, 36000]
insertion_sort_times = [8000, 20000, 45000, 90000, 135000, 180000]
selection_sort_times = [10000, 25000, 60000, 120000, 180000, 240000]

# Creating plots
plt.figure(figsize=(10, 8))

plt.plot(sizes, merge_sort_times, label='Merge Sort', marker='o')
plt.plot(sizes, quick_sort_times, label='Quick Sort', marker='o')
plt.plot(sizes, insertion_sort_times, label='Insertion Sort', marker='o')
plt.plot(sizes, selection_sort_times, label='Selection Sort', marker='o')

plt.title('Comparison of Sorting Algorithm Performances')
plt.xlabel('Array Size')
plt.ylabel('Running Time (microseconds)')
plt.legend()
plt.grid(True)
plt.show()
