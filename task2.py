def det(m):
    new_list = []
    for i in m:
        for j in i:
            new_list.append(j)
    result = new_list[0]*new_list[3] - new_list[1]*new_list[2]
    return result

metrix = [[4,5],[2,3]]

ans = det(metrix)

print(ans)