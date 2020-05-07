def solution(brown, red):
    total_num = brown + red
    for num in range(2, int(total_num**0.5)+1):
        if total_num % num == 0:
            w = total_num // num
            h = num
            if brown == (2*w + 2*h - 4):
                return [w, h]