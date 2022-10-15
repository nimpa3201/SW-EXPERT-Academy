T = 10
for _ in range(T):
    num = int(input())
    query = input()
    s = input()
    m = len(query)
    cnt=0
    for i in range (len(s)):
        if s[i:i+m] == query:
            cnt+=1
    print("#{} {}".format(num,cnt))
