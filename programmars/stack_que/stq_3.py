from collections import Counter

def solution(progresses, speeds):
    pr_max = 0
    ans = [0]*len(progresses)
    for i in range(len(progresses)):
        remain = 100-progresses[i]; days = remain // speeds[i]
        if remain % speeds[i] != 0:
            days += 1
        ans[i], pr_max = (pr_max, pr_max) if pr_max > days else (days, days)
    return list(Counter(ans).values())


print(solution([93,30,55], [1,30,5]))