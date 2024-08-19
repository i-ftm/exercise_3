def LCS(surce,target):
    x = len(surce)
    y = len(target)
    a = [[0 for j in range(y+1)] for i in range(x+1)]

    for i in range(1, x+1):
        for j in range(1, y+1):
            if surce[i-1] == target[j-1]:
                a[i][j] = a[i-1][j-1]+1
            else:
                a[i][j] = max(a[i-1][j], a[i][j-1])

    index = a[x][y]
    lcs = [""] * (index + 1)
    lcs[index] = ""

    i = x
    j = y
    while i > 0 and j > 0:
        if surce[i - 1] == target[j - 1]:
            lcs[index - 1] = surce[i - 1]
            index -= 1
            i -= 1
            j -= 1
        elif a[i - 1][j] > a[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs, a[x][y]

def best_subsequence(n,source_name):
    list_name = []
    for _ in range(n):
        list_name.append(input().strip())

    target_subsequence =""
    target_counter = 0


    for name in list_name:
        subsequence , counter = LCS(source_name,name)
        if counter > target_counter:
            target_counter = counter
            target_subsequence = "".join(subsequence)

    return target_subsequence, target_counter




name = input().strip()
n = int(input().strip())
subsequence, counter = best_subsequence(n,name)
print(subsequence)
print(counter)




