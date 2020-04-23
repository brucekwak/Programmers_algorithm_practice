# [풀이] BFS
from collections import deque

def solution(maps):
    # maps[r][c] := r행 c열
    # 시작점 = maps[0][0]
    # 도착점 = maps[n-1][m-1]
    
    # BFS
    N = len(maps)
    M = len(maps[0])
    
    shortest_maps = [[1e10]*M for _ in range(N)]  # shape = NxM
    shortest_maps[N-1][M-1] = 1
    
    start = [(N-1, M-1), 1]  # [(현재 위치), 거리]
    queue = deque()
    
    queue.append(start)
    
    while queue:
        current = queue.popleft()
        for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = current[0][0]+move[0], current[0][1]+move[1]
            dist = current[1]+1
            if r >= 0 and r <= (N-1) and c >= 0 and c <= (M-1) and maps[r][c] == 1 and dist < shortest_maps[r][c]:
                shortest_maps[r][c] = dist
                queue.append([(r,c), dist])
    
    if shortest_maps[0][0] == 1e10:
        return -1
    else:
        return shortest_maps[0][0]