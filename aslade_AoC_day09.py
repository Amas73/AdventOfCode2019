fn = 'day09.txt'

load_int_code = list(map(int,[r for r in open(fn).readlines()][0].split(',')))
#load_int_code = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
#load_int_code = [1102,34915192,34915192,7,4,7,99,0]
#load_int_code = [104,1125899906842624,99]
#load_int_code = [1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1101,0,3,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65]

init_int_code = {}
for n,x in enumerate(load_int_code): init_int_code[n] = x

def run_int_code(int_code, cp = 0):
    relative_base = 0
    while cp <= len(int_code) and int_code[cp] != 99:
        prog = str(int_code[cp])
        op_code = int(prog[-2:])
        p1_mode = prog[-3:-2]
        p2_mode = prog[-4:-3]
        p3_mode = prog[-5:-4]
        #print (int_code)
        #print ('RB: ' + str(relative_base) + ' (CP: ' + str(cp) +')')
        #print ('Prog: ' + prog+', Op_code: '+str(op_code)+', p_modes: ' + str(p1_mode) + ',' + str(p2_mode) + ',' + str(p3_mode))
        #print (int_code.setdefault(1000,0))

        if p1_mode == '1': val1 = int_code[cp+1]
        elif p1_mode == '2': val1 = int_code.setdefault(int(int_code[cp+1]) + relative_base,0)
        else: val1 = int_code.setdefault(int(int_code[cp+1]),0)
        if p2_mode == '1': val2 = int_code[cp+2]
        elif p2_mode == '2': val2 = int_code.setdefault(int(int_code[cp+2]) + relative_base,0)
        else: val2 = int_code.setdefault(int(int_code[cp+2]),0)
        if p3_mode == '1': val3 = int_code[cp+3]
        elif p3_mode == '2': val3 = int_code.setdefault(int(int_code[cp+3]) + relative_base,0)
        else: val3 = int_code.setdefault(int(int_code[cp+3]),0)

        #print ('Values: '+str(val1)+', '+str(val2)+', '+str(val3))
        #input('Enter Input Code: ')
        if op_code in [1,2,3,7,8]:
            # UPDATE Instructions Op_Codes
            if op_code == 3:
                ans = int(input('Enter Input Code: '))
                pos = val1
                inc = 2
                print (int_code)
                print ('RB: ' + str(relative_base) + ' (CP: ' + str(cp) +')')
                print ('Prog: ' + prog+', Op_code: '+str(op_code)+', p_modes: ' + str(p1_mode) + ',' + str(p2_mode) + ',' + str(p3_mode))
                print ('Values: '+str(val1)+', '+str(val2)+', '+str(val3))
            else:
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
                print (ans)
                inc = 2
            elif op_code == 9:
                relative_base += val1
                inc = 2
            else:
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
    return ans

output = run_int_code(init_int_code)

print ('Part 2 - Max Thrust Signal: ' + str(output))