
a = 0
while a < 10:
    
    a = a+1
    a += 1
    print(a)

print("*****")

for i in range(0, 10):
    print(i)
    for j in range(0, 10):
        print(j)

test_list = [0, "범수", "두나", 2]

empty_list = []

for i in test_list:
    print(i)
    empty_list.append(i)

print(empty_list)

             # i  j
test_list2 = [(9, 1), (2, 3), (6, 4)]
#   0  1
for a, b in test_list2:
    print(a)
    print(b)