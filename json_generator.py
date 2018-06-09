import numpy as np
import pandas as pd
user_id = []
n = 100
file = open("C:\\Users\\80693\\Desktop\\User_name.txt")
lines = file.readlines()
file.close()


for line in lines:
    line = line.strip().split('\t')
    line = [i.replace(" ", "_") for i in line]
    line = [i.replace("·", "_") for i in line]
    user_id.append(line[0])

link = pd.read_csv('C:\\Users\\80693\\Desktop\\link.csv', header=None)
np.array(link)

f = open("C:\\Users\\80693\\Desktop\\zhihu-imports.txt", "w")
f.write('[')
for i in range(n):
    f.write('{\n"name":"zhihu.%s",\n "imports":[\n' % user_id[i])
    flag = 1
    for j in range(n):
        if link[i][j] == 1:
            if flag == 0:
                f.write(',')
            if flag == 1:
                flag = 0
            f.write('"zhihu.%s"\n' % user_id[j])
    if i == n - 1:
        f.write(']\n}\n')
    else:
        f.write(']\n},\n')
f.write(']')
f.close()
