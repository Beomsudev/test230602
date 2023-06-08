import numpy as np
import random

"""
  1. 지뢰찾기 맵의 사이즈를 결정하는 n 값을 입력받음.
  2. n 값을 가지고, n x n 형태의 0 으로 초기화 된 ndarray  생성.
  3. 랜덤하게 m 개의 숫자 페어를 생성.
m 은 숫자 n 의 0.3 배를 내림한 수.
숫자 페어는 ( a, b ) 형태로, 숫자 a와 b는 0 ~ n-1 까지의 수. 
  4. 랜덤하게 만든 m 개의 숫자 페어가 곧 ndarray 위의 지뢰 위치.
  5. 지뢰위치는 숫자 100으로 그 외에는 옆에 위치한 지뢰의 갯수로 숫자를 변경해주세요.
"""

n = int(input("맵의 사이즈를 입력 하세요 : "))
# n = 4
nd_map = np.zeros((n, n), dtype=np.int8)
# 2번 클리어

m = int(n * 0.3) # m = 3
pos_list = []

for i in range(m):
    x = random.randrange(0, n)
    y = random.randrange(0, n)
    pos = (x, y)
    pos_list.append(pos)


for x_pos, y_pos in pos_list:
    if nd_map[x_pos, y_pos] == 100:
        x = random.randrange(0, n)
        y = random.randrange(0, n)
        pos = (x, y)
        pos_list.append(pos)
        continue
    nd_map[x_pos, y_pos] = 100



near_mine = []
for x in range(n):
    for y in range(n):
        ma = nd_map[x, y]
        if ma == 100:
            for k in range(x-1, x+2):
                for l in range(y-1, y+2):
                    if k < 0 or k >= n: # 4
                        continue
                    if l < 0 or l >= n:
                        continue
                    near_mine.append((k, l))
for i in range(len(near_mine)):
    nd_map[near_mine[i]] += 1

for x_pos, y_pos in pos_list:
    nd_map[x_pos, y_pos] = 100    

print(nd_map)