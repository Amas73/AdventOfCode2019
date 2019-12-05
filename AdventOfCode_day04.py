low_num = 130254
high_num = 678275
p1_pwds = []
p2_pwds = []

for n in range(low_num,high_num):
#def test(n):
    a,b = '',''
    dbl, dec = False, False
    cnt = 0
    rept = []
    for i in str(n):
        a = b
        b = i
        if a != '':        
            if not dbl: dbl = a == b
            if a == b: cnt += 1
            else: 
                rept.append(cnt)
                cnt = 0
            if b<a: dec = True
    rept.append(cnt)
    if dbl and not dec: p1_pwds.append(n)
    if 1 in rept and not dec: p2_pwds.append(n)

print ('Part 1 # of passwords: ' + str(len(p1_pwds)))
print ('Part 2 # of passwords: ' + str(len(p2_pwds)))