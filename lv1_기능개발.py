import math

def solution(progresses, speeds):    
    work_days = [math.ceil((100 - prog) / float(speed)) for prog, speed in zip(progresses, speeds)]
    
    answer = []
    front = 0
    for idx in range(len(work_days)):
        if work_days[front] < work_days[idx]:
            answer.append(idx-front)
            front = idx
    answer.append(len(work_days)-front)
    
    return answer