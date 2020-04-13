# [풀이] queue, dictionary comprehension 활용
from collections import deque

def solution(n, edge):
    # graph dict 만들기
    nodes = list(range(1, n+1))
    graph_dict = {node:[] for node in nodes}
    visit = [False for _ in range(len(nodes)+1)]
    
    for n1, n2 in edge:
        graph_dict[n1].append(n2)
        graph_dict[n2].append(n1)
    
    # BFS 하면서 1로부터의 depth 기록
    queue = deque()
    start_node = 1
    queue.append((start_node, 0))  # (node_num, depth)
    
    depth_dict = {}
    while queue:
        current_node, depth = queue.popleft()
        if visit[current_node] == False:
            visit[current_node] = True
            depth_dict[current_node] = depth      
            for child_i in graph_dict[current_node]:
                queue.append((child_i, depth+1))
    
    max_depth = max(list(depth_dict.values()))
    answer = len([node for node in depth_dict.keys() if depth_dict[node]==max_depth])
    
    return answer
