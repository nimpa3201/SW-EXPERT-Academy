t= int(input())
for t in range(1, t+1):
    n = int(input())
    arr =[ [0 for _ in range(n)] for _ in range(n)] 
    x,y = 0,0
    dxs, dys = [0,1,0,-1],[1,0,-1,0]
    arr[x][y] =1
    direct = 0
    def is_range(x,y):
        return 0<=x<n and 0<=y<n
    for i in range(2,n*n+1):
        nx = x+dxs[direct] 
        ny = y+dys[direct]
        if not is_range(nx,ny) or arr[nx][ny]  != 0 :
            direct = (direct+1)%4
        x,y = x + dxs[direct] ,y+dys[direct]
        arr[x][y] =i
    print('#'+str(t))
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end =' ')
        print()