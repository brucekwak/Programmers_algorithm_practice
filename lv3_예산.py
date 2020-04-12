def check_possible(budgets, check, M):
    check_list = []
    for b in budgets:
        if b > check:
            check_list.append(check)
        else:
            check_list.append(b)
    if sum(check_list) > M:
        return False
    return True

def solution(budgets, M):
    left = 0
    right = max(budgets)
    
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if check_possible(budgets, mid, M) == True:
            left = mid + 1
            answer = mid
        else:
            right = mid - 1
    
    return answer