def metrix_subtraction(m1, m2):
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[i])):
            row.append(m1[i][j] - m2[i][j])
        result.append(row)
    return result

metrix1 = [[1,2,3],[4,5,6],[7,8,9]]
metrix2 = [[10,11,12],[13,14,15],[16,17,18]]

print(metrix_subtraction(m1=metrix2, m2=metrix1))