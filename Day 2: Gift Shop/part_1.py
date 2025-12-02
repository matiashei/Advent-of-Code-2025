import re

ranges = []
invalid = []

with open("input.txt") as f:
    content = f.read()

for part in content.split(","):
    start, end = part.split("-")
    ranges.append((int(start), int(end)))

for r in ranges:
    for x in range(r[0], r[1]):
        s = str(x)
        if len(s) % 2 != 0:
            continue
        i = len(s) // 2
        pattern = re.compile(r'^(\d{' + str(i) + r'})\1+$')
        if (bool(pattern.match(s))):
            invalid.append(x)

print(sum(invalid))
