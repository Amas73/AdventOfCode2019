fn = 'c:/LocalData/aslade/advent_of_code_module_fuel.csv'
module_mass = [int(r.strip()) for r in open(fn).readlines()]

def fuel_calc(mass):
    return (int(mass/3)-2)

p1_total_fuel = 0
p2_total_fuel = 0

for i in module_mass:
    m = i
    p1 = True
    while i > 0:
        i = fuel_calc(i)
        if p1:
            p1_total_fuel = p1_total_fuel + i
            p1 = False
        if i> 0: p2_total_fuel = p2_total_fuel + i

print ('Part one - Module Fuel only: ' + str(p1_total_fuel))
print ('Part two - Module + Fuel Fuel: ' + str(p2_total_fuel))