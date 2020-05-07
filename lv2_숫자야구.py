# [Reference] https://geonlee.tistory.com/116
from itertools import permutations

def check_score(candi, baseball):
    for check_num, s, b in baseball:
        check_num = [int(x) for x in str(check_num)]
        strike = 0
        for i in range(3):
            if candi[i] == check_num[i]:
                strike += 1
        if strike != s:
            return False
        ball = len(set(candi) & set(check_num)) - strike
        if ball != b:
            return False
    return True

def solution(baseball):
    candi_list = list(permutations(list(range(1,10)), 3))

    answer = 0
    for candi in candi_list:
        if check_score(candi, baseball) == True:
            answer += 1
    
    return answer