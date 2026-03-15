import random
import time
import tracemalloc
import sys

# Increase recursion depth for larger inputs
sys.setrecursionlimit(20000)


# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Quick Sort Implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)


# Benchmark Function
def benchmark(sort_function, data):
    tracemalloc.start()
    start_time = time.perf_counter()

    sorted_result = sort_function(list(data))

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "time_seconds": end_time - start_time,
        "peak_memory_kb": peak / 1024,
        "is_correct": sorted_result == sorted(data)
    }


# Main Program
def main():
    size = 5000

    random_data = random.sample(range(10000), size)
    sorted_data = sorted(random_data)
    reverse_sorted_data = sorted(random_data, reverse=True)

    datasets = {
        "Random Data": random_data,
        "Sorted Data": sorted_data,
        "Reverse Sorted Data": reverse_sorted_data
    }

    print("=" * 70)
    print("Performance Comparison: Merge Sort vs Quick Sort")
    print("=" * 70)

    for name, data in datasets.items():
        merge_metrics = benchmark(merge_sort, data)
        quick_metrics = benchmark(quick_sort, data)

        print(f"\nDataset: {name}")
        print("-" * 70)
        print(
            f"Merge Sort -> Time: {merge_metrics['time_seconds']:.6f} sec, "
            f"Memory: {merge_metrics['peak_memory_kb']:.2f} KB, "
            f"Correct: {merge_metrics['is_correct']}"
        )
        print(
            f"Quick Sort -> Time: {quick_metrics['time_seconds']:.6f} sec, "
            f"Memory: {quick_metrics['peak_memory_kb']:.2f} KB, "
            f"Correct: {quick_metrics['is_correct']}"
        )


if __name__ == "__main__":
    main()