# [풀이-1] 에라토스테네스의 체 활용
from itertools import permutations

def solution(numbers):
    # 숫자 조합 구축
    num_list = []
    for size in range(1, len(numbers)+1):
        check_list = permutations(list(range(len(numbers))), size)
        for check in check_list:
            check_num = ''.join([numbers[ind] for ind in check])
            num_list.append(int(check_num))
    num_list = list(set(num_list))

    # max 값으로 에라토스테네스의 체 구축
    max_num = max(num_list)
    era_sieve = [True for _ in range(max_num+1)]  # 0 ~ max_num
    era_sieve[0] = False
    era_sieve[1] = False
    for i in range(4, max_num+1, 2):
        era_sieve[i] = False
    for i in range(3, max_num+1, 2):
        if era_sieve[i] == True:
            for j in range(i*2, max_num+1, i):
                era_sieve[j] = False
    
    # 소수 찾기
    prime_list = []
    for num in num_list:
        if era_sieve[num] == True:
            prime_list.append(num)
    
    answer = len(prime_list)

    return answer


# [풀이-2] 에라토스테네스의 체 -> 코드 간결
from itertools import permutations

def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i+1))))
    a -= set(range(2))
    for i in range(2, int(max(a)**0.5+1)):
        a -= set(range(i*2, max(a) + 1, i))
    
    return len(a)