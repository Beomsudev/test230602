import random

"""
문제 1
• 1월 1일이 월요일인 어느 해가 있다고 가정한다.
• x 월과 y 일을 입력 받는다.
• x 월 y 일이 무슨 요일인지 출력하는 함수를 작성한다.
• 단, 윤년이 아니고, 양력을 기준으로 한다.
• time 관련 모듈 사용 금지.
(반복문과 조건문을 활용해주세요.)
"""
def find_day(month, day):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #각 달의 일수  1   2   3   4   5   6   7   8   9   10  11  12

    monday = 1
    tueday = 2
    wedday = 3
    thuday = 4
    friday = 5
    satday = 6
    sunday = 0
    # 7로 나눴을 때 나머지 일 경우 각각의 요일과 대응 됨

    i = 0
    total_day = 0

    if month != 1:
        while i < month - 1:
            total_day = total_day + month_list[i]
            i += 1

    total_day = total_day + day

    print("{}월 {}일".format(month, day))
    if total_day % 7 == monday:
        print("월요일")
    if total_day % 7 == tueday:
        print("화요일")
    if total_day % 7 == wedday:
        print("수요일")
    if total_day % 7 == thuday:
        print("목요일")
    if total_day % 7 == friday:
        print("금요일")
    if total_day % 7 == satday:
        print("토요일")
    if total_day % 7 == sunday:
        print("일요일")


month = int(input("몇 월 : "))
day = int(input("몇 일 : "))
find_day(month, day)  

# 문제1 끝!


"""
문제 2
• 임의의 숫자로 채운 n 길이의 리스트가 있다.
• 리스트의 숫자들을 정렬을 하려고 한다. 정렬하는 방법은 다음과 같다.
✓ 인덱스 0 부터 그 다음 인덱스의 숫자를 비교한다.
✓ 비교했을 때, 작은 숫자가 낮은 인덱스에 있도록 바꾼다.
✓ 한번 리스트를 모두 검사하면 우측에는 큰 수가 배치되게 된다. 확정된 숫자는 검사하지
않는다.
• 위 알고리즘을 함수로 만들고, 결과로 정렬된 리스트를 반환하도록 한다.
"""
# [10, 9, 8, 7, 6, 5, 4 ,3 ,2 1]

n = int(input("리스트 길이를 입력하세요 : "))
random_list = random.sample(range(0, n), n)

print("변경 전 리스트 : ", random_list)

list_len = int(len(random_list) / 2)
i = 0
while i < list_len:
    if random_list[i] > random_list[i+1]:
        random_list.insert(i+2, random_list[i])
        random_list.pop(i)
    i += 2


print("변경 후 리스트 : ", random_list)

# 문제2 끝!
