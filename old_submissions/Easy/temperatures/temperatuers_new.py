import sys
import math

n = int(input())  # the number of temperatures to analyse
t = {}

for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t.update({i : int(i)})
    
t_index = sorted(t, key = lambda key: ~abs(t[key]))
t_index = list(map(t.get, t_index))
t_final = list(filter(lambda val: abs(val) == abs(t_index[-1]), t_index))

if len(t_final) == 0:
    t_final.append(0)

print(max(t_final))

