import numpy as np

left, right = ([], [])
for line in open("input.txt"):
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

#part1
print(np.sum(np.abs(np.array(sorted(left)) - np.array(sorted(right)))))

#part2
print(sum([l * right.count(l) for l in left]))
