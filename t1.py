def free_competition(n , times):
    contests = []
    for i in range(n):
        s = times[2 * i]
        e = times[2 * i + 1]
        contests.append((s, e))
    contests.sort(key= lambda x:x[1]) #چون دیر تر تموم شده ینی اخر همه به خاطر همین براساس زمان پایان مرتب میکنیم
    last_end_time = -1
    max_count = 0
    for start, end in contests:
        if start >= last_end_time:
            max_count +=1
            last_end_time= end

    print(max_count)

n = int(input())
times = list(map(int, input().split()))
free_competition(n,times)
