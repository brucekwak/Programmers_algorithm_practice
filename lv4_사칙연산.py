def solution(arr):
    
    N = (len(arr)+1)//2   # 숫자 개수
    for i in range(N):
        arr[2*i] = int(arr[2*i])
    
    # min_table[a][b] := a번째 숫자 ~ b번째 숫자까지의 범위에서 만들 수 있는 최소값
    min_table = [[-1]*N for _ in range(N)]  # N x N 행렬
    for i in range(N):
        min_table[i][i] = arr[2*i]
    for i in range(N-1):
        min_table[i][i+1] = (arr[2*i] + arr[2*(i+1)]) if arr[2*i+1] == "+" else (arr[2*i] - arr[2*(i+1)])
    
    # max table 초기화
    max_table = [[-1]*N for _ in range(N)]  # N x N 행렬
    for i in range(N):
        max_table[i][i] = arr[2*i]
    for i in range(N-1):
        max_table[i][i+1] = (arr[2*i] + arr[2*(i+1)]) if arr[2*i+1] == "+" else (arr[2*i] - arr[2*(i+1)])
    
    # cut_point 만들고 iteratin 돌리기
    for iter_num in range(2, N):
        for r in range(N-iter_num):  # 0 ~ (N-iter_num-1)
            # r번째 ~ (r+iter_num)번째 숫자로 만드는 최대/최소값
            max_candi_list = []
            min_candi_list = []
            for cut_point in range(iter_num):  # 0 ~ (iter_num-1)
                oper = arr[2*(r+cut_point)+1]
                max_candi = max_table[r][r+cut_point]
                min_candi = min_table[r][r+cut_point]
                if oper == "+":
                    max_candi += max_table[r+cut_point+1][r+iter_num]
                    min_candi += min_table[r+cut_point+1][r+iter_num]
                else:
                    max_candi -= min_table[r+cut_point+1][r+iter_num]
                    min_candi -= max_table[r+cut_point+1][r+iter_num]
                max_candi_list.append(max_candi)
                min_candi_list.append(min_candi)
                
            max_table[r][r+iter_num] = max(max_candi_list)
            min_table[r][r+iter_num] = min(min_candi_list)
    
    return max_table[0][-1]