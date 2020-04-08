# [풀이-1] 기본 풀이
def solution(heights):
    
    answer = [0]  # 첫번째 탑이 보내는 신호 -> 수신X
    for ind, height in enumerate(heights):
        if ind == 0:
            continue
        check_list = heights[:ind]     
        find_flag = False
        for i in range(len(check_list)-1, -1, -1):
            if check_list[i] > height:
                answer.append(i+1)
                find_flag = True
                break
        if find_flag == False:
            answer.append(0)
    
    return answer

# [풀이-2] 조금 더 간결한 풀이
def solution(heights):
    answer = [0] * len(heights)
    
    for i in range(len(heights)):
        for j in range(i-1, -1, -1):
            if heights[j] > heights[i]:
                answer[i] = j+1
                break
    
    return answer