def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(0, len(prices)-1):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[j] < prices[i]:
                break
    
    return answer