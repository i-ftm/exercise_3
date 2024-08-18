def ckeck_equal(numbers):
    sum1 = sum(numbers)
    if sum1 % 2 != 0:
        return 'No'
    target = sum1 // 2
    dp_array = [False] * (target + 1)
    dp_array[0] = True

    for num in numbers:
        for j in range(target, num - 1, -1):
            dp_array[j] = dp_array[j] or dp_array[j - num]
            print(j)
    return "Yes" if dp_array[target] else "No"

numbers = list(map(int, input().split()))
result = ckeck_equal(numbers)
print(result)





