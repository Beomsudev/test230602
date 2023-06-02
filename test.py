import numpy as np
import random

print("hello")
"""
  1. 지뢰찾기 맵의 사이즈를 결정하는 n 값을 입력받음.
  2. n 값을 가지고, n x n 형태의 0 으로 초기화 된 ndarray  생성.
  3. 랜덤하게 m 개의 숫자 페어를 생성.
m 은 숫자 n 의 0.3 배를 내림한 수.
숫자 페어는 ( a, b ) 형태로, 숫자 a와 b는 0 ~ n-1 까지의 수. 
  4. 랜덤하게 만든 m 개의 숫자 페어가 곧 ndarray 위의 지뢰 위치.
  5. 지뢰위치는 숫자 100으로 그 외에는 옆에 위치한 지뢰의 갯수로 숫자를 변경해주세요.

"""

in_num = int(10)

ran_nd = np.zeros((in_num, in_num))
print(ran_nd)

m = int(in_num * 0.3)
print(m)

ran_a = []
ran_b = []

for i in range(m):
    a =random.randrange(0, in_num)
    ran_a.append(a)

print(ran_a)

for i in range(m):
    b =random.randrange(0, in_num)
    ran_b.append(b)

print(ran_b)

for i in range(m):

    xm = ran_a[i] - 1
    xp = ran_a[i] + 1
    x0 = ran_a[i]

    ym = ran_b[i] - 1
    yp = ran_b[i] + 1
    y0 = ran_b[i]



    n1 = (xm, ym)
    n2 = (x0, ym)
    n3 = (xp, ym)
    n4 = (xm, y0)
    n5 = (x0, y0)
    n6 = (xp, y0)
    n7 = (xm, yp)
    n8 = (x0, yp)
    n9 = (xp, yp)
    if xm < 0 or xp > in_num or ym < 0 or yp > in_num:

        ran_nd[n1] += 1
        ran_nd[n2] += 1
        ran_nd[n3] += 1
        ran_nd[n4] += 1
        
        ran_nd[n6] += 1
        ran_nd[n7] += 1
        ran_nd[n8] += 1
        ran_nd[n9] += 1

    mine = (x0, y0)
    ran_nd[mine] = 100    

print(ran_nd)