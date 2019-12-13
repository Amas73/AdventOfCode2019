fn = 'day07.txt'

init_int_code = list(map(int,[r for r in open(fn).readlines()][0].split(',')))
#init_int_code = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
#init_int_code = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
#init_int_code = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
#init_int_code = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
#init_int_code = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

def run_int_code(phase, in_signal, int_code, cp = 0):
    while cp <= len(int_code) and int_code[cp] != 99:
        prog = str(int_code[cp])
        op_code = int(prog[-2:])
        p1_mode = prog[-3:-2]
        p2_mode = prog[-4:-3]
        p3_mode = prog[-5:-4]
        #print (int_code)
        #print (str(cp) + ',' + str(op_code))

        if p1_mode == '1': val1 = int_code[cp+1]
        else: val1 = int_code[int(int_code[cp+1])]
        
        if op_code in [1,2,3,7,8]:
            # UPDATE Instructions Op_Codes
            if op_code == 3:
                ans = phase
                pos = int_code[cp+1]
                phase = in_signal
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
        else:
            if op_code == 4:
                ans = val1
                out_signal = ans
                return [out_signal, False, (int_code, out_signal, cp+2)]
            else:
                if p2_mode == '1': val2 = int_code[cp + 2]
                else: val2 = int_code[int(int_code[cp + 2])]
                if op_code == 5:
                    if val1 !=0:
                        cp = val2
                        inc =  0
                    else: inc = 3
                if op_code == 6:
                    if val1 == 0: 
                        cp = val2
                        inc = 0
                    else: inc = 3
        cp = cp + inc
    return [0, True, (int_code, 0, cp)]

""" max_output = 0
for amp_a in range(5):
    for amp_b in range(5):
        if amp_a != amp_b:
            for amp_c in range(5):
                if amp_a != amp_c and amp_b != amp_c:
                    for amp_d in range(5):
                        if amp_a != amp_d and amp_b != amp_d and amp_c != amp_d:
                            for amp_e in range(5):
                                if amp_a != amp_e and amp_b != amp_e and amp_c != amp_e and amp_d != amp_e:
                                    output = 0
                                    for phase_setting in [amp_a, amp_b, amp_c, amp_d, amp_e]:
                                        amp_int_code = list(init_int_code)
                                        output = run_int_code(phase_setting, output, amp_int_code)[0]
                                    max_output = max(max_output, output)

print ('Part 1 - Max Thrust Signal: ' + str(max_output)) """

max_output = 0
for amp_a in range(5,10):
    for amp_b in range(5,10):
        if amp_a != amp_b:
            for amp_c in range(5,10):
                if amp_a != amp_c and amp_b != amp_c:
                    for amp_d in range(5,10):
                        if amp_a != amp_d and amp_b != amp_d and amp_c != amp_d:
                            for amp_e in range(5,10):
                                if amp_a != amp_e and amp_b != amp_e and amp_c != amp_e and amp_d != amp_e:
                                    output = 0
                                    end_loop, first_run = False, True
                                    amp_int_code = [(list((init_int_code)),i,0) for i in [amp_a, amp_b, amp_c, amp_d, amp_e]]
                                    while not end_loop:
                                        for x in range(5):
                                            output, end_loop, amp_int_code[x] = run_int_code(amp_int_code[x][1] if first_run else output, output, amp_int_code[x][0], amp_int_code[x][2])
                                        max_output = max(max_output, output)
                                        first_run = False

print ('Part 2 - Max Thrust Signal: ' + str(max_output))