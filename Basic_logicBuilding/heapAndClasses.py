import heapq

# heaps are array

minHeap = []
heapq.heappush(minHeap, 4)
heapq.heappush(minHeap, 5)
heapq.heappush(minHeap, 37)
heapq.heappush(minHeap, 3)

print(minHeap)  #print all the heap

print(minHeap[0])  #the minimum value will be returned
print("\n")
while len(minHeap):
    print(heapq.heappop(minHeap))       #removing all heap

print(minHeap)


#  to get greatest value of heap
maxHeap = []

heapq.heappush(maxHeap, -10)
heapq.heappush(maxHeap, -20)
heapq.heappush(maxHeap, -5)

# No Max heaps by default, work around is to use min heap
# and multiply by -1 when push and pop
print(-1 * maxHeap[0])
