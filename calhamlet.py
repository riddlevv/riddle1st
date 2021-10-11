def gettext():
    txt = open("hamlet.txt","r").read() #一定要在同一个文件夹中嘛
    txt = txt.lower()
    for ch in '!"#$%^&*()+-,./:;<=>?@[\\]_`{|}~':  #`的位置
        txt = txt.replace(ch," ")
    return txt
hamlettxt = gettext()
words = hamlettxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1
item = list(counts.items())
item.sort(key=lambda x:x[1],reverse = True)
for i in range(10):
    word,count = item[i]
    print("{0:<10}{1:>5}".format(word,count))
