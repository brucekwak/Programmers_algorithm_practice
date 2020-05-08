# [Reference] https://codedrive.tistory.com/82
import heapq

def solution(stock, dates, supplies, k):
    count = 0
    idx = 0
    candi_list = []
    while stock < k:
        for i in range(idx, len(dates)):
            if dates[i] <=stock:
                heapq.heappush(candi_list, (-supplies[i],supplies[i]))  # (우선순위, 값)
                idx = i+1
            else:
                break
        stock += heapq.heappop(candi_list)[1]
        count += 1
        
    return count