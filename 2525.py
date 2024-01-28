H, M = map(int, input().split())
t = int(input())

NM = (t+M)%60
NH = (H+((t+M)//60))%24

print(str(NH)+" "+str(NM))