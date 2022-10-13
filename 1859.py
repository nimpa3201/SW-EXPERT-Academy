T = int(input())
for tc in range(1, T+1):
    # 자연수 N의 개수 입력
    n= int(input())
    # N 리스트 입력
    arr= list(map(int, input().split()))
    tmp = arr[-1]
    ans =0 
    for i in range(n-1,-1,-1):
        if arr[i] > tmp:
            tmp =arr[i]
        else:
            ans += tmp - arr[i]
    print('#{} {}'.format(tc,ans))
        