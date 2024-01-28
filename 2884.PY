H, M = map(int, input().split())

if H==0 and M<45:
    print(str(23)+" "+str(M+15))

elif H>0 and M<45:
    print(str(H-1)+" "+str(M+15))

else:
    print(str(H)+" "+str(M-45))