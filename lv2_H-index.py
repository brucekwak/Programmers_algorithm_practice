# [풀이-1]
def solution(citations):
    citations_sorted = sorted(citations)
    
    h_index = 0
    for check_val in range(citations_sorted[-1]):
        for i, c in enumerate(citations_sorted):
            if c >= check_val:
                if (len(citations_sorted)-i >= check_val) and (i <= check_val):
                    h_index = check_val
    
    return h_index

# [풀이-2]
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] > l-i:
            return l-i
    return 0
