# [Reference] https://itholic.github.io/kata-camouflage/
from collections import Counter
from functools import reduce

def solution(clothes):
    
    counter_each_category = Counter([cat for _,cat in clothes])
    check_list = [x+1 for x in list(counter_each_category.values())]
    answer = reduce(lambda x,y:x*y, check_list) - 1
    
    return answer