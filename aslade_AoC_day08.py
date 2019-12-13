fn = 'day08.txt'

pixels = [int(ch) for ch in open(fn).read() if ch != '\n']

x_size = 25
y_size = 6

layers, cnt = [], []
p = 0
while p != len(pixels):
    row, c = [], []
    for r in range(y_size):
        r = pixels[p:p+x_size]
        row.append(r)
        c.append(dict((x,r.count(x)) for x in set(r)))
        p+=x_size
    layers.append(row)
    lc = {}
    for d in c:
        for k in d.keys():
            lc[k] = lc.get(k,0) + d[k]
    cnt.append(lc)

min_0 = 9999999
for i,d in enumerate(cnt):
    if d.get(0,0) < min_0:
        r=i
        min_0 = d.get(0,0)

print ('Part 1 : ' + str(cnt[r][1] * cnt[r][2]))

image,t=[],[]
t=[2 for i in range(x_size-len(t))]
for y in range(y_size): image.append(list(t))
for l in reversed(layers):
    for r,rw in enumerate(l):
        for c,co in enumerate(rw):
            if co != 2: 
                image[r][c] = co

print ('Part 2 :')
for r in image:
    print (''.join(str(x) for x in r).replace('1','█').replace('0','.'))