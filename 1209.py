T = 10
for _ in range(T):
    n = int(input())
    grid = [ list(map(int,input().split()))for _ in range(100)]
    c=0
    d =0
    ans1 =0
    ans2=0

    for i in range(len(grid[0])):  
        a =0
        b=0
        for j in range(len(grid[0])):
            a += grid[i][j] # 행 기준 합
            b += grid [j][i] # 열 기준 합
            if i == j:
                c += grid[i][j] # 대각선 합 (동남) 
            if len(grid)-1-i == j:
                d += grid[i][j] # 대각선 합 (서남)
        ans1 = max(ans1,a)
        ans2 = max(ans2,b)

    print("#{} {}".format(n,max(ans1,ans2,c,d)))
