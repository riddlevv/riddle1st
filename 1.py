s = "Hello World"
n = int(input())
if n==0:
    print(s)
elif n>0:
    st =""
    for n in range(len(s)):
        if(n+1)%2 != 0:
            st = st+s[n]
            if len(s)==(n+1):
                print(st)
        else:
            st = st+s[n]
            print(st)
            st=""
else:
    for n in s:
        print(n)
