# data = [
#     {
#         "name1": "Sat,Sun,Mon",
#         "name2": "Sat1,Sun1,Mon",
#         "qty": 150
#     },
#     {
#         "name1": "Tue,Wed,Thr",
#         "name2": "Sat1,Sun,Mon1",
#         "qty": 200
#     },
    
# ]

# ans = {}

# for i in data:
#     for key, value in i.items():
#         if key == 'qty':
#             continue
#         names = value.split(',')
#         for j in names:
#             if j in ans:
#                 ans[j] += i['qty']
#             else:
#                 ans[j] = i['qty']   

# print(ans) 

A = ['d1', 'd5', 'd6']    
B = ['d1', 'd3', 'd4']
C = ['d2', 'd3', 'd5']
D = ['d6', 'd2', 'd3']

# fuse(l1, l2, l3, ...)
def fuse(k, *l):
    scores = {}
    for i in l:
        for rank, v in enumerate(i):
            scores[v] = scores.get(v, 0) + 1/(k + rank + 1)
    
    # for rank, v in enumerate(B):
    #     scores[v] = scores.get(v, 0) + 1/(k + rank + 1)
        
    temp = []
    for key, val in scores.items():
        temp.append([val, key])
        
    temp.sort();
    temp = temp[::-1]
    
    ans = []
    for _, j in temp:
        ans.append(j)
    
    return ans

print(fuse(60, A, B, C, D))
