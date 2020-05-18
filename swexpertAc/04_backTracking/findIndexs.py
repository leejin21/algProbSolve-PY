# findIndexs.py
# 왜 +1을 해야 하는 지 규명하지 못함(아직)



def findIndexs(l, num):
    # find indexs of num in list l
    pre_idx = -1; idx_list = 0
    idx_list = []
    for _i in range(l.count(num)):
        temp = pre_idx+ l[pre_idx+1:].index(num) + 1
        idx_list.append(temp)
        pre_idx = temp
    
    return idx_list

print(findIndexs([1,2,3,3,5,3,3], 3))