max_list=[]
for i in range(9):
    max_list.append(int(input()))
    
print(max(max_list), max_list.index(max(max_list))+1)
