import re

with open('input.txt') as f:
    instr = f.read()

def solve1(mem):
    return sum(map(
        lambda x: int(x[0]) * int(x[1]), re.findall(r'mul\((\d+),(\d+)\)', mem)))

def solve2(mem):
    active = True
    res = 0
    for x, y, op in re.findall(r"mul\((\d+),(\d+)\)|(do(?:n't)?\(\))", mem):
        if op == "don't()":
            active = False
        elif op == "do()":
            active = True
        elif active:
            res += int(x) * int(y)

    return res

# Part1
print(solve1(instr))
# Part2
print(solve2(instr))
