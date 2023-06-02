import numpy as np

#1
n = int(input("맵 크기를 입력하세요: "))

#2
m = int(n*0.3)

#3
map = np.zeros((n,n), dtype=np.int8)
tmt_pos = np.random.randint(0, n, size=(m,2), dtype=np.int8).tolist()
# tmt_pos = np.array([[1,2],[1,2],[1,2]], dtype=np.int8).tolist()
print(tmt_pos)

#4
for posX, posY in tmt_pos:
    if map[posX][posY] == 100: # 이미 지뢰가 설치되어 있으면 새로운 지뢰 위치를 추가.
        tmt_pos.append(np.random.randint(0, n, size=2, dtype=np.int8).tolist())
        continue
    map[posX][posY] = 100
    #5
    for x in range(posX-1, posX+2):
        for y in range(posY-1, posY+2):
            if x < 0 or x >= n: continue # 맵 크기를 벗어난 위치 예외 처리
            if y < 0 or y >= n: continue # 맵 크기를 벗어난 위치 예외 처리
            if map[x][y] == 100: continue # 지뢰가 설치되어 있는 위치 예외 처리
            map[x][y] += 1

print(map)