import re

ranges = []
invalid = []
pattern = re.compile(r'^(\d+)\1+$')

with open("input.txt") as f:
    content = f.read()

for part in content.split(","):
    start, end = part.split("-")
    ranges.append((int(start), int(end)))

for r in ranges:
    for x in range(r[0], r[1]):
        if (bool(pattern.match(str(x)))):
            invalid.append(x)

print(sum(invalid))
