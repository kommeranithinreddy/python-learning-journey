fobj = open('number.txt', 'w')

for i in range(1, 11):
    fobj.write(f'{i}\n')

fobj.close()