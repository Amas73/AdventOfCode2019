import re

fn = 'day06.txt'
orbits_data = [r.strip() for r in open(fn).readlines()]
#orbits_data = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L']
#orbits_data = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L','K)YOU','I)SAN']

orbits = {}
for assoc in orbits_data:
    obj = re.search('.*(?=\))',assoc)[0]
    orb = re.search('(?<=\)).*',assoc)[0]
    orbits[orb] = obj

def orbit_counts(obj, orbit):
    cnt = 0
    while obj in orbit:
        obj = orbit[obj]
        cnt += 1
    return cnt

def orbit_shifts(obj_a, obj_b, orbit):
    a_path=[]
    while obj_a in orbit:
        a_path.append(obj_a)
        obj_a = orbit[obj_a]
    cnt_b = 0
    found = False
    while obj_b in orbit and not found:
        for cnt_a, a in enumerate(a_path):
            if obj_b == a:
                t_cnt = cnt_b + cnt_a -2
                found = True
        obj_b = orbit[obj_b]
        cnt_b += 1
    return t_cnt

tot=0
for o in orbits:
    tot += orbit_counts(o,orbits)

print ('Part 1: Total Orbits - ' + str(tot))
print ('Part 2: Orbit Transfers - ' + str(orbit_shifts('YOU','SAN',orbits)))
