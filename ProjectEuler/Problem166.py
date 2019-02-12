#Criss Cross

def check_if_works(matrix, e):
    #check rows
    for row in matrix:
        if sum(row) != e:
            return False
    #check columns
    for i in range(4):
        summ = 0
        for d in range(4):
            summ += matrix[d][i]
        if summ != e:
            return False
    #check diagonals
    summ = 0
    sumb = 0
    for i in range(4):
        summ += matrix[i][i]
        sumb += matrix[i][3 - i]
    if summ != e or sumb !=e:
        return False
    return True

matrix = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
list = []

for e in range(0,37):
    max = e + 1
    for a in range(max):
        matrix[0][0] = a
        for b in range(max):
            matrix[0][1] = b
            for c in range(max):
                matrix[0][2] = c
                for d in range(max):
                    matrix[0][3] = d
                    for f in range(max):
                        matrix[1][0] = f
                        for g in range(max):
                            matrix[1][1] = g
                            for h in range(max):
                                matrix[1][2] = h
                                for i in range(max):
                                    matrix[1][3] = i
                                    for k in range(max):
                                        matrix[2][0] = k
                                        for l in range(max):
                                            matrix[2][1] = l
                                            for m in range(max):
                                                matrix[2][2] = m
                                                for n in range(max):
                                                    matrix[2][3] = n
                                                    for o in range(max):
                                                        matrix[3][0] = o
                                                        for p in range(max):
                                                            matrix[3][1] = p
                                                            for q in range(max):
                                                                matrix[3][2] = q
                                                                for r in range(max):
                                                                    matrix[3][3] = r
                                                                    if check_if_works(matrix, e) == True:
                                                                        list.append(matrix)
                                                                        print(matrix)



for element in list:
    print(element)
