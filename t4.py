numbers = list(map(int, input().split()))
numbers.sort()
while True:
    a = [numbers.pop()]
    if sum(numbers) == sum(a):
        print('Yes')
        break
    print('No')
    break
