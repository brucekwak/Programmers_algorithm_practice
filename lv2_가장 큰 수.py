# [풀이-1] 숫자를 string 으로 변환 후, 사전순으로 정렬하는 아이디어
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    return str(int(''.join(numbers)))
	

# [풀이-2] 비교함수 정의하고, sorted 에 functools.cmp_to_key 활용
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))
    # t1이 크다면 1, t2가 크다면 -1, 같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    # 파이썬 3; 정의한 비교함수를 key 함수로 변환
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    return str(int(''.join(n)))