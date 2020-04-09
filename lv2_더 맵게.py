# [풀이 - 1] heapq.heapify() 활용
import heapq

def solution(scoville, K):
    heap = scoville[:]
    heapq.heapify(heap)
    
    total_count = 0
    while heap[0] < K:
        check = heapq.heappop(heap)
        if len(heap) > 0:
            check_next = heapq.heappop(heap)
            check_sum = check + check_next*2
            heapq.heappush(heap, check_sum)
            total_count += 1
        else:
            return -1
    return total_count

# [풀이 - 2] heappush 로 힙리스트 만들기
# (참고) 힙정렬하려면, heappush 로 만든 힙리스트에서 차례대로 pop한 원소로 리스트 구축하면 됨
import heapq

def solution(scoville, K):
    heap = []
    for score in scoville:
        heapq.heappush(heap, score)
    
    total_count = 0
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + 2 * heapq.heappop(heap))
            total_count += 1
        except IndexError:
            return -1
    return total_count