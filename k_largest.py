import heapq

def k_large(arr, k):
    if not 1 <= k <= len(arr):
        raise ValueError("k should be between 1 and len(arr)")

    heap = []

    for num in arr:
        heapq.heappush(heap,num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]

print(k_large([2,3,4,5,6,7,8,9], 4))