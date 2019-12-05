fn = 'c:/LocalData/aslade/intcode.csv'
init_int_code = list(map(int,[r for r in open(fn).readlines()][0].split(',')))
#init_int_code = ['1,0,0,0,99']
#init_int_code = ['2,3,0,3,99']
#init_int_code = ['2,4,4,5,99,0']
#init_int_code = ['1,1,1,4,99,5,6,0,99']

def process_int_code(n, v):
    int_code = list(init_int_code)
    int_code[1] = n
    int_code[2] = v
    cp = 0 
    while int_code[cp] != 99 and cp <= len(int_code):
        prog = int_code[cp]
        val1 = int_code[int(int_code[cp+1])]
        val2 = int_code[int(int_code[cp+2])]
        pos = int_code[cp+3]
        
        if prog in [1,2]:
            if prog == 1: ans = val1 + val2
            if prog == 2: ans = val1 * val2
            int_code[pos] = ans
        cp = cp + 4
    return int_code[0]

# Part one 
noun = 12
verb = 2
print ("Part one output: " + str(process_int_code(noun, verb)))
 
#Part two
out_chk = 19690720
noun = 0
verb = 0
while True:
    if process_int_code(noun, verb) == out_chk:
        break
    verb += 1
    if verb == 100:
        noun += 1
        verb = 0

print ("Part two noun & verb: " + str(100 * noun + verb))
