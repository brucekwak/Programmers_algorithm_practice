# [풀이 -1] queue 활용
from collections import deque

def solution(priorities, location):
    queue = deque()
    for ind, priority in enumerate(priorities):
        queue.append((ind, priority))  # tuple
    
    count = 0
    while len(queue) > 0:
        now = queue.popleft()
        if len(queue) == 0:
            count += 1
            return count
        else:
            max_val_in_queue = max([priority for ind, priority in queue])
            if now[1] >= max_val_in_queue:
                count += 1
                if now[0] == location:
                    return count
            else:
                queue.append(now)
    
    return count

# [풀이-2] queue & any 활용
from collections import deque

def solution(priorities, location):
    queue = deque()
    for i, p in enumerate(priorities):
        queue.append((i,p))
    count = 0
    while True:
        now = queue.popleft()
        if any(now[1] < q[1] for q in queue):
            queue.append(now)
        else:
            count += 1
            if now[0] == location:
                return count