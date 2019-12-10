fn = 'day07.txt'

init_int_code = list(map(int,[r for r in open(fn).readlines()][0].split(',')))
init_int_code = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
#init_int_code = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
#init_int_code = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]


def run_int_code(phase, in_signal):
    int_code = list(init_int_code)
    cp = 0 
    while cp <= len(int_code) and int_code[cp] != 99:
        print (str(int_code[cp]))
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
                ans = phase
                phase = in_signal
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
            out_signal = ans
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
    return out_signal

max_output = 0
for amp_1 in range(5):
    for amp_2 in range(5):
        if amp_1 != amp_2:
            for amp_3 in range(5):
                if amp_1 != amp_3 and amp_2 != amp_3:
                    for amp_4 in range(5):
                        if amp_1 != amp_4 and amp_2 != amp_4 and amp_3 != amp_4:
                            for amp_5 in range(5):
                                if amp_1 != amp_5 and amp_2 != amp_5 and amp_3 != amp_5 and amp_4 != amp_5:
                                    output = 0
                                    for phase_setting in [amp_1, amp_2, amp_3, amp_4, amp_5]:
                                        output = run_int_code(phase_setting, output)
                                    max_output = max(max_output, output)

print (max_output)