def kthTerm(n, k):
    if n not in range(2,31) or k not in range(1, 101):
        raise Exception("Wrong input value. Must be: 2 ≤ n ≤ 30 and 1 ≤ k ≤ 100")

    my_list = []
    count = 0
    while len(my_list) < k:
        if count == 0:
            val = 1
            my_list.append(val)
            count += 1
        else:
            val = n**count
            my_list.append(val)
            for i in my_list:
                if i == val:
                    break
                else:
                    val_p = val + i
                    my_list.append(val_p)

            count += 1

    return my_list[k-1]




print(kthTerm(3, 4))