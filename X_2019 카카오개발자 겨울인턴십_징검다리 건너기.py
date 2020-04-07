# 주어진 stones 에서 num 개를 통과할 수 있는가를 확인하는 함수
# k: 최대 넘을 수 있는 돌
# def check_possible(stones, check_num, k):
#     # 1) check_num-1 명이 건넌 후 돌다리의 상태
#     stones_remain = [max(0, stone-(check_num-1)) for stone in stones]
#     # print(stones_remain)
    
#     # 2) 남은 돌다리에서 한명이 더 건너려면 건너야 할 칸 리스트
#     stones_remain_ind_list = [ind for ind, val in enumerate(stones_remain) if val > 0]
#     if len(stones_remain_ind_list) == 0:
#         return False
    
#     step_list = [stones_remain_ind_list[i] - stones_remain_ind_list[i-1] for i in range(1, len(stones_remain_ind_list))]
#     # print(step_list)
#     step_list.append(stones_remain_ind_list[0] + 1)
#     step_list.append(len(stones_remain_ind_list) - stones_remain_ind_list[-1])
    
#     if max(step_list) > k:
#         return False
#     return True

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