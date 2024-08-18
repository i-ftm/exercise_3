def ckeck_equal(numbers):
    sum1 = sum(numbers)
    if sum1 % 2 != 0:
        return 'No'
    target = sum1 // 2
    if target in numbers :
        numbers.remove(target)
        s=sum(numbers)
        if s == target:
            return 'Yes'
        return 'No'
    # numbers.sort()
    a = list()
    for i in range(len(numbers)):
        a.append(numbers.pop())
        if sum(a) == target:
            return 'Yes'

    return 'No'

numbers = list(map(int, input().split()))
result = ckeck_equal(numbers)
print(result)

# sum1 = sum(numbers)
# if sum1 % 2 != 0:
#     return 'No'
# target = sum1 // 2
# dp_array = [False] * (target + 1)
# dp_array[0] = True
#
# for num in numbers:
#     for j in range(target, num - 1, -1):
#         dp_array[j] = dp_array[j] or dp_array[j - num]
#         print(j)
#         print(dp_array)
# return "Yes" if dp_array[target] else "No"
