def metrix_subtraction(m1, m2): # defined the function
    result = []                 # created an empty list to store the new Metrix

    for i in range(len(m1)):    # taking every row one by one
        row = []
        for j in range(len(m1[i])): # taking every value of that each row one by one
            row.append(m2[i][j] - m1[i][j])         # appending new values for each row
        result.append(row)          # appending the new row
    return result

metrix1 = [[1,2,3],[4,5,6],[7,8,9]]
metrix2 = [[10,11,12],[13,14,15],[16,17,18]]

print("Metrix no.1: ", metrix1, "\nMetrix no.2: ", metrix2, "\nSubstraction of 2 Metrix: ", end="")
print(metrix_subtraction(m1=metrix1, m2=metrix2))