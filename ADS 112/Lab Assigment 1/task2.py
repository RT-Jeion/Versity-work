def det(m):
    new_list = []
    for i in m:         # taking the rows one by one
        for j in i:     # taking the values fo each row one by one
            new_list.append(j)      # appending every values in a linear new list
    result = new_list[0]*new_list[3] - new_list[1]*new_list[2]      # applying the determination rules fo 2 x 2 metrix
    return result

metrix = [[4,5],[2,3]]

ans = det(metrix)

print(ans)