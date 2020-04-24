def solution(K, travel):
    maximum_visit = [-1] * (K+1)
    candi_list = [travel[0][:2], travel[0][2:]]
    
    if candi_list[0][0] == candi_list[1][0]:
        maximum_visit[candi_list[0][0]] = min([candi_list[0][1], candi_list[1][1]])
    else:
        maximum_visit[candi_list[0][0]] = candi_list[0][1]        
        maximum_visit[candi_list[1][0]] = candi_list[1][1]    
    
    maximum = -1
    for ind, next_info in enumerate(travel[1:]):
        next_candi_list = []
        for candi_i in candi_list:
            # candi_i 에 대해,
            next_info_1, next_info_2 = next_info[:2], next_info[2:]
            temp_1 = [candi_i[0] + next_info_1[0], candi_i[1] + next_info_1[1]]
            temp_2 = [candi_i[0] + next_info_2[0], candi_i[1] + next_info_2[1]]
            if temp_1[0] <= K:
                next_candi_list.append(temp_1)
                maximum_visit[temp_1[0]] = max(temp_1[1], maximum_visit[temp_1[0]])
            if temp_2[0] <= K:
                next_candi_list.append(temp_2)
                maximum_visit[temp_2[0]] = max(temp_2[1], maximum_visit[temp_2[0]])
        
        final_candi_list = [time for time, value in next_candi_list]
        candi_list = [[x, maximum_visit[x]] for x in list(set(final_candi_list))]
        maximum_visit = [-1] * (K+1)
        
        if ind == (len(travel[1:])-1):
            maximum = max([value for time, value in candi_list])
        
    return maximum