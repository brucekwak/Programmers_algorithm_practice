def check_possible(mid, n, times):
    total = 0
    for t in times:
        total += (mid // t)
    print(total)
    if total >= n:
        return True
    return False

def solution(n, times):
    answer = 0
    left = 1
    right = sum([t * (n//len(times)+1) for t in times])
    
    answer = 1
    while left <= right:
        mid = (left + right) // 2
        print(left, mid, right)
        if check_possible(mid, n, times) == True:
            right = mid -1
            answer = mid
        else:
            left = mid + 1
        
    return answer