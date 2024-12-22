##### solutions for AOC 2024
import re
import numpy as np

def read_inputs(file):
    with open(file) as f:
        inp = f.readlines()

    out = []
    for line in inp:
        out.append(re.split('\s+', line.replace('\n','')))

    return out

def day1():
    # inp = np.asarray(read_inputs('inputs/test1.txt'), dtype=int).T
    inp = np.asarray(read_inputs('inputs/day1.txt'), dtype=int).T

    dist = abs(np.diff(np.sort(inp).T).T)
    print('Part one: ', dist.sum())

    unique0, cts0 = np.unique(np.sort(inp)[0], return_counts=True)
    unique1, cts1 = np.unique(np.sort(inp)[1], return_counts=True)

    intersect, ind0, ind1 = np.intersect1d(unique0, unique1, assume_unique=True, return_indices=True)
    sim = intersect*cts0[ind0]*cts1[ind1]
    print('Part two: ', sim.sum())

# day1()

def is_safe(line):
    if not np.all(line>0) and not np.all(line < 0):
        return False
    elif np.any(abs(line)>3):
        return False
    else:
        return True

def day2():
    inp = read_inputs('inputs/test2.txt')
    inp = read_inputs('inputs/day2.txt')

    safe = []
    for report in inp: 
        levels = np.asarray(report, dtype=int)
        safe.append(is_safe(np.diff(levels)))

    safe_guys = np.count_nonzero(safe)
    print('Part 1: ', safe_guys)

# day2()

def mult(string):
    x, y = string.split('(')[-1].split(')')[0].split(',')
    return int(x)*int(y)

def day3():
    # inp = read_inputs('inputs/test3.txt')
    inp = read_inputs('inputs/day3.txt')
    inp = ''.join(np.concatenate(inp))

    good_commands = re.findall('mul\(.?.?.?,.?.?.?\)',inp)
    real = [mult(comm) for comm in good_commands]
    print('Part 1: ', sum(real))

    #ignore stuff between do() to don't()
    split = inp.split("do()")
    enabled = ''
    for comm in split:
        enabled = enabled + comm.split("don't()")[0]
    good_commands = re.findall('mul\(.?.?.?,.?.?.?\)',enabled)
    real = [mult(comm) for comm in good_commands]
    print('Part 2: ', sum(real))

day3()