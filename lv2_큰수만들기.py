# [Reference] https://gurumee92.tistory.com/162

def solution(number, k):
    collected = []
    
    for (i, num) in enumerate(number):
        while collected and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        
        if k == 0:
            collected += number[i:]
        
        collected.append(num)
    
    collected = collected[:-k] if k > 0 else collected
    answer = "".join(collected)
    return answer