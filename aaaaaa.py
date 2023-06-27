# Can generate random index with n values.
test_list = [1, 5, 9, 100, 23, 50, 3]


def bubble_sort(test_l):

    for i in range(len(test_l)):
            # 0 1 2 3 4 5 6
        for j in range(len(test_l) - i - 1):
                    # 7 - 0 - 1 = 6
                    # 0 1 2 3 4 5
                    # 7 - 1 - 1 = 5
            # Change position of two values if the lower index value is bigger than the higher index value.
            if test_l[j] > test_l[j+1]:
                #  1           5
                temp = test_l[j]
                # 
                test_l[j] = test_l[j+1]
                # 
                test_l[j+1] = temp
                # 
            # If not, do nothing.
            else:
                continue

    return test_l


print(bubble_sort(test_list))