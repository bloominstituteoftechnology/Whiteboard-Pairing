

def spiralCopy(arr):

    rl = len(arr)
    cl = len(arr[0])

    print(f"rows {rl}, columns: {cl}")

    
    # number of c lengths = c - 1
    # number of r lengths = r - 1

    order = ['ltr', 'down', 'rtl', 'up']
    r = rl - 1
    c = cl

    iM = arr
#             5               3               4           2        3       1        2       0
# output: [1, 2, 3, 4, 5,  10, 15, 20,  19, 18, 17, 16,  11, 6,  7, 8, 9,  14,    13, 12]  done
#            ltr             down           rtl           up       ltr    down    rtl
#          1, 2, 3, 4, 5,  10, 15, 20,  19, 18, 17, 16,  11, 6,  7, 8, 9,  14,    13, 12]
    output = []
    index = 0
    x = 0
    y = 0
    while True:
        # print('output', output)
        if order[index] == 'ltr':
            if c == 0:
                break
            for i in range(c):
                output.append(iM[y][i + x])
            c -= 1
            x += c
            y += 1
            index += 1
        elif order[index] == 'rtl':
            if c == 0:
                break
            # print(f'rtl x: {x} y: {y} c: {c}')                
            for i in range(c):
                # print('i', i, 'value', iM[y][x - i] )
                output.append(iM[y][x - i])
            c -= 1
            x -= c 
            y -= 1
            index += 1
        elif order[index] == 'down':
            if r == 0:
                break
            # print(f'down x: {x} y: {y}')
            for i in range(r):
                # print('i', i, 'value', iM[i + y][x] )
                output.append(iM[i + y][x])
            r -= 1
            y += r
            x -= 1
            index += 1
        else: 
            assert order[index] == 'up', 'logic error'
            if r == 0:
                break
            for i in range(r):
                output.append(iM[y - i][x])
            r -= 1
            y -= r
            x += 1
            index = 0
    return output



# inputMatrix = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20]
# ]

# print(spiralCopy(inputMatrix))