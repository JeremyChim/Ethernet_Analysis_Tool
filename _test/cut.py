lst = '1234567890'

len = [2,1,3,4]

a = 0
for i in len:
    b = a + i
    c = lst[a:b]
    a = b
    print(c)