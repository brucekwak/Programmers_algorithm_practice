# [풀이-1] 1차 풀이
def solution(answers):
    
    candi_1 = [1, 2, 3, 4, 5] * len(answers)
    candi_1 = candi_1[:len(answers)]
    candi_2 = [2, 1, 2, 3, 2, 4, 2, 5] * len(answers)
    candi_2 = candi_2[:len(answers)]
    candi_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * len(answers)
    candi_3 = candi_3[:len(answers)]
    
    score_list = []
    for candi_i in [candi_1, candi_2, candi_3]:
        score = [1 for i in range(len(candi_i)) if candi_i[i] == answers[i]]
        score_list.append(sum(score))
    
    max_score = max(score_list)
    answer = []
    for ind, score in enumerate(score_list):
        if score == max_score:
            answer.append(ind+1)
    return answer

# [풀이-2] 간결한 풀이
# 풀이-1보다 시간은 더 소요됨
# score 가 +1 될 때마다 +1 연산
def solution(answers):
    p = [
        [1, 2, 3, 4, 5], 
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    score = [0] * len(p)
    
    for a_ind, a in enumerate(answers):
        for v_ind, v in enumerate(p):
            if a == v[a_ind % len(v)]:
                score[v_ind] += 1
    
    return [i+1 for i, val in enumerate(score) if val == max(score)]