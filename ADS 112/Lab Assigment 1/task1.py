def metrix_subtraction(m1, m2): # defined the fucntion
    result = []                 # created an empty list to store the new Metrix

    for i in range(len(m1)):    # taking every row one by one
        row = []
        for j in range(len(m1[i])): # taking every value of that each row one by one
            row.append(m1[i][j] - m2[i][j])         # appending new values for each row
        result.append(row)          # appending the new row
    return result

metrix1 = [[1,2,3],[4,5,6],[7,8,9]]
metrix2 = [[10,11,12],[13,14,15],[16,17,18]]

print(metrix_subtraction(m1=metrix2, m2=metrix1))