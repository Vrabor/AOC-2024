reports = []
for line in open("input.txt"):
    reports.append(list(map(int, line.split())))


def safe(report):
    asc = all([report[i] < report[i + 1] for i in range(0, len(report) - 1)])
    dsc = all([report[i] > report[i + 1] for i in range(0, len(report) - 1)])
    dst = all([1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(0, len(report) - 1)])

    return (asc or dsc) and dst

def safe_tolerance(report):
    return any([safe(report[:i] + report[i + 1:]) for i in range(len(report))])

# day1
print(sum(map(safe, reports)))

# day2
print(sum(map(safe_tolerance, reports)))
