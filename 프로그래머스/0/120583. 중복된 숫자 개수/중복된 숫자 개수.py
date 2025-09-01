def solution(array, n):
    return sum(array[i]==n for i in range(len(array)))