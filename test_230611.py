import numpy as np

# 문제 1
"""
특정 ndarray 를 정규화 하는 함수 생성

정규화 공식 : Z = ( X X 평균 ) / X 표준편차
함수의 매개변수는 (1) ndarray 와 (2) axis
axis 매개변수의 값이
    axis = 1 : 전체 값에 대한 정규화
    axis = 0 : row 별 정규화
    axis = 1 : column
별 정규화
"""
def normalizing(ndarray, ax=-1):
    if ax == -1:
        z = (ndarray - np.mean(ndarray)) / np.std(ndarray)

    if ax == 0:
        z = (ndarray - np.mean(ndarray, axis=0)) / np.std(ndarray, axis=0)

    if ax == 1:
        tp_mean = np.reshape((np.mean(ndarray, axis=1)), (np.shape(ndarray)[0], 1))
        tp_std = np.reshape((np.std(ndarray, axis=1)), (np.shape(ndarray)[0], 1))

        z = (ndarray - tp_mean) / tp_std

    # print(z)
    return z

spl_ndarray = np.random.randint(-5, 5, size=(5, 5))
print(spl_ndarray)



a = normalizing(spl_ndarray, ax=1)
print(a)

# 문제2
"""
Sorting : 평균에 가까운 순서대로 오름차순 나열

행 벡터를 입력 받음
argmin, argmax, minimum, maximum, mean, abs 등을 활용
동일한 가까운 정도라면 작은 숫자를 먼저 나열
Sorting 전과 후의 배열을 출력
"""

a = np.array([5, 8, 22, -13, 6, 24, 53, 72, 4])
print("*****")
print(a)

a_zero = np.zeros_like(a)
print("*****")
print(a_zero)

sort = np.abs(a-np.mean(a))
print("*****")
print(sort)

sort_num = np.zeros_like(a)
print("*****")
print(sort_num)

for i in range(np.shape(a)[0]):
    arg = np.argmin(sort)
    a_zero[i] = a[arg]
    sort_num[arg] = i
    sort[arg] = np.max(sort)+1

print("평균  값 : ", np.mean(a))
print("sort 전 : ", a)
print("sort 후 : ", a_zero)

# 문제3
"""
거리 구하기
    임의의 동일한 길이를 가진 행 벡터 2 개를 생성 . numpy.random
    해밍 거리는 계산 하기 전에 다음을 진행해서 행 벡터 변형
    2개의 행 벡터에 대해서 정규화 문제 1 의 공식 참고
    numpy.ceil를 사용해서 정수화
    numpy.logical_or과 numpy.zeros_like 를 사용해서 0 이 아니면 모두 참이 되게 변형

거리 계산
    맨해튼 거리 : 𝑑𝑚=𝑥1−𝑥2+𝑦1−𝑦2+𝑧1−𝑧2+⋯
    유클리디언 거리 : 𝑑𝑢=𝑥1−𝑥22+𝑦1−𝑦22+𝑧1−𝑧22+⋯
    해밍 거리 : 0 과 1 로 이루어진 배열에 대해 𝑥1−𝑥2+𝑦1−𝑦2+𝑧1−𝑧2+⋯
"""
a = np.random.randint(0, 100, size=(1, 5))
b = np.random.randint(0, 100, size=(1, 5))

# Manhattan
print("맨해튼")
print(np.sum(np.abs(a - b)))

# Euclidean
print("유클리디언")
print(np.sqrt(np.sum(a - b) ** 2))

# Hamming
print("해밍")
norm_a = np.logical_or(np.ceil((a - np.mean(a)) / np.std(a)), np.zeros_like(a))
norm_b = np.logical_or(np.ceil((b - np.mean(b)) / np.std(b)), np.zeros_like(b))

print(np.logical_xor(norm_a, norm_b))
print(np.sum(np.logical_xor(norm_a, norm_b)))