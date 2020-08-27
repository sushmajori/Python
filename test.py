s= input()
k=int(input())
charValue=input()
a=""
for i in range (len(s)):
    b= ord(s[i]-97)
    a=a+charvalue[b]
    maximum = -1
    count = 0
    for i in range(len(s)):
        if(count > k):
            break
        else:
            if(a[j]=='0' and count == k):
                count = count +1
            elif (a[j]=='0' and count !=k):
                count = count + 1
                sub = sub + 1
            else :
                sub = sub + 1
    count = 0
    if(sub > maximum):
        maximum = sub
    print(maximum)
