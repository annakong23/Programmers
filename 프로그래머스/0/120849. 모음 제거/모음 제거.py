def solution(my_string):
    moeum = ['a','e','i','o','u']
    for m in moeum:
        my_string = my_string.replace(m,'')
    return my_string