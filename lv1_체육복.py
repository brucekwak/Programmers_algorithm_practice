# [풀이-1] for 문 길게
def solution(n, lost, reserve):
    
    add_count = 0
    check_list = []
    for r in reserve:
        if r in lost:
            check_list.append(r)
    for c in check_list:
        reserve.remove(c)
        lost.remove(c)
            
    reserve = sorted(reserve)
    for l in lost:
        if (l-1) in reserve:
            reserve.remove(l-1)
            add_count += 1
        elif (l+1) in reserve:
            reserve.remove(l+1)
            add_count += 1
    
    answer = n - len(lost) + add_count
    
    return answer

# [풀이-2] list comprehension 활용
def solution(n, lost, reserve):
    
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    
    for r in _reserve:
        a = r-1
        b = r+1
        if a in _lost:
            _lost.remove(a)
        elif b in _lost:
            _lost.remove(b)
    
    return n - len(_lost)