from collections import defaultdict
from heapq import heappush, heappop

def solution(genres, plays):
    answer = []
    
    # 1. 장르별 총 재생시간
    play_time_dict = defaultdict(int)
    sort_dict_list = defaultdict(list)
    for ind, genre in enumerate(genres):
        play_time_dict[genre] += plays[ind]
        sort_dict_list[genre].append((plays[ind], ind))
    
    # 2. 높은 장르부터 장르 내 곡들을 재생시간별로 정렬 후 1, 2번째 곡 추가
    #    재생시간 같을 경우, 고유 번호 빠른 것부터
    genre_list = list(play_time_dict.keys())
    genre_list = sorted(genre_list, key=(lambda x:play_time_dict[x]), reverse=True)
    for genre in genre_list:
        check_list = sorted(sort_dict_list[genre], key=(lambda x:x[0]), reverse=True)
        if len(check_list) >= 2:
            answer += [check_list[0][1], check_list[1][1]]
        else:
            answer += [check_list[0][1]]
    
    return answer