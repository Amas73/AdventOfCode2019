fn = 'day06.txt'
orbits_data = [r.strip() for r in open(fn).readlines()]
orbits_data = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L']

orbits = {}
for assoc in orbits_data:
    obj = re.search('.*(?=\))',assoc)[0]
    orb = re.search('(?<=\)).*',assoc)[0]
    orbits[orb] = obj

