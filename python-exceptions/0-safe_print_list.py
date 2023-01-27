

def safe_print_list(my_list=[], x=0):
    cnt = 0
    for i in range(x):
        try:
            if i == x - 1:
                print("{}".format(my_list[i]))
            else:
                print("{}".format(my_list[i]), end="")
            cnt += 1
        except IndexError:
            print()
            return cnt

    return cnt
