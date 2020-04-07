def check_possible(stones, check_num, k):
    now = -1
    for i in range(len(stones)):
        if (stones[i] - (check_num-1)) > 0:
            if i-now > k:
                return False
            now = i
    if (len(stones) - now) > k:
        return False
    else:
        return True
    
def solution(stones, k):
    
    if min(stones) == max(stones):
        return min(stones)
    
    # binary search
    answer = 0
    lower_limit, upper_limit = 0, max(stones)     
    while lower_limit <= upper_limit:
        # print('---')
        # print(lower_limit, upper_limit)
        check_num = (upper_limit + lower_limit) // 2
        # print(check_num)
        check_result = check_possible(stones, check_num, k)
        # print(check_result)
        if check_result == True:
            answer = check_num
            lower_limit = check_num + 1
        else:
            upper_limit = check_num - 1
    return answer