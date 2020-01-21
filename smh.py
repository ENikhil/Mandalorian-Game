f = open("art.txt", "r")
data=f.read()
ascii=data.split('\n\n')
print(ascii[2][1])