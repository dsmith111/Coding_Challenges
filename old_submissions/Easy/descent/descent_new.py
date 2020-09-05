import sys
import math

mountain_h = {}
# game loop
while True:
    for i in range(8):
        mountain_h.update({int(input()) : i})  # represents the height of one mountain.
        
    print(mountain_h[max(mountain_h)])
    mountain_h.pop(max(mountain_h))