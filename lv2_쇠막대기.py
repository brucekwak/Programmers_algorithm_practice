# [풀이-1] str.replace() 없이
def solution(arrangement):
    answer = 0
    cumul_stick = 0
    
    i = 0
    stick_num = 0
    while i <= (len(arrangement)-2):
        if arrangement[i:i+2] == '()':
            answer += cumul_stick
            i += 2
        elif arrangement[i] == '(':
            cumul_stick += 1
            i += 1
        elif arrangement[i] == ')':
            cumul_stick -= 1
            i += 1
            stick_num += 1
    if i == (len(arrangement)-1):
        stick_num += 1
    answer += stick_num
    
    return answer

# [풀이-2] str.replace() 활용
def solution(arrangement):
    answer = 0
    stick = 0
    laser_to_zero = arrangement.replace('()', '0')

    for str_i in laser_to_zero:
        if str_i == '(':
            stick += 1
        elif str_i == ')':
            stick -= 1
            answer += 1
        elif str_i == '0':
            answer += stick
    
    return answer