import sys
import math

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
current_x, current_y = (initial_tx, initial_ty)
# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    x, y = (0, 0)
    x_dict = {1: 'E', -1: 'W', 0: ''}
    y_dict = {1: 'S', -1: 'N', 0: ''}
    if current_x < light_x:
        x = 1
        current_x += x
    elif current_x > light_x:
        x = -1
        current_x += x
    if current_y < light_y:
        y = 1
        current_y += y
    elif current_y > light_y:
        y = -1
        current_y += y
    print("".join([y_dict[y], x_dict[x]]))
