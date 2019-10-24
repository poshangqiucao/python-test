fs = open('test.txt','r')
fs1 = open('test1.txt','w')
line = fs.read().split("\t")

for word in line:
    words = word.split("\n")
    for item in words:
        fs1.write(item+"\n")
fs.close()
fs1.close()