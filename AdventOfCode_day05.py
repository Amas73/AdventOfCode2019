fn = 'c:/LocalData/aslade/AdventOfCode/2019/day05.txt'
init_int_code = list(map(int,[r for r in open(fn).readlines()][0].split(',')))
#init_int_code = [3,0,4,0,99]
#init_int_code = [1002,4,3,4,33]
#init_int_code = [1101,100,-1,4,0]
#init_int_code = [3,9,8,9,10,9,4,9,99,-1,8]
#init_int_code = [3,9,7,9,10,9,4,9,99,-1,8]
#init_int_code = [3,3,1108,-1,8,3,4,3,99]
#init_int_code = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

int_code = list(init_int_code)
cp = 0 
while cp <= len(int_code) and int_code[cp] != 99:
    prog = str(int_code[cp])
    op_code = int(prog[-2:])
    p1_mode = prog[-3:-2]
    p2_mode = prog[-4:-3]
    p3_mode = prog[-5:-4]
    
    if p1_mode == '1': val1 = int_code[cp+1]
    else: val1 = int_code[int(int_code[cp+1])]
    
    if op_code in [1,2,3,7,8]:
        # UPDATE Instructions Op_Codes
        if op_code == 3:
            ans = int(input('Enter Input Code: '))
            pos = int_code[cp+1]
            inc = 2
        else:
            if p2_mode == '1': val2 = int_code[cp+2]
            else: val2 = int_code[int(int_code[cp+2])]
            val3 = int_code[cp+3]
            if op_code == 1:
                pos = val3
                ans = val1 + val2
                inc = 4
            if op_code == 2:
                pos = val3
                ans = val1 * val2
                inc = 4
            if op_code == 7:
                pos = val3
                ans = int(val1 < val2)
                inc = 4
            if op_code == 8:
                pos = val3
                ans = int(val1 == val2)
                inc = 4
        int_code[pos] = ans
    # NON-UPDATE Instructions Op_Codes
    if op_code == 4:
        ans = val1
        print ('CP:'+str(cp)+', '+str(ans))
        inc = 2
    else:
        if p2_mode == '1': val2 = int_code[cp+2]
        else: val2 = int_code[int(int_code[cp+2])]
        if op_code == 5:
            if val1 !=0:
                cp = val2
                inc = 0
            else: inc = 3
        if op_code == 6:
            if val1 ==0: 
                cp = val2
                inc = 0
            else: inc = 3

    cp = cp + inc
