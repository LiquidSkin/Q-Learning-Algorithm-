a = [[1, 2], [2, 3]]
list =[]
for i in range(2):
    a = []
    for j in range(2):
        a.append(a[i][j])
    list.append(a)


print(list)