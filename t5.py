def division_labor(n):
    di_list=[]
    for _ in range(n):
        di_list.append(int(input()))
    target = sum(di_list)//3

    a = [False for i in range(target+1)]
    a[0] = True
    for d in di_list:
        for i in range(target, d-1, -1):
            a[i]= a[i] or a[i-d]

    for i in range(target, -1, -1):
        if a[i]:
            d_kambiz = i
            break

    d_all= d_kambiz * 3
    difference = abs(sum(di_list)-d_all)
    return difference

n = int(input())
difference = division_labor(n)
print(difference)