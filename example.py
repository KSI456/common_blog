import math
def cal(n,times,right,zero,k):
    while True:
        middle = math.floor((right+zero)/2)
        time = [math.floor(middle/x) for x in times]
        total = 0
        for j in time:
            total+=j
        if n!=total and k==1:
            return middle+1
        if n<total:
            right=middle
        elif n>total:
            zero=middle
        else:
            k=1
            return cal(n,times,right-1,zero-1,k)
def solution(n, times):
    zero=1
    right = max(times)*n
    k=0
    return cal(n,times,right,zero,k)

n=6
times = [7,10]
print(solution(n,times))