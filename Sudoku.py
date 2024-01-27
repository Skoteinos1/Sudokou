# This code can solve up to Hard Sudokus from websudoku.com

# Define working variables
tab = [[[0 for k in range(9)] for j in range(9)] for i in range(11)]
pos = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
rows = 9*[0]
cols = 9*[0]

"""tab[0][0] = [0, 0, 0,  0, 0, 0,  0, 0, 0]
tab[0][1] = [0, 0, 0,  0, 0, 0,  0, 0, 0]
tab[0][2] = [0, 0, 0,  0, 0, 0,  0, 0, 0]

tab[0][3] = [0, 0, 0,  0, 0, 0,  0, 0, 0]
tab[0][4] = [0, 0, 0,  0, 0, 0,  0, 0, 0]
tab[0][5] = [0, 0, 0,  0, 0, 0,  0, 0, 0]

tab[0][6] = [0, 0, 0,  0, 0, 0,  0, 0, 0]
tab[0][7] = [0, 0, 0,  0, 0, 0,  0, 0, 0]
tab[0][8] = [0, 0, 0,  0, 0, 0,  0, 0, 0]"""

tab[0][0] = [1, 0, 0,  0, 3, 8,  4, 0, 0]
tab[0][1] = [0, 4, 0,  1, 0, 0,  0, 3, 0]
tab[0][2] = [0, 6, 0,  0, 4, 0,  0, 2, 0]

tab[0][3] = [0, 0, 0,  0, 0, 0,  2, 5, 0]
tab[0][4] = [0, 0, 4,  5, 0, 7,  3, 0, 0]
tab[0][5] = [0, 3, 1,  0, 0, 0,  0, 0, 0]

tab[0][6] = [0, 8, 0,  0, 1, 0,  0, 4, 0]
tab[0][7] = [0, 1, 0,  0, 0, 9,  0, 7, 0]
tab[0][8] = [0, 0, 7,  4, 2, 0,  0, 0, 1]

added_new = True
while added_new:
    added_new = False
    for k in range(1, 10):
        # Checks which columns have current number
        in_col = 9*[0]
        for i in range(9):
            for j in range(9):
                if k == tab[0][i][j]:
                    in_col[j] = k
        # Based on rows and columns figures out if nmber can be placed in current cell
        for i in range(9):
            for j in range(9):
                empty = True
                if tab[0][i][j]:
                    empty = False
                if k in tab[0][i]:
                    empty = False
                if in_col[j]:
                    empty = False
                if empty:    
                    tab[k][i][j] = k
    
    # Check if nmber can be placed in current 3x3 square
    for k in range(1, 10):
        for p in pos:
            in_square = False
            for i in range(3):
                for j in range(3):
                    if tab[0][p[0]+i][p[1]+j] == k:
                        in_square = True
                if in_square:
                    break
            if in_square:
                for i in range(3):
                    for j in range(3):
                        tab[k][p[0]+i][p[1]+j] = 0   

    # Cleanup for square with all possible numbers
    for k in range(1,10):
        for i in range(9):
            for j in range(9):
                if tab[10][i][j] == 0:
                    tab[10][i][j] = ''
                if tab[k][i][j]:
                    tab[10][i][j] += str(tab[k][i][j])
    
    # Sets number in solution if there is only 1 possibility in current cell
    for i in range(9):
        for j in range(9):
            # print(tab[10][i][j])
            if len(tab[10][i][j]) == 1:
                tab[0][i][j] = int(tab[10][i][j])
                added_new = True
    
    # Sets number in solution if there is only 1 possibility in current row
    for k in range(1,10):
        for i in range(9):
            if tab[k][i].count(k) == 1:
                for j in range(9):
                    if tab[k][i][j]:
                        tab[0][i][j] = k
                        added_new = True
    
    # Sets number in solution if there is only 1 possibility in current column
    for k in range(1,10):
        for j in range(9):
            in_col = 9*[0]            
            for i in range(9):
                in_col[i] = tab[k][i][j]
            if in_col.count(k) == 1:
                 for i in range(9):
                    if tab[k][i][j]:
                        tab[0][i][j] = k
                        added_new = True

    # Clears working tab if number was found
    if added_new:
        for k in range(1,11):
            for i in range(9):
                for j in range(9):
                    tab[k][i][j] = 0
                
# Printout of results
# Prints 1 square with solved numbers and 9 squares with possible numbers
for k in range(0,10,5):
    for i in range(9):
        foo = str(tab[k][i]) + '        ' + str(tab[k+1][i]) + '        ' + str(tab[k+2][i]) + '        ' + str(tab[k+3][i]) + '        ' + str(tab[k+4][i])
        foo = foo.replace(',','')
        foo = foo.replace('[','')
        foo = foo.replace(']','')
        foo = foo.replace('0','-')
        for j in [6, 13, 35, 42, 64, 71, 93, 100, 122, 129]:
            foo = foo[:j] + '  ' + foo[j:]
        print(foo)
        if i % 3 == 2:
            print()
    print()

# Prints square with all possible numbers
for i in range(9):
    for j in range(9):
        foo = tab[10][i][j]
        foo = (9-len(foo)) * ' ' + foo
        print(foo, end=' ')
        if j in [2, 5]:
            print(' |', end=' ')
    if i % 3 == 2:
        print('\n-------------------------------------------------------------------------------------------------------------')
    else:
        print()
