def solution(arr):
    if (len(arr) > 1):
        te = arr.index(min(list(map(int, arr))))
        arr.pop(te)
        return arr
    else:
        return [-1]


print (solution([4,3,2,1]))