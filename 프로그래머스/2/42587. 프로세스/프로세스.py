# from collections import deque

# def solution(priorities, location):
#     answer = 0
#     queue = deque([(i,p) for i,p in enumerate(priorities)])
    
#     while queue:
#         idx, priority = queue.popleft()
        
#         if any(priority<q[1] for q in queue):
#             queue.append((idx, priority))
#         else:
#             answer += 1
            
#             if idx == location:
#                 return answer

from collections import deque

def solution(priorities, location):
    queue = deque([(i,p) for i,p in enumerate(priorities)])
    order = 0
    
    while queue:
        idx, priority = queue.popleft()
        
        if queue and priority < max(q[1] for q in queue):
            queue.append((idx, priority))
        else:
            order += 1
            if idx == location:
                return order










