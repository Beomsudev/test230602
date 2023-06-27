import numpy as np

### 1. 지뢰찾기 맵의 사이즈를 결정하는 n 값을 입력받음.
# n = int(input("지뢰찾기 맵 사이즈를 입력하세요.: "))
n = 10
### 2. n 값을 가지고, n x n 형태의 0 으로 초기화 된 ndarray  생성
nd_map = np.zeros((n,n), dtype=np.int8)
print(nd_map)
### 3. 랜덤하게 m 개의 숫자 페어를 생성. / m 은 숫자 n 의 0.3 배를 내림한 수. / 숫자 페어는 ( a, b ) 형태로, 숫자 a와 b는 0 ~ n-1 까지의 수.
m = int(n*0.3) 

### 4. 랜덤하게 만든 m 개의 숫자 페어가 곧 ndarray 위의 지뢰 위치.

pos_list = np.random.randint(0, n, size=(m,2), dtype=np.int8).tolist() # pos_list sample = [[2, 4], [7, 0], [7, 2]]
#                            0  9        3,2 
""""
[
 [8, 9],
 [9, 1],
 [6, 4]
]
a = [[2, 4], [7, 0], [7, 2]]
a[0] =  [2, 4]
a[0][0] = 2
"""

#                  [[2, 4], [2, 4], [7, 2]]
for y_pos, x_pos in pos_list:
    if nd_map[y_pos, x_pos] == 100: # 중복된 위치의 지뢰는 다른 위치로 변경
        pos_list.append(np.random.randint(0, n, size=2, dtype=np.int8).tolist())
        continue

    ### 5. 지뢰위치는 숫자 100으로 그 외에는 옆에 위치한 지뢰의 갯수로 숫자를 변경해주세요.
    for y in range(y_pos-1, y_pos+2):
        for x in range(x_pos-1, x_pos+2):
            if y < 0 or y >= n or x < 0 or x >= n: # 맵 밖의 좌표는 무시
                continue
            if nd_map[y, x] == 100: # 지뢰의 좌표는 무시
                continue
            nd_map[y, x] += 1
    nd_map[y_pos, x_pos] = 100


### 추가 디테일. 지뢰의 갯수와 m의 갯수 비교하여 같을 시에만 출력
mine_count = 0
for y in range(n):
    for x in range(n):
        if nd_map[y, x] == 100:
            mine_count += 1

if mine_count == m:
    print("* "*n*2)
    print(nd_map)
    print("* "*n*2)
    print("총 지뢰 갯수 : {} 입니다.".format(mine_count))

"""

결과값 예시 (n = 10일 경우)
* * * * * * * * * * * * * * * * * * * * 
[[  0   0   0   0   0   0   0   0   1   1]
 [  0   0   0   0   0   0   0   0   1 100]
 [  0   0   0   0   0   0   1   1   2   1]
 [  0   0   0   0   0   0   1 100   1   0]
 [  0   0   0   0   0   0   1   1   1   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  1   1   0   0   0   0   0   0   0   0]
 [100   1   0   0   0   0   0   0   0   0]
 [  1   1   0   0   0   0   0   0   0   0]]
* * * * * * * * * * * * * * * * * * * *
총 지뢰 갯수 : 3 입니다.
"""