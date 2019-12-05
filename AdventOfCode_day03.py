fn = 'c:/LocalData/aslade/AdventOfCode/2019/day03.txt'
wire_paths = [r for r in open(fn).readlines()]
#wire_paths = ['R8,U5,L5,D3','U7,R6,D4,L4']
#wire_paths = ['R75,D30,R83,U83,L12,D49,R71,U7,L72','U62,R66,U55,R34,D71,R55,D58,R83']
#wire_paths = ['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51','U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']

def line_intersect(p0, p1, p2, p3):
    s1_x = p1[0] - p0[0]
    s1_y = p1[1] - p0[1]
    s2_x = p3[0] - p2[0]
    s2_y = p3[1] - p2[1]
    denom = (-s2_x * s1_y + s1_x * s2_y)
    if denom !=0:
        s = (-s1_y * (p0[0] - p2[0]) + s1_x * (p0[1] - p2[1])) / denom
        t = ( s2_x * (p0[1] - p2[1]) - s2_y * (p0[0] - p2[0])) / denom
        if (s >= 0 and s <= 1 and t >= 0 and t <= 1):
            i_x = p0[0] + (t * s1_x)
            i_y = p0[1] + (t * s1_y)
            return ([i_x,i_y])
    return 0

wires = {}
for n,wire in enumerate(wire_paths):
    wires[n] = []
    x, y, l = 0, 0, 0
    wires[n].append([x, y, l])
    for path in wire.split(','):
        dir = path[:1]
        dist = int(path[1:])
        if dir == 'U': y += dist
        if dir == 'D': y += -dist
        if dir == 'R': x += dist
        if dir == 'L': x += -dist
        l += dist
        wires[n].append([x, y, l])

a, b = [], []
min_dist = 99999999
min_step = 99999999
w0_steps = 0
for n in wires[0]:
    a = list(b)
    b = n
    c, d = [], []
    if a != []:
        w1_steps = 0
        for m in wires[1]:
            c = list(d)
            d = m
            if c != [] and not (c == [0,0,0] and a == [0,0,0]):
                i = line_intersect(a,b,c,d)
                if i != 0: 
                    min_dist = min(min_dist,(abs(i[0])+abs(i[1])))
                    int_step = abs(i[0] - a[0]) + abs(i[1] - a[1]) + abs(i[0] - c[0]) + abs(i[1] - c[1])
                    min_step = min(min_step, (w0_steps + w1_steps + int_step))
            w1_steps = m[2]
    w0_steps = n[2]
                
print ('Part 1 minimum distance: ' + str(min_dist))
print ('Part 2 minimum steps: ' + str(min_step))


"""
grid = []
grid_row = []
for n in range(x_max + abs(x_min) +1):
    grid_row.append(0)

for n in range(y_max + abs(y_min) +1):
    grid.append(grid_row)
"""
