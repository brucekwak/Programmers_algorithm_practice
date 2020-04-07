# [풀이 1] 기본 풀이 
def solution(board, moves):
    bucket = list()
    N = len(board)
    remove_count = 0
    
    for move in moves:
        find_flag = False
        for check_i in range(N):  # 0 ~ N-1
            print(board[check_i][move-1])
            if board[check_i][move-1] != 0:
                bucket.append(board[check_i][move-1])
                board[check_i][move-1] = 0
                find_flag = True
                break
        if find_flag == True:
            if len(bucket) >= 2 and (bucket[-1] == bucket[-2]):
                remove_count += 2
                bucket = bucket[:-2]  # 뒤쪽 2개 원소 삭제
            
    return remove_count


# [풀이 2] stack, pop 용어 활용
def solution(board, moves):
    stack = list()    
    remove_count = 0
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stack.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop(-1)
                stack.pop(-1)
                remove_count += 2
            
    return remove_count